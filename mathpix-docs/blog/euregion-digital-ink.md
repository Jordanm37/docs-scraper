---
title: Mathpix OCR Update: EU Region, Client Side Tokens, APIs For Digital Ink With Live Updates, New PDF Features
url: https://mathpix.com/blog/euregion-digital-ink
---

# Mathpix OCR Update: EU Region, Client Side Tokens, APIs For Digital Ink With Live Updates, New PDF Features

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Feuregion-digital-ink)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Feuregion-digital-ink)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Feuregion-digital-ink&title=Mathpix OCR Update: EU Region, Client Side Tokens, APIs For Digital Ink With Live Updates, New PDF Features)

# EU region

In order to provide lower latencies to users in Europe, we are now serving traffic in the EU region directly from AWS servers in Frankfurt, Germany (eu-central-1). This brings our total number of regions to 3, the others being N. Virginia (us-east-1) and Singapore (ap-southeast-1).

More regions means lower latencies (requests don’t need to travel as far) and also means more redundancy and increased availability globally. Requests are automatically routed to the region that provides the lowest latency.

This region is also convenient for customers who are required by law to process data inside the EU. Such customers can use our EU specific URL `https://eu-central-1.api.mathpix.com/` to guarantee processing in Europe.

# Client side tokens

You can now use [app-tokens](https://docs.mathpix.com/#using-client-side-app-tokens) for authenticating requests inside client side app code. We have always discouraged customers from putting API keys inside client side apps, due to the risk of API key theft. With app tokens, you can safely grant access to Mathpix OCR services inside client apps, with a temporary access token that expires in five minutes (this is the default, the expiration is configurable). This way, you can keep your API key safe in your private cloud, and expose a single authenticated endpoint to your customers so that they can request and receive Mathpix app tokens.

This is convenient for taking advantage of our latency-routed global network of servers without needing to maintain proxy servers that are themselves also distributed globally. This also means that requests are faster because there is one less hop required to reach Mathpix OCR servers.

We now show an example of how this can simplify server set ups.

In the below diagram, the customer operates latency routed servers in each region to authorize requests and take advantage of Mathpix global network of servers. All app requests, including ones containing digital ink or image data, are proxied through customer operated servers.

![](/images/diagram1.webp)

Now we show the same setup using app tokens. The customer operated server is only needed to fetch app tokens and does not need to proxy requests containing digital ink or image data. Customer API keys are only used to fetch app tokens. Apps can call Mathpix endpoints directly without having to go through an auth proxy.

![](/images/diagram2.webp)

# Digital ink

A big motivation for supporting client side app tokens was to provide a convenient package for customers who want to process digital ink, without having to pipe data through their own servers to authorize the requests. The [app-tokens](https://docs.mathpix.com/#using-client-side-app-tokens) route provides a `include_strokes_session_id` flag, which when true, returns a `strokes_session_id` string that can be used inside calls to [v3/strokes](https://docs.mathpix.com/#process-stroke-data).

Requests with `strokes_session_id` must be authorized with app tokens headers.

The purpose of `strokes_session_id` is to provide a better experience for customers who want to provide equation drawing experiences that include live updates. Calls to v3/strokes that include `strokes_session_id` are priced per drawing session (1 equation) and are not priced per live update.

In short, using `strokes_session_id` is more expensive than one request to v3/strokes (with no intermediate results) but less expensive than calling v3/strokes many times for the same equation to show the live updates (intermediate results).

The [new pricing](https://mathpix.com/convert#pricing) for the v3/strokes endpoint is:

* 0/session (0-1K sessions)
* $0.01/session (1-100K sessions)
* $0.008/session (100K-1000K sessions)
* $0.005/session (1000K+ sessions)

A demo of the new digital ink functionality:

We will be providing sample code shortly for the above demo. This sample demo will contain common digital ink usage patterns, including scratching to remove symbols.

# New PDF features

* Algorithm improvements
* Basic support for handwritten PDFs