---
title: New HTML, MMD, and MD ZIP export formats
url: https://mathpix.com/blog/new-zips
---

# New HTML, MMD, and MD ZIP export formats

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fnew-zips)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fnew-zips)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fnew-zips&title=New HTML, MMD, and MD ZIP export formats)

We’ve added new packaged outputs for the [v3/converter](https://docs.mathpix.com/#convert-documents) and [v3/pdf](https://docs.mathpix.com/#process-a-pdf) API endpoints. The html.zip, md.zip, and mmd.zip archives bundle the main file plus all images for easy distribution, organization, and offline use.

**Unzipped layout:**

```
output_folder/
├─ pdf_id.html
└─ images/
   ├─ example-image-1.jpg
   └─ example-image-2.jpg
```

**How images are referenced:**

* HTML:

`<img src="./images/2025_09_05_681ef77eff7a26c87a61g-01.jpg" alt="">`

* MD/MMD:

`![](./images/2025_09_05_681ef77eff7a26c87a61g-01.jpg)`

These formats are available directly through the [API](https://docs.mathpix.com/#conversion-results) or via [mpxpy](https://github.com/Mathpix/mpxpy), our Python SDK:

```
from mpxpy.mathpix_client import MathpixClient

client = MathpixClient(app_id="YOUR_APP_ID", app_key="YOUR_APP_KEY")

# Export a PDF result
pdf = client.pdf_new(
    file_path="path/to/file.pdf",
    convert_to_md_zip=True,
    convert_to_mmd_zip=True,
    convert_to_html_zip=True,
)
pdf.wait_until_complete()
md_zip_path = pdf.to_md_zip_file(path="output/sample.md.zip")
mmd_zip_path = pdf.to_mmd_zip_file(path="output/sample.mmd.zip")
html_zip_path = pdf.to_html_zip_file(path="output/sample.html.zip")

# Or a Mathpix Markdown conversion
conversion = client.conversion_new(
    mmd='Example MMD with <img src="https://example-image.png"/>',
    convert_to_md_zip=True,
    convert_to_mmd_zip=True,
    convert_to_html_zip=True,
)
conversion.wait_until_complete()
md_zip_path = conversion.to_md_zip_file(path="output/converted.md.zip")
mmd_zip_path = conversion.to_mmd_zip_file(path="output/converted.mmd.zip")
html_zip_path = conversion.to_html_zip_file(path="output/converted.html.zip")
```