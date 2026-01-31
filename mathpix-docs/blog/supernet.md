---
title: Update for image and PDF API: new layout model, document tree outputs, parse text inside charts and diagrams
url: https://mathpix.com/blog/supernet
---

# Update for image and PDF API: new layout model, document tree outputs, parse text inside charts and diagrams

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fsupernet)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsupernet)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsupernet&title=Update for image and PDF API: new layout model, document tree outputs, parse text inside charts and diagrams)

## Model update

We have released our latest layout parsing model, **SuperNet**. This model is larger and more capable than its predecessors. It combines several of our special purpose models (e.g., table layout parser, PDF page parser) into one larger model. The new approach improves accuracy and will enable us to ship improvements more rapidly moving forward.

Among the many improvements:

* New capability to parse text fragments from diagrams (see below for more details)
* Improved PDF parsing for distorted and imperfect scans
* Improved general table parsing accuracy
* Improved code/pseudocode recognition
* Improved handling of rotated images and rotated PDF pages
* Improved recognition of +/-90 degrees rotated table cells
* Basic support for recognition of diagonally split table cells

Note that we have tested this model extensively on our internal benchmarks: this is our most well-tested model update yet.

## Document tree information in line-by-line outputs

We have added new fields to our line-by-line data outputs in order to provide a detailed document tree output for each page.

In particular, we have added `id`, `parent_id`, and `children_ids` to the line-by-line outputs for PDFs and images. This is critical for diagram text extraction (see below), as we want to be able to associate text fragments with their parent containers. Diagrams can themselves have diagrams as children.

For API clients to be able to differentiate between “search only” text and normal “conversion” text, we have added a new `conversion_output` boolean field to each line, which is false whenever the line is not directly included in the converted Markdown / DOCX / HTML / LaTeX outputs. Diagrams are still included as images in outputs and have `conversion_output=true`, but the text inside of them, which will have `conversion_output=false`, can now be parsed if you specify `"include_diagram_text": true` in the request options.

For tables, the parent table has `conversion_output=true` but the children cells (if available) have `conversion_output=false`. The cells themselves may have children (e.g., diagrams, text lines), and so on.

For a more detailed breakdown of the updates to the line by line data, see [our changelog](https://mathpix.com/docs/convert/changelog). The updates to the API, including new returned fields and a full breakdown of line types, are documented at [Mathpix Docs](https://docs.mathpix.com).

## Parse text inside charts and diagrams

To parse text fragments inside charts and diagrams, use `"include_diagram_text": true` in your request options. Note that for the image API (v3/text), you need to specify `"include_line_data": true` to get the lines data.  
For example, this image:

![Example diagram](/images/blog/diagram-supernet.png)

will get parsed as:

![Example diagram, parsed](/images/blog/parsed-diagram-supernet.png)

with lines outputs that looks like this (fields and the full list were omitted for brevity):

```
[
  {
    "type": "text",
    "conversion_output": true,
    "id": "b36ee632ed9f40a98be59f58876fc2c1",
    "text": "Figure 16.2.1. Current architecture for Lustre",
  },
  {
    "type": "diagram",
    "conversion_output": false,
    "id": "5ffc764d50ea4108a034d2842413b293",
    "children_ids": [
      "dfa08e22c9f34dbe864833b4b95685b8",
      "ef84af0a9e9642f5a8c49b4d566118a1",
      "b3f4a8cff5eb46e5af0b438bf348548d",
      "cb4e078fd4ab4e69a1ac754d96b9f7e2",
      "b217826830094fdcab48c657ccc48a87",
      "61558bb3f115410ba9fd192f78046cef",
      "2f769041cd7d4850a1f51b9590b6af08"
    ],
    "error_id": "image_not_supported"
  },
  {
    "type": "chart_info",
    "conversion_output": false,
    "id": "dfa08e22c9f34dbe864833b4b95685b8",
    "parent_id": "5ffc764d50ea4108a034d2842413b293",
    "children_ids": [
      "8d68793a3e6e4fcd951a98da1569e787",
      "2d7c06b837ea46a191c6b808c0fa3bba"
    ],
    "text": "Lustre Lite filesystem"
  },
  {
    "type": "text",
    "conversion_output": false,
    "id": "8d68793a3e6e4fcd951a98da1569e787",
    "parent_id": "dfa08e22c9f34dbe864833b4b95685b8",
    "text": "Lustre Lite"
  },
  {
    "type": "text",
     "conversion_output": false,
    "id": "2d7c06b837ea46a191c6b808c0fa3bba",
    "parent_id": "dfa08e22c9f34dbe864833b4b95685b8",
    "text": " filesystem",
  },
  ...
]
```

## Additional considerations

* We are deprecating the triangle shape associated with `"include_geometry_data"`; diagram label outputs are unchanged
* There is a chance of increased latency for very large tables due to the improved algorithm being more compute-intensive
* Table content is now left-aligned by default for improved readability