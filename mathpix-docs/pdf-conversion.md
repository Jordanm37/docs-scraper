---
title: PDF Conversion
url: https://mathpix.com/pdf-conversion
---

# Convert scientific PDFs

Mathpix Snip provides world's most accurate PDFs converter with advanced support for math, tables, and chemistry.

![PDF conversion feature details]()

[Launch Snip](https://snip.mathpix.com)

![PDF conversion feature details]()

## The PDF converter with the most advanced STEM support

![PDF conversion feature details]()

[Get Started](https://snip.mathpix.com)

[Get Started](https://snip.mathpix.com)

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

## Convert PDFs to the filetype you need

No matter how or where you edit your documents, Mathpix fits seamlessly into your workflow. Getting information out of PDFs will never be a headache ever again.

### Convert PDF to Word

![PDF to MS Word]()

The best PDF to Word (.docx) converter for math, chemistry, physics, and other STEM materials. With Mathpix, you no longer need to be a LaTeX expert to edit scientific papers.

[Learn more](/pdf-to-word)

![PDF to MS Word]()

### Convert PDF to LaTeX

![PDF to LaTeX]()

Convert PDFs to LaTeX (as a .zip) that can then be used with any LaTeX editor. You can even convert your PDF directly to Overleaf.

[Learn more](/pdf-to-latex)

![PDF to LaTeX]()

### Convert PDF to HTML

![PDF to HTML]()

Convert PDFs to HTML to perfectly display your scientific content as a web page. Works great for converting unaccessible PDF documents to pages, which can be easily read with a screen reader.

[Learn more](/pdf-to-html)

![PDF to HTML]()

### Convert PDF to Mathpix Markdown

![PDF to MMD]()

Convert PDFs to Mathpix Markdown, our LaTeX-enhanced flavor of Markdown optimized for STEM content. [Learn more about Mathpix Markdown.](/mathpix-markdown)

[Learn more](/pdf-to-markdown)

![PDF to MMD]()

### Convert PDF to plain Markdown

![PDF to Markdown]()

We use Mathpix Markdown extensively because it is an expressive and feature-rich markup language for handling STEM documents that resolves many of the limitations of plain Markdown. However, modern LLMs are usually trained on plain Markdown, so we support MD outputs in our apps and API.

[Learn more](/pdf-to-markdown)

![PDF to Markdown]()

## How to convert PDFs to Word, LaTeX, Markdown, and HTML on the web

1. Drag or upload your PDF into the Mathpix Snip web editor.

2. Enter the range of pages to convert. To upload full PDF, you can leave this option blank.

3. Mathpix auto-converts it to a new document editable in the app.

4. Choose your export format in the top right corner of the page.

[Go to Snip](https://snip.mathpix.com)

* ![Upload a PDF](images/upload-pdf1.webp)
* ![Select page ranges](images/select-pages-pdf.webp)
* ![PDF is being processed](images/pdf-uploading.webp)
* ![Export your file in the needed format](images/export-pdf-docx.webp)

* ### Try it yourself

  Check out our step-by-step tutorial that guides you through the process of digitizing PDFs. Upload once, convert as many times as you want.

  [Go to Snip](https://snip.mathpix.com)

## Our PDF conversion tools

### Read your PDFs on any device

Use our PDF reader & viewer to interact with any type of PDF file on any device.

![PDF reader]()

[Learn more](/pdf-reader)

### Digitize and search PDFs

Digitize your research PDFs using OCR to create a searchable knowledge repository.

![Search PDFs]()

[Learn more](/pdf-search)

### Copy text and math from source PDF

Copy any part of a PDF in your repository in different format like LaTeX and MathML.

![Select and copy PDF parts]()

[Learn more](/pdf-data-extraction)

### Convert PDFs from your browser

We provide a Chrome extension, which allows to add and digitize PDFs from your browser.

![Chrome Extension for PDF cloud]()

[Learn more](/chrome-extension)

### Digitize PDFs, edit, and export with Snip

Use Snip to digitize all your PDFs and read them on any device. You can also create editable documents and export them to useful formats like LaTeX, DOCX, Markdown, and HTML.

![PDF features in Snip]()

[Learn more](https://snip.mathpix.com)

### Manage your PDF repository in your private cloud

Use all of the PDF processing features of Snip but with a self-hosted, fully contained solution.

![OCR PDFs on your private cloud.]()

[Learn more](/on-prem-pdf-cloud)

### Convert PDFs from the command line

Our MPX CLI command line tool converts PDF files on your local machine without needing to upload them online. You can also convert between file formats like LaTeX to Word.

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

Use the easy-to-implement Convert API to convert PDFs to alternative formats like LaTeX and DOCX. Our PDF API (v3/pdf) enables document conversion at scale.

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

## Read PDF Conversion related posts on our blog

![]()

2022-01-12

### Mathpix PDF to LaTeX Converter

Use Mathpix's simple AI-powered PDF conversion tool to convert your PDF to LaTeX and export to Overleaf.

[Read more](/blog/pdf-to-latex-converter)

![]()

2021-10-05

### Mathpix PDF to Word Converter

Need to convert your PDF to Word? Converting PDFs has never been simpler than with Mathpix’s AI-powered PDF to Word conversion.

[Read more](/blog/pdf-to-word-converter)

![]()

2021-05-21

### Convert whole PDFs to LaTeX, DOCX, Markdown; updated pricing

You can now process entire PDFs using Convert API's technology and get LaTeX, DOCX, Markdown, or HTML results via Snip or the API...

[Read more](/blog/pdf-processing-new-pricing)