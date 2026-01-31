---
title:  Convert API User Guide: Privacy FAQ
url: https://mathpix.com/docs/convert/privacy
---

i

* [Docs](/docs)  >
* [Convert API](/docs/convert/overview)  >
* [Privacy](privacy)

* [Privacy FAQ](#privacy-faq)
  + [What happens to our end-user’s images when using Convert API in our product?](#what-happens-to-our-end-user%E2%80%99s-images-when-using-convert-api-in-our-product%3F)
  + [What if we want Mathpix to delete all images processed from our API key immediately?](#what-if-we-want-mathpix-to-delete-all-images-processed-from-our-api-key-immediately%3F)
  + [Does Mathpix collect any information about my end-user?](#does-mathpix-collect-any-information-about-my-end-user%3F)
    - [What does Mathpix do to keep images safe?](#what-does-mathpix-do-to-keep-images-safe%3F)
    - [How can I request access to the data Mathpix has from my API key?](#how-can-i-request-access-to-the-data-mathpix-has-from-my-api-key%3F)

# Privacy FAQ

Thank you for trusting Mathpix with your images! We take this responsibility very seriously. Below you can find easy to understand answers to common questions we get about our privacy policy and how we handle your (or your end-user’s) images and data.

You can also read the full [Mathpix Privacy Policy](https://mathpix.com/privacy).

---

### What happens to our end-user’s images when using Convert API in our product?

When using Convert API to process images of math and text, each image or batch of images is sent to our servers where we either return a valid response or an error message if we cannot process the image for any reason. (More information on API request options, formats, and errors can be found on our [Docs](https://docs.mathpix.com)).

Unless a customer has [specifically requested that all images sent from their API key be deleted from our database immediately](https://docs.mathpix.com/#privacy) after processing, once the image has been processed the image is then sent to our internal Quality Assurance (QA) database. These images can be accessed by our QA team, in order to assure that our service is working as intended and for finding any bugs in our recognition engine.

Any images with personally identifying information are deleted from the QA database within 24 hours. All images are deleted from the QA database after 90 days.

### What if we want Mathpix to delete all images processed from our API key immediately?

To [indicate](https://docs.mathpix.com/#privacy) to Mathpix that you never want us to save any images to disk, simply include the `improve_mathpix` flag in your request, set to `false`. Please note that querying [v3/ocr-results](https://docs.mathpix.com/#query-image-results) will only work for requests where `improve_mathpix` is set to `true`.

## Does Mathpix collect any information about my end-user?

Mathpix collects IP addresses of end-users to protect us in the case of spamming of our servers. Not collecting end-user IP addresses is an available option, but please note that if spamming is coming from your API key and we do not have IP information to locate the source, we will be forced to suspend your API key until the issue has been resolved.

### What does Mathpix do to keep images safe?

We take our data management extremely seriously, and we have taken many measures to ensure that all data is managed in a way that protects your privacy. We only require the minimum amount of personal information that is necessary to fulfill the purpose of your use of Convert API in your product.

Mathpix uses third party vendors and hosting partners for the necessary hardware, software, networking, storage, and related technology required to provide our services. Although Mathpix owns the code, databases, and all rights to the API code, you retain all rights to any data sent from your API key.

In order to provide the best quality of service, we must monitor the images being processed by the app. Any image reviewed by our QA team has already been completely anonymized from your end-user. Only those responsible for monitoring server health have access to end-user IP addresses. All images are deleted from our QA database after being reviewed by our QA team (within 90 days).

Please note that our policies and practices are subject to change–we are always trying to improve how we handle the data we process. Any changes to our policies will be reflected on our website in our [Privacy Policy](https://mathpix.com/privacy), [Terms and Conditions](https://mathpix.com/terms) or in this FAQ.

### How can I request access to the data Mathpix has from my API key?

You have access to all the API request and reponse data from your API keys under the **Results** tab of your [Convert Organization page](https://console.mathpix.com/orgs):

![Results tab](/images/results-tab.webp)

[<   Examples](/docs/convert/examples)

[Use Cases   >](/docs/convert/usecases)