---
title:  Error Handling and Debugging
url: https://mathpix.com/docs/mpxpy/errors
---

i

* [Docs](/docs)  >
* [Python SDK](/docs/mpxpy/overview)  >
* [Error Handling and Debugging](errors)

* [Error Handling and Debugging](#error-handling-and-debugging)
  + [Common Error Types](#common-error-types)
  + [Debugging Tips](#debugging-tips)
  + [Example Error Handling](#example-error-handling)

# Error Handling and Debugging

The Mathpix Python SDK raises informative errors to help you quickly identify problems with authentication, file inputs, or API usage.

## Common Error Types

* **AuthenticationError:**  
  Raised when your credentials are missing or invalid.  
  Make sure your `app_id` and `app_key` are correctly configured in environment variables or passed to the client.
* **ValidationError:**  
  Raised when input parameters are missing, conflicting, or improperly formatted.  
  For example, calling `image_new()` without either `file_path` or `url`.
* **FilesystemError:**  
  Triggered if there’s an issue accessing the file system, such as writing to a nonexistent folder.
* **ConversionIncompleteError:**  
  Raised when you attempt to retrieve output before the conversion is fully finished.
* **MathpixClientError:**  
  A general error class for unexpected issues with the SDK or network.

## Debugging Tips

* Enable logging in your app to track request/response activity.
* Check all error messages for helpful context and validation clues.
* Ensure file paths and URLs are valid and accessible.
* Double-check that you’re using the correct SDK method for the content you’re processing.
* Review rate limits in your Mathpix Console if requests are being throttled.

## Example Error Handling

```
from mpxpy.mathpix_client import MathpixClient
from mpxpy.errors import MathpixClientError, ConversionIncompleteError

client = MathpixClient(app_id="your-app-id", app_key="your-app-key")

try:
    pdf = client.pdf_new(file_path="example.pdf", convert_to_docx=True)
    pdf.wait_until_complete()
    result_path = pdf.to_docx_file("output/example.docx")
except ConversionIncompleteError:
    print("Conversion is not yet complete. Try again later.")
except MathpixClientError as e:
    print(f"Mathpix error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

Catch specific exceptions like `AuthenticationError` or `ValidationError` if you need to handle different failure types differently.

[<   Available Output Formats](/docs/mpxpy/formats)

[Mathpix Python SDK on GitHub   >](/docs/mpxpy/github)