---
title: Convert API: Image & PDF digitizing API for STEM
url: https://mathpix.com/convert
---

# Convert API for STEM

Image & PDF digitizing software for STEM companies. Make creating and searching STEM content easy for your end users.

Battle-tested with deep functionality, including math equations, chemical diagrams, tables, and full PDF document conversion.

Compatible with industry standards like PDFs, LaTeX, Asciimath, MathML, Markdown, HTML, and SMILES (for chemistry).

[Get Started](https://console.mathpix.com)[Go to Docs](/docs/convert/overview)[API reference](https://docs.mathpix.com)

[Get Started](https://console.mathpix.com)[Go to Docs](https://mathpix.com/docs/convert/overview)

![Example API request](images/ocr/ocr-hero-desktop.webp)

![Example API request](images/ocr/ocr-hero-mobile.webp)

## The most trusted, innovative, and limit-pushing OCR provider for STEM

![latency](images/latency.svg)

### Low latency

We are constantly pushing the boundaries of what is possible for image recognition while maintaining extremely low latencies.

![Medal](images/medal.svg)

### Industry leader

Due to our exceptional accuracy and constant innovation, we are the most trusted brand for OCR among [leaders in online math education](#customers).

![graph](images/graph.svg)

### Battle-tested reliability

We process over 10 million images every day. Our system is battle tested and reliable with 99.9%+ uptime.

## Our API capabilities

Convert API is the industry leading computer vision solution for all things STEM. We excel at processing documents that are technical in nature and contain structured data.

![](images/ocr/ocr-api-text.png)

Text

Scan text and handwriting from images and PDFs.

![](images/ocr/ocr-api-math.png)

Math

The industry standard for processing images and documents with PhD level math.

![](images/ocr/ocr-api-chem.png)

Chemical diagram

OCR printed and handwritten molecules.

![](images/ocr/ocr-api-code.png)

Code

Extract perfectly formatted code snippets from images and PDFs.

![](images/ocr/ocr-api-table.png)

Table

Complex tables are no match for Convert API. Scan tabular data in seconds.

![](images/ocr/ocr-api-chart.png)

Charts

## All Convert API endpoints

* **v3/text**

  ### Process an image

  This is our most widely used endpoint. You can use this endpoint to OCR individual images of handwritten and printed equations, handwritten and printed text, tables, and diagrams to get digital formats like LaTeX, Asciimath, and MathML.

  [Developer Docs](https://docs.mathpix.com/#process-an-image)
* ![Process an image using the v3/text API endpoint]()

* **v3/pdf**

  ### Process a PDF

  Use this endpoint to OCR PDFs and convert them to other formats. This endpoint works asynchronously, since large PDF files can take several minutes to process. v3/pdf accepts PDF files and URLs in the request.

  [Developer Docs](https://docs.mathpix.com/#process-a-pdf)
* ![Process an image using the v3/text API endpoint]()

* **v3/strokes**

  ### Process strokes (digital ink)

  Use this endpoint to add stroke recognition (i.e. digital ink) to your app. This endpoint works for all math, and for Hindi and Latin alphabet language text. You can process the data for each individual stroke, or you can use a session\_id for live drawing capabilities in your app.

  [Developer Docs](https://docs.mathpix.com/#process-stroke-data)

* **v3/batch**

  ### Process a batch of images

  Use this endpoint to process multiple images in a single POST request. The request will return a batch ID which is queried with a GET request once an appropriate amount of time has passed for the images to process. You should only use the batch endpoint if your workflow is not latency sensitive.

  [Developer Docs](https://docs.mathpix.com/#process-a-batch)
* ![Process a batch of images using the v3/batch endpoint]()

Industry leaders trust Mathpix

![Anthropic logo]()

![Gemini AI logo]()

![Tencent logo]()

![Perplexity logo]()

![Chegg logo]()

FEATURES

## Digitize entire PDFs

PDFs are first converted into Mathpix Markdown, from which they can be exported to DOCX / MS Word, LaTeX, and PDF. Text, diagrams, equations, and tables, are extracted from the PDF.

### Original PDF

![Example PDF]()

xml version="1.0" encoding="UTF-8"?

271218
Created with Sketch.

### Extracted Mathpix Markdown

![Example equation]()

xml version="1.0" encoding="UTF-8"?

271218
Created with Sketch.

### Rendered result

![Example equation]()

[Go to PDF API docs](https://docs.mathpix.com/#process-a-pdf)

## Supported image types

  

Use Convert API to very accurately convert images of simple and complicated printed and handwritten math, text, tables, and chemical diagrams.

  

We can also [recognize all the world's most spoken languages](/docs/convert/supported_languages) like English, Vietnamese, Spanish, French, German, Hindi, Chinese, Japanese, Russian, Korean, Thai, and more.

![](images/ocr/bayes_theorem.webp)

Equations

![](images/ocr/matrix.webp)

Matrices

![](images/ocr/handwritten.webp)

Word problems

![](images/ocr/chem_eq.webp)

Chemical equations

![](images/ocr/printed_tx.webp)

Multiple choice questions

![](images/ocr/table.webp)

Tables

![](images/ocr/chinese.webp)

Foreign alphabet text

![](images/ocr/moleclues.webp)

Chemical diagrams

![](images/ocr/note.webp)

Handwritten notes

![](images/ocr/curl-api.png)

Code snippets

You can find more example requests and types of images that you can process with Convert API in the User Guide.

[View examples](/docs/convert/examples)

## Use cases for Convert API

### Solving and Search Apps

With a long tail of advanced math, handwriting, and foreign language features, Convert API is the #1 choice for solving, tutoring, and search apps like Mathway, Doubtnut, and Toppr.

### Grading and Assessment Platforms

Grading and assessment platforms like Gradescope use Convert API in their platforms to make it faster and easier for professors to distribute and grade homework and exams with AI.

### Publishing, Accessibility and LMS

Publishing companies use Convert API to create digital STEM educational material like online math textbooks. Accessible education companies like Benetech use Mathpix to make math and science educational materials accessible to all students.

### Bulk digitization (on‑prem available)

Our APIs are useful for bulk digitization of images or PDFs. We also offer an [on-premise solution](/on-prem-pdf-cloud) for bulk PDF processing for companies like London Stock Exchange, who need to
[securely](/secure-conversion) process documents in their private cloud.

## Ready to get started?

Pay As You Go plans require a credit or debit card payment on file. ACH and bank transfers, POs, and other Enterprise payment options available on request. See our [pricing page](/pricing/api)
for details.