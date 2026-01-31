---
title: Markdown to LaTeX
url: https://mathpix.com/markdown-to-latex
---

# Convert Markdown to LaTeX

![Markdown Conversion graphic]()

Get the benefit of perfect LaTeX PDF rendering, while working with Markdown. Get the best of both worlds.

The most interoperable document editor for STEM. Instantly converts entire documents with math, tables, and images to LaTeX.

[Learn about Mathpix Markdown](/mathpix-markdown)

![Markdown Conversion graphic]()

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

## Our Markdown to LaTeX conversion tools

Digitize and convert documents in-app or use our command line tool for local conversion.

* ### Convert PDFs to Markdown, export to LaTeX

  Upload a PDF to our Snip web app to get it digitized to Mathpix Markdown. Make your edits using our lightweight markup language, and export to LaTeX.

  [Get Started](https://snip.mathpix.com)[Learn more](/pdf-conversion)

* ### Create Notes from scratch

  Using Markdown for creating your notes is faster and more efficient, than doing the same in LaTeX. Markdown is simple, straight-forward, and unobtrusive language. The best part is you can still export the result to LaTeX anytime.

  [Get Started](https://snip.mathpix.com)[Learn more](/mathpix-markdown)

* ### Export as a ZIP and open in any LaTeX editor

  Our tools fit seamlessly into any workflow, so downloaded files are compatible with every LaTeX environment like TeXmaker.

  [Get Started](https://snip.mathpix.com)

* ### Export to Overleaf directly from the Snip app

  Perfect match with the most commonly used online LaTeX editor. Convert Markdown to Overleaf blazingly fast.

  [Get started](https://github.com/Mathpix/mpx-cli)[Learn more](/docs/snip/snip-with-overleaf)

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
mpx convert input-file.mmd output-file.tex

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