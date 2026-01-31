---
title: PDF to Markdown
url: https://mathpix.com/pdf-to-markdown
---

# Convert PDF to Markdown

![PDF to Markdown]()

Mathpix Snip converts scientific PDFs to editable Markdown files in minutes. Perfectly compatible with Snip Apps and Visual Studio Code.

[Get Started](https://snip.mathpix.com)

![PDF to Markdown]()

## PDF conversion optimized for scientific documents

Mathpix is the only PDF converter with high-accuracy OCR features developed specifically for scientific documents like research papers

![PDF with an equation]()

### Equations

Even PhD-level math, physics, and statistics.

![PDF with a table]()

### Tables

High-accuracy for tables containing math symbols and full equations.

![PDF with two columns]()

### Two-column PDFs

Converts the two-column formatting required by many major journals.

## How to convert PDF to Markdown

1. Drag or upload your PDF into the Mathpix Snip web editor.

2. Enter the range of pages to convert. To upload full PDF, you can leave this option blank.

3. Mathpix auto-converts it to a new document editable in the app.

4. Click "Export" -> "Markdown" in the top right corner of the page.

[Go to Snip](https://snip.mathpix.com)

* ![Upload a PDF](images/upload-pdf1.webp)
* ![Select page ranges](images/select-pages-pdf.webp)
* ![PDF is being processed](images/pdf-uploading.webp)
* ![Export your file in the needed format](images/export-pdf-docx.webp)

## The best markup language for creating and sharing technical documents

Mathpix Markdown is a STEM-enhanced markdown, which combines math and science specific LaTeX support with standard Markdown syntax, and special extensions like SMILES for chemical diagram rendering.

![Mathpix Markdown feature details]()

![Mathpix Markdown feature details small]()

[Learn more](/mathpix-markdown)

## The best Markdown extension for VS Code

Visual Studio Code supports an .mmd extension so you can conveniently edit files on your local machine.

![VS Code feature details]()

[Installation guide](/docs/mathpix-markdown/how-to-mmd-vscode)

## Our PDF to Markdown conversion tools

### Digitize PDFs, edit, and export with Snip

Use Snip to digitize all your PDFs and read them on any device. You can also create editable Markdown documents and export them to useful formats like LaTeX, DOCX, and HTML.

![PDF features in Snip]()

[Go to Snip](https://snip.mathpix.com)

### Manage your PDF repository in your private cloud

Use all of the PDF processing features of Snip but with a self-hosted, fully contained solution.

![OCR PDFs on your private cloud.]()

[Learn more](/on-prem-pdf-cloud)

### Convert PDFs from the command line

Our MPX CLI command line tool converts PDF files on your local machine without needing to upload them online. You can also convert between file formats like LaTeX to Word using Markdown.

Copy

npm install -g @mathpix/mpx-cli
mpx login
npm install -g @mathpix/mpx-cli
export MATHPIX\_OCR\_API\_KEY=...
mpx set-api-key ...
# This will save the key in a file at
# ~/.mpx/config on Linux, macOS, or Unix
# C:\Users\USERNAME\.mpx\config on Windows
mpx convert input-file.pdf output-file.mmd
mpx convert input-file.pdf output-file.docx
mpx convert input-file.pdf output-file.tex
mpx convert input-file.pdf output-file.html
mpx convert input-file.mmd output-file.docx
mpx convert input-file.mmd output-file.tex
mpx convert input-file.mmd output-file.html
mpx convert input-file.mmd output-file.pdf
mpx convert input-file.mmd output-file.pdf --pdf-method html

[Learn more](/mpx-cli)

### Bulk PDF conversion using our API

Use the easy-to-implement Convert API to convert PDFs to alternative formats like Markdown, LaTeX, and DOCX. Our PDF API (v3/pdf) enables document conversion at scale.

Copy

curl -X POST https://api.mathpix.com/v3/pdf
-H 'app\_id: APP\_ID'
-H 'app\_key: APP\_KEY'
-H 'Content-Type: application/json'
--data '{ "url": "https://cdn.mathpix.com/examples/cs229-notes1.pdf" }'
curl --location --request POST 'https://api.mathpix.com/v3/pdf'
--header 'app\_id: APP\_ID'
--header 'app\_key: APP\_KEY'
--form 'file=@"cs229-notes5.pdf"'
--form 'options\_json="{\"math\_inline\_delimiters\": [\"$\", \"$\"]}"'

[Learn more](/convert#features)

## Read PDF to Markdown related posts on our blog

![]()

2022-03-13

### OCR-powered Markdown Table Generator

Use Mathpix’s table generator tool for easy pasting Markdown tables into editors. Forget about manually retyping tabular data and significantly boost your productivity!

[Read more](/blog/ocr-powered-markdown-table-generator)

![]()

2021-05-21

### Convert whole PDFs to LaTeX, DOCX, Markdown; updated pricing

You can now process entire PDFs using Convert API's technology and get LaTeX, DOCX, Markdown, or HTML results via Snip or the API...

[Read more](/blog/pdf-processing-new-pricing)

![]()

2019-08-30

### Snip web app (beta): OCR Powered Notes App With Latex Flavored Markdown

Snip web app released as lightweight, single user, note taking app for math, science, and engineering.

[Read more](/blog/snip-notes-beta)