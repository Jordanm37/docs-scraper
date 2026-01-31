---
title:  Convert API User Guide: API Best Practices
url: https://mathpix.com/docs/convert/best-practices
---

i

* [Docs](/docs)  >
* [Convert API](/docs/convert/overview)  >
* [Best Practices](best-practices)

* [Minimizing latency](#minimizing-latency)
* [Server locations](#server-locations)
* [Authorization](#authorization)
* [Running “batch” / indexing jobs](#running-%E2%80%9Cbatch%E2%80%9D-%2F-indexing-jobs)
* [v3/text vs. v3/latex](#v3%2Ftext-vs.-v3%2Flatex)
* [Supported image file types](#supported-image-file-types)

# Minimizing latency

The biggest source of latency is image uploads. The speed of a response from Mathpix API servers is roughly proportional to the size of the image. Try to use images under 100KB for maximum speeds. JPEG compression and image downsizing are recommended to ensure lowest possible latencies. For minimal latencies, we also recommend using form uploads with a file and a `options_json` form field instead of using base64 JSON encoding for image data (both options for sending an image are described in <https://docs.mathpix.com/#process-an-image>). We also recommend using an easy-to-use cropping UI for end users to crop images, so that the minimal amount of image data is send to the API.

# Server locations

We currently offer servers in the following AWS regions:

* US East 1 (N. Virginia)
* EU Central 1 (Frankfurt)
* SE Asia (Singapore)

To optimize latency, we recommend having servers in those regions and using latency based routing.

If you are located in the EU and need to ensure that all data is processed within the EU, you can send requests directly to our EU specific URL `https://eu-central-1.api.mathpix.com/` to guarantee processing in Europe.

# Authorization

Convert API currently offers API key authorization through a customer’s proxy server or the use of client-side app tokens.

We have always discouraged customers from putting API keys inside client-side apps, due to the risk of API key theft (note: customers are responsible for any usage made with a stolen API key). With app tokens, you can safely grant access to Convert API services inside client apps, with a temporary access token that expires in five minutes (this is the default, the expiration is configurable). This way, you can keep your API key safe in your private cloud, and expose a single authenticated endpoint to your customers so that they can request and receive Mathpix app tokens.

This is convenient for taking advantage of our latency-routed global network of servers without needing to maintain proxy servers that are themselves also distributed globally. This also means that requests are faster because there is one less hop required to reach Convert API servers.

**Example configuration 1: [Proxy server](https://docs.mathpix.com/#using-server-side-api-keys)**

In the below diagram, the customer operates latency routed servers in each region to authorize requests and take advantage of Mathpix global network of servers. All app requests, including ones containing digital ink or image data, are proxied through customer operated servers.

![diagram](/images/diagram1.webp)

**Example configuration 2: [App tokens](https://docs.mathpix.com/#using-client-side-app-tokens)**

Now we show the same setup using app tokens. The customer operated server is only needed to fetch app tokens and does not need to proxy requests containing digital ink or image data. Customer API keys are only used to fetch app tokens. Apps can call Mathpix endpoints directly without having to go through an auth proxy.

![diagram](/images/diagram2.webp)

# Running “batch” / indexing jobs

For such use cases, we recommend using our v3/text endpoint with the “async” flag as well as leveraging the “tags” field (<https://docs.mathpix.com/#request-parameters>). You can then query results later using our v3/ocr-results endpoints (<https://docs.mathpix.com/#query-image-results>) and specifying the same “tags” you used to call the v3/text endpoint. This is the new way we are enabling batch use cases. This method conveniently doesn’t require the API client to pre-batch requests, and it also leverages the v3/text codepath, while the older v3/batch endpoint can only leverage the v3/latex codepath.

# v3/text vs. v3/latex

Our first endpoints v3/latex and v3/batch were based on image to LaTeX conversion, where the intent was to parse out the math in an image, while ignoring text.

In order to provide better functionality for full text recognition, we build the v3/text endpoint, while keeping the v3/latex interface identical for backward compatibility. New customers should use v3/text endpoint as it has more features and is more robust.

# Supported image file types

Mathpix supports image types compatible with OpenCV, including:

JPEG files - \_.jpeg, \_.jpg, \*.jpe  
Portable Network Graphics - \*.png  
Windows bitmaps - \_.bmp, \_.dib  
JPEG 2000 files - \*.jp2  
WebP - \*.webp  
Portable image format - \_.pbm, \_.pgm, \_.ppm \_.pxm, \*.pnm  
PFM files - \*.pfm  
Sun rasters - \_.sr, \_.ras  
TIFF files - \_.tiff, \_.tif  
OpenEXR Image files - \*.exr  
Radiance HDR - \_.hdr, \_.pic  
Raster and Vector geospatial data supported by GDAL

[<   Creating an API key](/docs/convert/creating-an-api-key)

[Endpoints   >](/docs/convert/endpoints)