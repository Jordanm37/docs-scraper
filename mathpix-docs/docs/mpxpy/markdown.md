---
title:  Converting Mathpix Markdown with Mathpix Python SDK
url: https://mathpix.com/docs/mpxpy/markdown
---

i

* [Docs](/docs)  >
* [Python SDK](/docs/mpxpy/overview)  >
* [Converting Mathpix Markdown](markdown)

* [Converting Mathpix Markdown (MMD) with Mathpix Python SDK](#converting-mathpix-markdown-(mmd)-with-mathpix-python-sdk)
  + [Code Example](#code-example)
  + [Rendered Output Example: From MMD to PDF](#rendered-output-example%3A-from-mmd-to-pdf)
  + [Output Formats](#output-formats)
  + [Conversion Class Documentation](#conversion-class-documentation)

# Converting Mathpix Markdown (MMD) with Mathpix Python SDK

The Mathpix Python SDK provides functionality to convert Mathpix Markdown (MMD) into other formats, such as PDF, DOCX, and standard Markdown.

## Code Example

```
from mpxpy.mathpix_client import MathpixClient

client = MathpixClient(
    app_id="your-app-id",
    app_key="your-app-key"
)

# Define the Mathpix Markdown input with headers, math, and a table

mmd_input = """
## Part I

## Linear Regression

To make our housing example more interesting, let's consider a slightly richer dataset in which we also know the number of bedrooms in each house:

| Living area $\\left(\\text{feet}^{2}\\right)$ | \\#bedrooms | Price (1000\\$s) |
|:---:|:---:|:---:|
| 2104 | 3 | 400 |
| 1600 | 3 | 330 |
| 2400 | 3 | 369 |
| 1416 | 2 | 232 |
| 3000 | 4 | 540 |
| $\\vdots$ | $\\vdots$ | $\\vdots$ |

To perform supervised learning, we must decide how we're going to represent functions/hypotheses $h$ in a computer. As an initial choice, let's say we decide to approximate $y$ as a linear function of $x$:

$$
h_{\\theta}(x) = \\theta_{0} + \\theta_{1} x_{1} + \\theta_{2} x_{2}
$$

In the case where we have only one training example $(x, y)$, so that we can neglect the sum in the definition of $J$, we have:

$$
\\begin{aligned}
\\frac{\\partial}{\\partial \\theta_j} J(\\theta)
&= \\frac{\\partial}{\\partial \\theta_j} \\frac{1}{2} \\left(h_\\theta(x) - y\\right)^2 \\\\
&= \\left(h_\\theta(x) - y\\right) \\cdot \\frac{\\partial}{\\partial \\theta_j} \\left(h_\\theta(x) - y\\right)
\\end{aligned}
$$
"""

# Convert MMD to PDF (you can also use "docx", "html", or "md")
conversion = client.conversion_new(
    mmd=mmd_input,
    convert_to_pdf=True,
    convert_to_docx=True,
    convert_to_md=True,
)

# Wait for the conversion to complete
conversion.wait_until_complete(timeout=30)

# Get the PDF outputs
pdf_output_path = conversion.to_pdf_file(path='output/sample.pdf')
# Get the Markdown outputs
md_output_path = conversion.to_md_file(path='output/sample.md')
md_text = conversion.to_md_text() # is of type str
# Get the DOCX outputs
docx_output_path = conversion.to_docx_file(path='output/sample.docx')
docx_bytes = conversion.to_docx_bytes() # is of type bytes
```

* Use `to_*` methods to either get the result in memory or save it directly to a file.
* Saving to file always requires setting the `path` explicitly — the SDK will not guess or generate filenames automatically.
* All folders in the provided `path` are created automatically if they do not exist.
* If you only need in-memory content (e.g. for sending over a network or writing to a DB), use the `to_*_bytes()` or `to_*_text()` methods.
* You can also render PDF from LaTeX using `convert_to_latex_pdf=True`. This uses Mathpix's LaTeX renderer instead of MMD.

## Rendered Output Example: From MMD to PDF

![Processing an Markdown](/images/SDK-processing-markdown.webp)

This view shows the final PDF output generated from Mathpix Markdown input. It demonstrates how headers, LaTeX equations, and tables are rendered using the Mathpix SDK.

## Output Formats

* **PDF**  
  Saved to: `output/sample.pdf`  
  Ideal for print-ready rendering from Mathpix Markdown input.
* **Markdown**  
  Saved to: `output/sample.md`  
  Also available in-memory using `conversion.to_docx_bytes()` — useful for returning as a file in web apps.
* **DOCX**  
  Saved to: `output/sample.docx`  
  Also available as bytes using `conversion.to_docx_bytes()`.

Other formats such as HTML and LaTeX ZIP are supported as well — see the full method list below.

---

## Conversion Class Documentation

**Properties**

* `auth`: An Auth instance with Mathpix credentials.
* `conversion_id`: The unique identifier for this conversion.
* `convert_to_docx`: Optional boolean to automatically convert your result to docx
* `convert_to_md`: Optional boolean to automatically convert your result to md
* `convert_to_tex_zip`: Optional boolean to automatically convert your result to tex.zip
* `convert_to_html`: Optional boolean to automatically convert your result to html
* `convert_to_pdf`: Optional boolean to automatically convert your result to pdf
* `convert_to_latex_pdf`: Optional boolean to automatically convert your result to pdf containing LaTeX

**Methods**

* `wait_until_complete`: Wait for the conversion to complete.
* `conversion_status`: Get the current status of the conversion.
* `to_docx_file`: Save the processed conversion result to a DOCX file at a local path.
* `to_docx_bytes`: Get the processed conversion result as DOCX bytes.
* `to_md_file`: Save the processed conversion result to a Markdown file at a local path.
* `to_md_text`: Get the processed conversion result as a Markdown string.
* `to_mmd_file`: Save the processed conversion result to a Mathpix Markdown file at a local path.
* `to_mmd_text`: Get the processed conversion result as a Mathpix Markdown string.
* `to_tex_zip_file`: Save the processed conversion result to a tex.zip file at a local path.
* `to_tex_zip_bytes`: Get the processed conversion result in tex.zip format as bytes.
* `to_html_file`: Save the processed conversion result to a HTML file at a local path.
* `to_html_bytes`: Get the processed conversion result in HTML format as bytes.
* `to_pdf_file`: Save the processed conversion result to a PDF file at a local path.
* `to_pdf_bytes`: Get the processed conversion result in PDF format as bytes.
* `to_latex_pdf_file`: Save the processed conversion result to a PDF file containing LaTeX at a local path.
* `to_latex_pdf_bytes`: Get the processed conversion result in PDF format as bytes (with LaTeX).

[<   Processing PDFs](/docs/mpxpy/pdf)

[Available Output Formats   >](/docs/mpxpy/formats)