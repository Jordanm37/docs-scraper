---
title: Markdown to PDF
url: https://mathpix.com/markdown-to-pdf
---

# Convert Markdown to PDF

Generate PDFs from your Markdown editor. You can generate your PDF using an HTML based method, or you can generate a PDF using LaTeX itself.

PDF with LaTeX option offers deep integration with Mathpix Markdown LaTeX features

Works on Markdown files with math, text, image URLs, tables, and chemistry

![Markdown to PDF graphic]()

[Learn about Mathpix Markdown](/mathpix-markdown)

![Markdown to PDF graphic]()

## Markdown conversion optimized for scientific documents

Since Mathpix Markdown is a strict superset of Markdown, our conversion tooling for MMD is more powerful than what is possible with standard Markdown.

![Document with an equation]()

### Equations

Advanced support for math, physics, and statistics expressions via Mathjax, including equation references via the \eqref, \label, \ref commands

![Document with a table]()

### Tables

Full support for LaTeX style tabular environments in addition to Markdown style tables

![Document with an image]()

### Images

Figures are preserved in the output documents as expected; for LaTeX outputs, which are returned as compressed zip files, they are put in a special images folder

## The easiest way to edit PDFs

1. Drag or upload a PDF into the Mathpix Snip web editor.

2. When PDF is uploaded, open it and click "Create" -> "New Note".

3. Make changes to your new Note.

4. Export your Note as a PDF file.

* ![Upload a PDF](images/markdown-to-pdf1.webp)
* ![Create a new Note to edit](images/markdown-to-pdf2.webp)
* ![Make any edits in Markdown section](images/markdown-to-pdf3.webp)
* ![Export Markdown to PDF](images/markdown-to-pdf4.webp)

## Mathpix Markdown (MMD)

We took standard Markdown and extended it with key LaTeX features and chemistry support.

Mathpix Markdown extends standard Markdown, for more power and control when converting your document to HTML, LaTeX, PDF, and DOCX.

![Mathpix Markdown feature details]()

![Mathpix Markdown feature details small]()

[Syntax reference](/docs/mathpix-markdown/syntax-reference)

## MPX CLI tool for Markdown conversion

### Convert

Convert Markdown files to other formats on your local machine.

Copy

npm install -g @mathpix/mpx-cli
mpx login
npm install -g @mathpix/mpx-cli
export MATHPIX\_OCR\_API\_KEY=...
mpx set-api-key ...
# This will save the key in a file at
# ~/.mpx/config on Linux, macOS, or Unix
# C:\Users\USERNAME\.mpx\config on Windows
mpx convert input-file.mmd output-file.pdf

[Learn more](/mpx-cli)

### Verify

Serve local MMD files as a static HTML site to check results.

Copy

$ mpx serve. /input-dir
$ mpx serve. /input-dir/example.mmd
$ mpx build. /input-dir. /output-dir

[Learn more](/mpx-cli)

## Read Markdown Conversion related posts on our blog

![]()

2022-03-13

### OCR-powered Markdown Table Generator

Use Mathpix’s table generator tool for easy pasting Markdown tables into editors. Forget about manually retyping tabular data and significantly boost your productivity!

[Read more](/blog/ocr-powered-markdown-table-generator)

![]()

2021-05-21

### Convert whole PDFs to LaTeX, DOCX, Markdown; updated pricing

You can now process entire PDFs using Mathpix's OCR technology and get LaTeX, DOCX, Markdown, or HTML results via Snip or the API...

[Read more](/blog/pdf-processing-new-pricing)

![]()

2022-01-12

### Mathpix PDF to LaTeX Converter

Use Mathpix's simple AI-powered PDF conversion tool to convert your PDF to LaTeX and export to Overleaf.

[Read more](/blog/pdf-to-latex-converter)