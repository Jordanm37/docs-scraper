---
title: Streaming API for PDF OCR
url: https://mathpix.com/blog/streaming-api-for-pdfs
---

# Streaming API for PDF OCR

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fstreaming-api-for-pdfs)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fstreaming-api-for-pdfs)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fstreaming-api-for-pdfs&title=Streaming API for PDF OCR)

We are excited to announce that our PDF API now provides a streaming endpoint, `GET api.mathpix.com/v3/pdf/{pdf_id}/stream`, which dramatically lowers latencies for real-time applications. Previously, polling was required to retrieve results; with the new streaming API, polling is no longer needed for this purpose.

Pages are streamed sequentially. Each page’s result is streamed as a JSON message using server-side events. A PDF that may take 20 seconds to complete will start providing results for the first few pages in as little as 2-3 seconds.

You can find the documentation for the new streaming endpoint in our [API Docs](https://docs.mathpix.com/?python#stream-pdf-pages).

To use the new endpoint, you must first set `streaming` to `true` when you upload your PDF via `POST api.mathpix.com/v3/pdf`, as documented in [PDF request parameters](https://docs.mathpix.com#request-parameters-for-uploading-pdfs). Once this is done, you can make the corresponding GET request to stream the page results.

Calling `GET api.mathpix.com/v3/pdf/{pdf_id}/stream` enables clients to stream page-by-page results containing Mathpix Markdown.

The streaming API dramatically lowers latency to first data but may slightly increase the total amount of time required to process the entire PDF. Page results are streamed sequentially. Each JSON page message contains a `text` field to hold the Mathpix Markdown output for that page, a `page_idx` field, and a `pdf_selected_len` field.

This streaming API will be particularly useful for real-time applications, such as RAG and Document Question Answering.

Please contact us at [support@mathpix.com](mailto:support@mathpix.com) with any feature requests or suggestions for the streaming API. We expect to add new API features soon.

## Other updates and bugfixes

* Improved detection of abstracts, titles, and other semantic text categories. Notably, we now allow for multiple `\title{}` elements in a single PDF.
* Improved support for custom math display delimiters, particularly for cases with equation tags.
* Prevented multicolumn overflow by respecting the total number of table columns.
* Resolved a bug that caused internal error responses during spellcheck.
* Fixed an issue where table cell delimiters (`&`) were not escaped inside sub-environments (e.g., `\begin{aligned}...\end{aligned}` within a table cell).
* Addressed a minor bug in the `gathered` math environment.
* Fixed an issue with nested `align*` environments when `"include_equation_tags": true`.