---
title:  Authentication and Environment
url: https://mathpix.com/docs/mpxpy/auth
---

i

* [Docs](/docs)  >
* [Python SDK](/docs/mpxpy/overview)  >
* [Authentication and Environment](auth)

* [Authentication and Environment](#authentication-and-environment)
  + [Authentication Priority](#authentication-priority)
  + [Using a Config File (`~/.mpx/config`)](#using-a-config-file-(~%2F.mpx%2Fconfig))
  + [Using `.env` or `local.env`](#using-.env-or-local.env)
  + [Passing Credentials Directly](#passing-credentials-directly)
  + [Default API Endpoint](#default-api-endpoint)

# Authentication and Environment

This section explains how to authenticate the Mathpix Python SDK client and configure environment variables securely.

To use the SDK, you'll need your Mathpix API `app_id` and `app_key`. You can get them from the [Mathpix Console](https://console.mathpix.com/).

## Authentication Priority

The `MathpixClient` will prioritize auth configs in the following order:

1. Arguments passed directly to the client.
2. A local config file at `~/.mpx/config`.
3. Environment variables located in `.env`
4. Environment variables located in `local.env`

## Using a Config File (`~/.mpx/config`)

Create the file `~/.mpx/config` with the following content:

```
MATHPIX_APP_ID=your-app-id
MATHPIX_APP_KEY=your-app-key
MATHPIX_URL=https://api.mathpix.com  # optional, defaults to this value
```

This file will be automatically detected and loaded by the SDK.

## Using `.env` or `local.env`

You can also define credentials in `.env` or `local.env` files in your project directory:

```
MATHPIX_APP_ID=your-app-id
MATHPIX_APP_KEY=your-app-key
MATHPIX_URL=https://api.mathpix.com  # optional
```

## Passing Credentials Directly

You can also pass credentials directly when initializing the `MathpixClient`:

```
from mpxpy.mathpix_client import MathpixClient

client = MathpixClient(
    app_id="your-app-id",
    app_key="your-app-key",
    api_url="https://api.mathpix.com"  # optional
)
```

Credentials passed directly will override any environment or config-based values.

## Default API Endpoint

The default API endpoint is `https://api.mathpix.com.`  
You can override this endpoint if needed by setting `MATHPIX_URL` in the environment variables or passing it to the client:

```
 client = MathpixClient(
    app_id="your-app-id",
    app_key="your-app-key",
    api_base_url="https://custom-api.mathpix.com"
)
```

[<   Getting Started](/docs/mpxpy/getting-started)

[Processing Images   >](/docs/mpxpy/images)