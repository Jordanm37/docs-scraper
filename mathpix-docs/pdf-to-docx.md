---
title: PDF to DOCX
url: https://mathpix.com/pdf-to-docx
---

# Convert PDF to DOCX

Mathpix Snip converts scientific PDFs to editable DOCX files in minutes.

Works on PDFs containing math, tables, and figures

Works on two-column PDFs

Optimized for scientific papers

Advanced foreign language support

Easy exporting to DOCX in seconds

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

## How to convert PDF to DOCX

1. Drag or upload your PDF into the Mathpix Snip web editor.

2. Enter the range of pages to convert. To upload full PDF, you can leave this option blank.

3. Mathpix auto-converts it to a new document editable in the app.

4. Click "Export" -> "DOCX" in the top right corner of the page.

[Go to Snip](https://snip.mathpix.com)

* ![Upload a PDF](images/upload-pdf1.webp)
* ![Select page ranges](images/select-pages-pdf.webp)
* ![PDF is being processed](images/pdf-uploading.webp)
* ![Export your file in the needed format](images/export-pdf-docx.webp)

## Our PDF to DOCX conversion tools

### Digitize PDFs, edit, and export with Snip

Use Snip to digitize all your PDFs and read them on any device. You can also create editable documents and export them to DOCX and useful formats like LaTeX, Markdown, and HTML.

![PDF features in Snip]()

[Go to Snip](https://snip.mathpix.com)

### Manage your PDF repository in your private cloud

Use all of the PDF processing features of Snip but with a self-hosted, fully contained solution.

![OCR PDFs on your private cloud.]()

[Learn more](/on-prem-pdf-cloud)

### Read your PDFs on any device

Use our PDF reader & viewer to interact with virtually any type of PDF file.

![PDF reader]()

[Learn more](/pdf-reader)

### Digitize and search PDFs

Digitize your research PDFs using OCR to create a searchable knowledge repository.

![Search PDFs]()

[Learn more](/pdf-search)

### Convert PDFs from the command line

Our MPX CLI command line tool converts PDF files on your local machine without needing to upload them online. You can also convert between file formats like LaTeX to DOCX.

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

Use the easy-to-implement Convert API to convert PDFs to alternative formats like DOCX. Our PDF API (v3/pdf) enables document conversion at scale.

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

## Read PDF to DOCX related posts on our blog

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

![]()

2020-09-02

### Major improvements to MS Word compatibility

Mathpix Snip is more compatible with Microsoft Word than ever with a new MathML format enabling better multiline equations, summations, and integrals in Word.

[Read more](/blog/improved-compatibility-msword)