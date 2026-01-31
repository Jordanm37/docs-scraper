---
title:  Mathpix CLI
url: https://mathpix.com/docs/snip/mpx-cli
---

i

* [Docs](/docs)  >
* [Snip](/docs/snip/overview)  >
* [Mathpix CLI](mpx-cli)

* [Convert files from your command line](#convert-files-from-your-command-line)
* [How to use Mathpix CLI](#how-to-use-mathpix-cli)
  + [Use MPX CLI with your Mathpix account](#use-mpx-cli-with-your-mathpix-account)
  + [Use MPX CLI with your API key](#use-mpx-cli-with-your-api-key)
* [Features](#features)
  + [1. Digitize PDFs using OCR](#1.-digitize-pdfs-using-ocr)
  + [2. Convert document filetypes using MMD](#2.-convert-document-filetypes-using-mmd)
  + [3. Convert images to LaTeX and more](#3.-convert-images-to-latex-and-more)
  + [4. Serve local MMD files and directories](#4.-serve-local-mmd-files-and-directories)

# Convert files from your command line

Use our command line tool to convert between different filetypes including PDF using OCR technology. It’s a convenient option when working with documents or images on your local file system.

![OCR PDFs on your private cloud](/images/mpx-cli-preview.webp)

# How to use Mathpix CLI

The first thing you need is to connect your Mathpix account with CLI interface.

## Use MPX CLI with your Mathpix account

Just login with your Mathpix account credentials when installing MPX CLI from the command line.

![Use MPX CLI with your Mathpix account](/images/loginmpx.webp)

```
npm install -g @mathpix/mpx-cli

mpx login
```

More details could be found here: <https://github.com/Mathpix/mpx-cli/blob/master/README.md>

## Use MPX CLI with your API key

Just set your API key as your environment variable when installing MPX CLI from the command line.

![Use MPX CLI with your API key](/images/mpxapikey.webp)

```
npm install -g @mathpix/mpx-cli

export MATHPIX_OCR_API_KEY=...

mpx set-api-key ...
# This will save the key in a file at
# ~/.mpx/config on Linux, macOS, or Unix
# C:\Users\USERNAME\.mpx\config on Windows
```

# Features

Everything you can do from the command line with MPX CLI:

## 1. Digitize PDFs using OCR

Convert PDFs from your local filesystem to formats like LaTeX, DOCX, HTML, and Markdown using OCR.

![Digitize PDFs using OCR](/images/ocr-pdf-cli.webp)

```
mpx convert input-file.pdf output-file.mmd
mpx convert input-file.pdf output-file.docx
mpx convert input-file.pdf output-file.tex
mpx convert input-file.pdf output-file.html
```

## 2. Convert document filetypes using MMD

Convert between document formats like LaTeX, DOCX, and HTML using.

![Convert document filetypes using MMD](/images/document-conversion.webp)

```
mpx convert input-file.mmd output-file.docx
mpx convert input-file.mmd output-file.tex
mpx convert input-file.mmd output-file.html
mpx convert input-file.mmd output-file.pdf
mpx convert input-file.mmd output-file.pdf --pdf-method html
```

## 3. Convert images to LaTeX and more

Use the command line to convert images to LaTeX, DOCX, MMD, and HTML like you would with Snip.

![Convert images to LaTeX and more](/images/img-cli.webp)

```
mpx convert input-file.png output-file.docx
mpx convert input-file.jpeg output-file.tex
```

## 4. Serve local MMD files and directories

Serve local MMD files and directories as a static HTML site.

![Serve local MMD files and directories](/images/serve.webp)

```
mpx serve ./input-dir
mpx serve ./input-dir/example.mmd

mpx build ./input-dir ./output-dir
```

[<   Chrome Extension](/docs/snip/extension-overview)

[Accounts & Billing   >](/docs/snip/accounts-billing)