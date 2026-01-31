---
title: Markdown Conversion
url: https://mathpix.com/markdown-conversion
---

# Convert Markdown to LaTeX, DOCX, and PDF

The most feature rich Markdown conversion tool, built for STEM researchers, students, and teachers.

![Markdown Conversion graphic]()

[Learn about Mathpix Markdown](/mathpix-markdown)

![Markdown Conversion graphic]()

## Mathpix Markdown (MMD)

We took standard Markdown and extended it with key LaTeX features and chemistry support.

  

Your LaTeX constructions are properly preserved during conversion to LaTeX, DOCX, HTML, and PDF.

![Mathpix Markdown feature details]()

![Mathpix Markdown feature details small]()

[Syntax reference](/docs/mathpix-markdown/syntax-reference)

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

## Markdown conversion support

### [Markdown to HTML](https://snip.mathpix.com)

Markdown is live previewed in your browser with HTML in the Snip web app.

[![MMD file exported to HTML.]()](https://snip.mathpix.com)

### [Markdown to DOCX](/markdown-to-docx)

Generate beautiful Word documents with one click, including editable equations and tables.

[![MMD file exported to DOCX.]()](/markdown-to-docx)

### [Markdown to LaTeX](/markdown-to-latex)

The outputs are compatible with popular LaTeX editor like Texmaker. We also have an option to export to Overleaf with one single click.

[![MMD file exported to LaTeX.]()](/markdown-to-latex)

### [Markdown to PDF](/markdown-to-pdf)

Save your Markdown file as a PDF for easy sharing. We provide the option to generate your PDF using either an HTML based approach, or via LaTeX.

[![MMD file exported to PDF.]()](/markdown-to-pdf)

## MPX CLI for Markdown conversion

Use our command line tool to convert between different filetypes using OCR technology.

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
$ mpx convert input-file.mmd output-file.tex
$ mpx convert input-file.mmd output-file.docx
$ mpx convert input-file.mmd output-file.pdf
$ mpx convert input-file.mmd output-file.html
$ mpx convert input-file.mmd output-file.pdf --pdf-method html

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