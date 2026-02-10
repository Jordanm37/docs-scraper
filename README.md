# docs-scraper

A fast, async Python tool that scrapes documentation websites and converts them to clean Markdown files.

## Features

- **Async crawling** with configurable concurrency via `asyncio` and `httpx`
- **Sitemap-aware** -- automatically discovers pages from `sitemap.xml` (including sitemap indexes) before falling back to link crawling
- **Smart content extraction** -- strips nav, header, footer, and script tags; targets `<main>`, `<article>`, and common doc-content selectors
- **Markdown output** with YAML frontmatter (title, source URL) for each page
- **Rate limiting** through `asyncio.Semaphore` to avoid overwhelming target servers
- **JSON sitemap** generated alongside output for programmatic use

## Installation

Requires Python 3.10+.

```bash
git clone https://github.com/Jordanm37/docs-scraper.git
cd docs-scraper
poetry install
```

## Usage

```bash
# Basic -- scrape a docs site into ./output
poetry run python scrape_docs.py https://docs.example.com

# Custom output directory
poetry run python scrape_docs.py https://docs.example.com --output ./my-docs

# Limit pages and concurrency
poetry run python scrape_docs.py https://docs.example.com --max-pages 50 --concurrency 5
```

### CLI Options

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--output` | `-o` | `output` | Output directory for Markdown files |
| `--max-pages` | `-m` | `500` | Maximum number of pages to scrape |
| `--concurrency` | `-c` | `10` | Number of concurrent requests |

## Output Structure

```
output/
  _sitemap.json        # Index of all scraped pages
  index.md             # Root page
  getting-started.md   # Converted doc pages...
  api/
    reference.md
```

Each `.md` file includes frontmatter:

```yaml
---
title: Page Title
url: https://docs.example.com/page
---
```

## License

MIT
