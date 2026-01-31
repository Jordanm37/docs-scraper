---
title:  Convert API User Guide: All API endpoints
url: https://mathpix.com/docs/convert/endpoints
---

i

* [Docs](/docs)  >
* [Convert API](/docs/convert/overview)  >
* [Endpoints](endpoints)

* [v3/text](#v3%2Ftext)
* [v3/pdf](#v3%2Fpdf)
* [v3/strokes](#v3%2Fstrokes)
* [v3/batch](#v3%2Fbatch)
* [v3/latex](#v3%2Flatex)
* [v3/ocr-results](#v3%2Focr-results)
* [v3/pdf-results](#v3%2Fpdf-results)

# v3/text

You can use this endpoint to OCR individual images of handwritten and printed equations, handwritten and printed text, tables, and diagrams to get digital formats like LaTeX, Asciimath, and MathML. You can also request additional information about the data in the image like which alphabets were detected (we support [most foreign languages](/language-support)), line data, word data, and confidence.

This is also the endpoint you want to process images of diagrams like [geometry](https://docs.mathpix.com/#geometry-objects) and chemistry. At this time we only support triangles for geometry, which are represented via vertices, edges, and labels.

[Go to v3/text developer docs](https://docs.mathpix.com/#process-an-image)

# v3/pdf

Use this endpoint to OCR PDFs and convert them to Markdown, LaTeX, and DOCX. This endpoint works asynchronously, since large PDF files can take several minutes to process. This endpoint accepts PDF files and URLs in the request.

Since requests are asynchronous, you can check the [processing status](https://docs.mathpix.com/#processing-status) of a PDF using the PDF ID returned by the API. Once the PDF has been processed, you can convert it to your desired format. The PDF endpoint can also return line-by-line data, which can be useful for building novel experiences on top of original PDFs. A separate PDF results endpoint ([v3/pdf-results](https://docs.mathpix.com/#query-pdf-results)) can be used to query information about a certain PDF, or all your PDFs.

[Go to v3/pdf developer docs](https://docs.mathpix.com/#process-a-pdf)

# v3/strokes

Use this endpoint to add stroke recognition (i.e. digital ink) to your app. This endpoint works for all math, and for Hindi and Latin alphabet language text. You can process the data for each individual stroke, or you can use a `session_id` for live drawing capabilities in your app (this is also the more cost-effective option).

[Go to v3/strokes developer docs](https://docs.mathpix.com/#process-stroke-data)

# v3/batch

Use this endpoint to process a multiple images in a single POST request. The request will return a batch ID which be queried with a GET request once an appropriate amount of time has passed for the images to process. You should only use the batch endpoint if your workflow is not latency sensitive (for example, you are digitizing a textbook and need to process all images of equations). Please note that batch requests are priced per image in the batch, not per request.

[Go to v3/batch developer docs](https://docs.mathpix.com/#process-a-batch)

# v3/latex

This is our legacy endpoint for converting images to LaTeX, that was developed before we added support for regular text. The intent of the endpoint was to parse out the math in an image, while ignoring text, so this endpoint should only be used for images that only have individual equations and no text that needs to be processed.

[Go to v3/latex developer docs](https://docs.mathpix.com/#process-an-equation-image)

# v3/ocr-results

Use this endpoint to search your results from POST requests to v3/text, v3/strokes, and v3/latex with a GET request on `/v3/ocr-results?search-parameters`.

[Go to v3/ocr-results developer docs](https://docs.mathpix.com/#query-image-results)

# v3/pdf-results

Use this endpoint to search your results from POST requests to v3/pdf with a GET request on `/v3/pdf-results?search-parameters`. The search request must contain a valid app\_key header to identify the group owning the results to search.

[Go to v3/pdf-results developer docs](https://docs.mathpix.com/#query-pdf-results)

[<   Best Practices](/docs/convert/best-practices)

[Rate and page limits   >](/docs/convert/limits)