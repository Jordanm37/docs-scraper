---
title: Markdown to DOCX
url: https://mathpix.com/markdown-to-docx
---

# Convert Markdown to DOCX

![Markdown to DOCX]()

Snip web app is a simple Markdown-powered editor, developed specifically for STEM.

It can easily convert entire documents with math, tables, and images to DOCX files, which can be opened in MS Word and Google Docs.

[Learn about Mathpix Markdown](/mathpix-markdown)

![Markdown to DOCX]()

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

DOCUMENT CONVERSION

## Our Markdown to DOCX conversion tools

Digitize and convert documents in-app or use our command line tool for local conversion.

* ### Convert PDFs to Markdown, export to DOCX

  Upload a PDF to our Snip web app to get it digitized to Mathpix Markdown. Make your edits using our lightweight markup language, and export to DOCX.

  [Get Started](https://snip.mathpix.com)[Learn more](/pdf-conversion)

* ### Create Notes from scratch

  Markdown is the most simple and straight-forward language for creating scientific documents and notes. The best part is you can export the result to DOCX anytime.

  [Get Started](https://snip.mathpix.com)[Learn more](/mathpix-markdown)

* ### Export Markdown to Word directly from the Snip app

  Our tools fit seamlessly into any workflow, so you can convert Markdown files to MS Word in just a few clicks.

  [Get Started](https://snip.mathpix.com)[Learn more](/pdf-to-word)

* ### Export to DOCX and open in Google Docs

  Convert Markdown to a DOCX file and open in Google Docs to create, share, and edit documents right in your web browser.

  [Get Started](https://snip.mathpix.com)[Learn more](/pdf-to-word)

## Mathpix Markdown (MMD)

We took standard Markdown and extended it with key LaTeX features and chemistry support.

Mathpix Markdown extends standard Markdown, for more power and control when converting your document to HTML, LaTeX, PDF, and DOCX.

![Mathpix Markdown feature details]()

![Mathpix Markdown feature details small]()

[Syntax reference](/docs/mathpix-markdown/syntax-reference)

## MPX CLI for Markdown conversion

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
mpx convert input-file.mmd output-file.docx

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