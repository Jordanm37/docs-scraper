---
title:  Available Output Formats in Mathpix Python SDK
url: https://mathpix.com/docs/mpxpy/formats
---

* [Docs](/docs)  >
* [Python SDK](/docs/mpxpy/overview)  >
* [Available Output Formats](formats)

# Available Output Formats in Mathpix Python SDK

The Mathpix Python SDK allows you to convert input from **images**, **PDFs**, or **Mathpix Markdown (MMD)** into a wide range of output formats and download them locally.

## Supported Output Formats

| Format | Description | Supported endpoints |
| --- | --- | --- |
| **pdf** | Vector PDF of the rendered content | `/v3/pdf`, `/v3/converter` |
| **latex\_pdf** | PDF rendered from LaTeX instead of MMD | `/v3/pdf`, `/v3/converter` |
| **docx** | Microsoft Word file with styled math & text | `/v3/pdf`, `/v3/converter` |
| **md** | Plain UTF-8 Markdown | `/v3/pdf`, `/v3/converter` |
| **mmd** | Mathpix Markdown (source format with LaTeX) | `/v3/text`, `/v3/pdf` |
| **html** | Self-contained HTML document | `/v3/pdf`, `/v3/converter` |
| **tex\_zip** | Zipped folder with LaTeX sources & images | `/v3/pdf`, `/v3/converter` |
| **json** | Line-by-line OCR output as structured JSON | `/v3/text`, `/v3/pdf` |
| **mmd\_json** | Line-by-line JSON (content in MMD) | `/v3/pdf` |

The `to_*` and `to_*_file()` helpers in the SDK automatically pick the correct endpoint based on your request.

## Which inputs can you send to each endpoint?

| Endpoint | Purpose | Supported Input Types |
| --- | --- | --- |
| `/v3/text` | OCR for images and small documents | JPEG (`.jpeg`, `.jpg`, `.jpe`), PNG (`.png`), BMP (`.bmp`, `.dib`), JPEG 2000 (`.jp2`), WebP (`.webp`), Portable image formats (`.pbm`, `.pgm`, `.ppm`, `.pxm`, `.pnm`), PFM (`.pfm`), Sun Raster (`.sr`, `.ras`), TIFF (`.tiff`, `.tif`), OpenEXR (`.exr`), Radiance HDR (`.hdr`, `.pic`), GDAL-compatible raster/vector formats |
| `/v3/pdf` | OCR and conversion for documents | PDF, EPUB, DOCX, PPTX, AZW/AZW3/KFX (Kindle), MOBI, DJVU, DOC, WPD (WordPerfect), ODT (OpenDocument Text) |
| `/v3/converter` | Convert Mathpix Markdown to other formats | MMD string |

## Code Example

```
from mpxpy.mathpix_client import MathpixClient

client = MathpixClient(
    app_id="your-app-id",
    app_key="your-app-key"
)

# Convert MMD to PDF and Markdown
conversion = client.conversion_new(
    mmd="E = mc^2",
    convert_to_pdf=True,
    convert_to_md=True
)

# Wait until the conversion finishes
conversion.wait_until_complete(timeout=30)

# Save results to local files
pdf_path = conversion.to_pdf_file(path='output/equation.pdf')
md_path = conversion.to_md_file(path='output/equation.md')

# Optional: access content in memory
pdf_bytes = conversion.to_pdf_bytes()
md_text = conversion.to_md_text()
```

After running this script, the following files will be saved locally:

* `output/equation.pdf` – the formatted PDF output
* `output/equation.md` – the Markdown version of the input

## Output Options Summary

* Use `to_*_file(path)` methods to save results directly to disk.
* Use `to_*_bytes()` or `to_*_text()` for in-memory access (useful for web services or databases).
* You can request multiple formats in the same API call by setting multiple `convert_to_*` flags.
* Not all formats are supported for all input types — see the [full conversion spec](https://docs.mathpix.com).

[<   Converting Mathpix Markdown](/docs/mpxpy/markdown)

[Error Handling and Debugging   >](/docs/mpxpy/errors)