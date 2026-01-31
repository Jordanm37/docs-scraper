---
title: Introducing mpxpy (our new Python client), support for DOCX / PPTX / EPUB file formats, and more
url: https://mathpix.com/blog/mpxpy
---

# Introducing mpxpy (our new Python client), support for DOCX / PPTX / EPUB file formats, and more

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fmpxpy)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fmpxpy)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fmpxpy&title=Introducing mpxpy (our new Python client), support for DOCX / PPTX / EPUB file formats, and more)

We are excited to introduce [mpxpy](https://mathpix.com/docs/mpxpy), our **official Python client** for the Mathpix Document Conversion APIs along with features to process document and ebook formats (including DOCX, PPTX, and EPUB) with Convert API.

## About mpxpy

`mpxpy` makes it easier than ever to integrate Mathpix capabilities into your Python applications:

* Process PDFs, documents (DOCX, PPTX), and eBooks (EPUB)
* Extract and convert text and equations from images
* Convert between multiple formats (Markdown, DOCX, LaTeX, HTML, and more)
* Access structured JSON data with line-by-line information

## Getting started

To get started, install the [package](https://pypi.org/project/mpxpy) with `pip`:

```
pip install mpxpy
```

## Authentication

Set up your credentials in one of these ways:

**Method 1: Pass credentials directly**

```
client = MathpixClient(
    app_id="your-app-id",
    app_key="your-app-key"
)
```

**Method 2: Use environment variables or config files**

Set MATHPIX\_APP\_ID, MATHPIX\_APP\_KEY, and MATHPIX\_API\_URL (optional) in `~/.mpx/config`, `.env`, or `local.env`

```
client = MathpixClient()
```

## Processing PDFs and Documents

Process PDF, EPUB, DOCX, PPTX, and other file formats. Retrieve the results or save them to your local file system:

```
from mpxpy.mathpix_client import MathpixClient

client = MathpixClient(
    app_id='your-app-id',
    app_key='your-app-key'
)
```

Process a PDF file with multiple conversion formats and options:

```
pdf = client.pdf_new(
    url='https://cdn.mathpix.com/examples/cs229-notes1.pdf',
    convert_to_docx=True,
    convert_to_md=True,
)

# Wait for processing to complete. Optional timeout argument is 60 seconds by default.
pdf.wait_until_complete(timeout=30)

# Get the Markdown outputs
md_output_path = pdf.to_md_file(path='output/cs229-notes-1.md')
md_text = pdf.to_md_text() # is type str
mmd_output_path = pdf.to_mmd_file(path='output/cs229-notes-1.mmd')
mmd_text = pdf.to_mmd_text() # is type str
# Get the DOCX outputs
docx_output_path = pdf.to_docx_file(path='output/cs229-notes-1.docx')
docx_bytes = pdf.to_docx_bytes() # is type bytes
# Get the tex.zip outputs
tex_zip_output_path = pdf.to_tex_zip_file(path='output/cs229-notes-1.tex.zip')
tex_zip_bytes = pdf.to_tex_zip_bytes() # is type bytes
# Get the JSON outputs (this is automatically available without requesting its conversion)
lines_json_output_path = pdf.to_lines_json_file(path='output/cs229-notes-1.lines.json')
lines_json = pdf.to_lines_json() # parses JSON into type Dict
```

## Processing Images

You can also extract text and structured data from images:

```
from mpxpy.mathpix_client import MathpixClient

client = MathpixClient(app_id='your-app-id', app_key='your-app-key')

image = client.image_new(
    url='https://mathpix-ocr-examples.s3.amazonaws.com/cases_hw.jpg'
)

# Get Mathpix Markdown representation
mmd = image.mmd()

# Get structured JSON data
data = image.lines_json()
```

## Converting Mathpix Markdown

Convert Mathpix Markdown (MMD) to various formats:

```
from mpxpy.mathpix_client import MathpixClient

client = MathpixClient(app_id='your-app-id', app_key='your-app-key')

# Similar to Pdf, Conversion class takes separate arguments for each conversion format
conversion = client.conversion_new(
    mmd='\\frac{1}{2}',
    convert_to_docx=True,
    convert_to_md=True,
    convert_to_html=True
)

conversion.wait_until_complete() # Optional timeout argument defaults to 60 s

# Access results using the same methods as in Pdf
# Get the Markdown outputs
md_output_path = conversion.to_md_file(path='output/math-mmd.md')
md_text = conversion.to_md_text() # is type str
mmd_output_path = conversion.to_mmd_file(path='output/math-mmd.mmd')
mmd_text = conversion.to_mmd_text() # is type str
# Get the DOCX outputs
docx_output_path = conversion.to_docx_file(path='output/math-mmd.docx')
docx_bytes = conversion.to_docx_bytes() # is type bytes
# Get the tex.zip outputs
tex_zip_output_path = conversion.to_tex_zip_file(path='output/math-mmd.tex.zip')
tex_zip_bytes = conversion.to_tex_zip_bytes() # is type bytes
# Get the JSON outputs (this is automatically available without requesting its conversion)
lines_json_output_path = conversion.to_lines_json_file(path='output/math-mmd.lines.json')
lines_json = conversion.to_lines_json() # parses JSON into type Dict
```

## Contributing to mpxpy

`mpxpy` is open source, and we welcome contributions from the community! Whether you want to fix bugs, improve documentation, or add new features, your input is valuable. Visit our Github repository to learn more or submit issues and pull requests.

## Introducing document and eBook support with Convert API

The `v3/pdf` endpoint now supports input files in popular document and eBook formats like DOCX, PPTX, and EPUB. You can upload them the same way as standard PDFs. Supported formats include DOCX, PPTX, and EPUB.

For a full list of supported formats, please visit our [documentation page](https://docs.mathpix.com/#process-a-pdf).

## General improvements

This update also improves the overall OCR model accuracy. Notably, we’ve fixed a long-standing issue with Chinese text recognition: The Chinese pause comma symbol (`、`) is now correctly recognized and is no longer misconverted into a full-width comma.