#!/usr/bin/env python3
"""
Docs Scraper - Scrape documentation sites to markdown.

Usage:
    poetry run python scrape_docs.py https://docs.example.com
    poetry run python scrape_docs.py https://docs.example.com --output ./my-docs
    poetry run python scrape_docs.py https://docs.example.com --max-pages 50
"""

import argparse
import asyncio
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Increase recursion limit for deeply nested HTML
sys.setrecursionlimit(10000)


class DocsScraper:
    def __init__(
        self,
        base_url: str,
        output_dir: str = "output",
        max_pages: int = 500,
        concurrency: int = 10,
    ):
        self.base_url = base_url.rstrip("/")
        self.base_domain = urlparse(base_url).netloc
        self.output_dir = Path(output_dir)
        self.max_pages = max_pages
        self.concurrency = concurrency
        self.visited: set[str] = set()
        self.pages: dict[str, dict] = {}
        self.semaphore = asyncio.Semaphore(concurrency)

    def normalize_url(self, url: str) -> str:
        """Normalize URL for deduplication."""
        parsed = urlparse(url)
        # Remove fragments, normalize path
        path = parsed.path.rstrip("/") or "/"
        return f"{parsed.scheme}://{parsed.netloc}{path}"

    def is_same_domain(self, url: str) -> bool:
        """Check if URL belongs to same domain."""
        return urlparse(url).netloc == self.base_domain

    def url_to_filepath(self, url: str) -> Path:
        """Convert URL to local file path."""
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        if not path:
            path = "index"
        # Clean up path for filesystem
        path = re.sub(r"[<>:\"|?*]", "_", path)
        if not path.endswith(".md"):
            path = f"{path}.md"
        return self.output_dir / path

    async def fetch(self, client: httpx.AsyncClient, url: str) -> str | None:
        """Fetch URL content with rate limiting."""
        async with self.semaphore:
            try:
                resp = await client.get(url, follow_redirects=True, timeout=30)
                if resp.status_code == 200:
                    return resp.text
            except Exception as e:
                print(f"  Error fetching {url}: {e}")
        return None

    async def get_sitemap_urls(self, client: httpx.AsyncClient) -> list[str]:
        """Try to get URLs from sitemap.xml."""
        sitemap_urls = [
            f"{self.base_url}/sitemap.xml",
            f"{self.base_url}/sitemap_index.xml",
            f"{self.base_url}/sitemap-0.xml",
        ]

        urls = []
        for sitemap_url in sitemap_urls:
            content = await self.fetch(client, sitemap_url)
            if content:
                try:
                    # Handle sitemap index
                    root = ET.fromstring(content)
                    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

                    # Check for sitemap index
                    sitemaps = root.findall(".//sm:sitemap/sm:loc", ns)
                    if sitemaps:
                        for sm in sitemaps:
                            sub_content = await self.fetch(client, sm.text)
                            if sub_content:
                                sub_root = ET.fromstring(sub_content)
                                for loc in sub_root.findall(".//sm:loc", ns):
                                    if self.is_same_domain(loc.text):
                                        urls.append(loc.text)
                    else:
                        # Regular sitemap
                        for loc in root.findall(".//sm:loc", ns):
                            if self.is_same_domain(loc.text):
                                urls.append(loc.text)

                    if urls:
                        print(f"Found {len(urls)} URLs in sitemap")
                        return urls
                except ET.ParseError:
                    continue

        return urls

    def extract_links(self, html: str, base_url: str) -> list[str]:
        """Extract internal links from HTML."""
        soup = BeautifulSoup(html, "lxml")
        links = []

        for a in soup.find_all("a", href=True):
            href = a["href"]
            # Skip anchors, javascript, mailto
            if href.startswith(("#", "javascript:", "mailto:", "tel:")):
                continue

            full_url = urljoin(base_url, href)
            normalized = self.normalize_url(full_url)

            if self.is_same_domain(normalized) and normalized not in self.visited:
                links.append(normalized)

        return links

    def extract_content(self, html: str) -> tuple[str, str]:
        """Extract main content and title from HTML."""
        soup = BeautifulSoup(html, "lxml")

        # Get title
        title = ""
        if soup.title:
            title = soup.title.string or ""
        if not title:
            h1 = soup.find("h1")
            if h1:
                title = h1.get_text(strip=True)

        # Remove unwanted elements
        for tag in soup.find_all(["nav", "header", "footer", "aside", "script", "style", "noscript"]):
            tag.decompose()

        # Try to find main content
        main_content = None
        for selector in ["main", "article", '[role="main"]', ".content", ".docs-content", "#content", ".markdown-body"]:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if not main_content:
            main_content = soup.body or soup

        # Convert to markdown with error handling
        try:
            markdown = md(str(main_content), heading_style="ATX", strip=[])
        except RecursionError:
            # Fallback: just get text content
            markdown = main_content.get_text(separator="\n\n", strip=True)

        # Clean up excessive whitespace
        markdown = re.sub(r"\n{3,}", "\n\n", markdown)
        markdown = markdown.strip()

        return title, markdown

    async def crawl(self, client: httpx.AsyncClient, start_urls: list[str]) -> None:
        """Crawl pages starting from given URLs."""
        queue = list(start_urls)

        while queue and len(self.visited) < self.max_pages:
            # Process batch
            batch = []
            while queue and len(batch) < self.concurrency:
                url = queue.pop(0)
                if url not in self.visited:
                    batch.append(url)
                    self.visited.add(url)

            if not batch:
                break

            # Fetch batch in parallel
            tasks = [self.fetch(client, url) for url in batch]
            results = await asyncio.gather(*tasks)

            for url, html in zip(batch, results):
                if html:
                    try:
                        title, content = self.extract_content(html)
                        self.pages[url] = {"title": title, "content": content}
                        print(f"  [{len(self.pages)}/{self.max_pages}] {url}")

                        # Add new links to queue
                        new_links = self.extract_links(html, url)
                        queue.extend([l for l in new_links if l not in self.visited])
                    except Exception as e:
                        print(f"  Error processing {url}: {e}")

    def save_pages(self) -> None:
        """Save all pages to files."""
        self.output_dir.mkdir(parents=True, exist_ok=True)

        for url, data in self.pages.items():
            filepath = self.url_to_filepath(url)
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Add frontmatter
            content = f"---\ntitle: {data['title']}\nurl: {url}\n---\n\n{data['content']}"
            filepath.write_text(content, encoding="utf-8")

        print(f"\nSaved {len(self.pages)} pages to {self.output_dir}")

    def save_sitemap(self) -> None:
        """Save sitemap/link tree as JSON."""
        sitemap = {
            "base_url": self.base_url,
            "total_pages": len(self.pages),
            "pages": [
                {"url": url, "title": data["title"], "file": str(self.url_to_filepath(url))}
                for url, data in sorted(self.pages.items())
            ],
        }

        sitemap_path = self.output_dir / "_sitemap.json"
        sitemap_path.write_text(json.dumps(sitemap, indent=2), encoding="utf-8")
        print(f"Saved sitemap to {sitemap_path}")

    async def run(self) -> None:
        """Main entry point."""
        print(f"Scraping {self.base_url}")
        print(f"Output: {self.output_dir.absolute()}")
        print(f"Max pages: {self.max_pages}")
        print()

        async with httpx.AsyncClient(
            headers={"User-Agent": "DocsScraper/1.0"},
            follow_redirects=True,
        ) as client:
            # Try sitemap first
            print("Checking for sitemap...")
            urls = await self.get_sitemap_urls(client)

            if not urls:
                print("No sitemap found, crawling from base URL...")
                urls = [self.base_url]

            # Crawl
            print("\nScraping pages...")
            await self.crawl(client, urls)

        # Save results
        print("\nSaving files...")
        self.save_pages()
        self.save_sitemap()

        print("\nDone!")


def main():
    parser = argparse.ArgumentParser(description="Scrape documentation sites to markdown")
    parser.add_argument("url", help="Base URL of the documentation site")
    parser.add_argument("--output", "-o", default="output", help="Output directory")
    parser.add_argument("--max-pages", "-m", type=int, default=500, help="Maximum pages to scrape")
    parser.add_argument("--concurrency", "-c", type=int, default=10, help="Concurrent requests")

    args = parser.parse_args()

    scraper = DocsScraper(
        base_url=args.url,
        output_dir=args.output,
        max_pages=args.max_pages,
        concurrency=args.concurrency,
    )

    asyncio.run(scraper.run())


if __name__ == "__main__":
    main()
