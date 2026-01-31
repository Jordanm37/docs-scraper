---
title: Mathpix Convert API Pricing
url: https://mathpix.com/pricing/api
---

# Convert API Pricing

Enterprise-grade document conversion API with unmatched accuracy and flexibility. Scale your applications with 150+ customizable parameters and industry-leading recognition technology.

## Estimate your pricing

×

Image usage

PDF usage

Stroke usage

### Estimated monthly cost

$0/month

[Get started](https://console.mathpix.com/orgs)

For developers

#### Pay as you go

Pay monthly based on usage

Usage-based  
  
$19.99 one-time setup fee  
Estimate your pricing

[Get Started](https://console.mathpix.com/orgs)

What's included:

* $29 credit applied for testing our endpoints
* Pay only what you use
* Visualization dashboard
* Billing on 1st of each month for the previous month's usage

For enterprises

#### Enterprise

Special pricing for long-term contracts

Contact us  
  
High volume? Save with preferred custom pricing

[Get a quote](/contact-us)

What's included:

* 24/7 priority support
* Custom recognition features
* Customized privacy and security

## Pay as you go pricing details

  

Convert API endpoint pricing - detailed cost calculations and rate conversions.

*Usage tiers are per month*

Service

Price

Setup fee

$19.99 (one-time fee)

**Image**

Process image (v3/text)\*   
Process strokes (without live updates) (v3/strokes)  
Process equation image (v3/latex)\*  
Process batch (v3/batch)\*  
  
\*Note that each image with more than 12 rows of text shall count as one PDF page and will be priced at the PDF pricing rate.

0-1M images

$0.002 per image

1M+ images

$0.0015 per image

**PDF**

v3/pdf

0-1M pages

$0.005 per page

1M+ pages

$0.0035 per page

**Strokes**

v3/strokes with live updates

0-1K

$0.00 per session

1K-100K

$0.01 per session

100K-1M

$0.008 per session

1M+

$0.005 per session

#### Frequently Asked Questions

How do I get an API key?

To obtain an API key for the Mathpix Convert API, please follow these steps after signing up:

1. Create a Convert Organization:

   * Log in to your Mathpix account.
   * Navigate to the Convert Organizations Page.
   * Click on **Create organization** at the top right corner of the screen.
2. Set Up Billing Information:

   * You will be prompted to add a credit or debit card to activate your API key.
   * A one-time, non-refundable setup fee is required to enable your API keys.
3. Access Your API Key:

   * Once your Convert organization is created and billing information is added, your API key will be displayed on your dashboard.
   * If you need additional API keys, you can create them by clicking **Create Key**.

  

For detailed instructions, please refer to the [Creating an API Key](https://mathpix.com/docs/convert/creating-an-api-key) section in our documentation.

If you encounter any issues during this process, feel free to contact us at [support@mathpix.com](mailto:support@mathpix.com).

What happens to our end-user’s images when using the Convert API in our product?

When your product sends images to the Mathpix Convert API, the following occurs:

* **Processing:** The images are processed to extract the desired information, such as text, mathematical expressions, or chemical diagrams.
* **Temporary Storage:** To ensure service quality and allow for quality assurance, images and their associated data are temporarily stored.
* **Retention Period:** By default, these images are retained for up to 30 days. However, you have the option to opt out of data retention for quality assurance purposes. If you choose to opt out, images are deleted within 24 hours after processing.

  

Mathpix is committed to maintaining the confidentiality and security of your data. We do not use your end-users' images for any purpose other than providing the requested service and improving our recognition engine, if permitted. For more detailed information, please refer to our [Privacy Policy.](/privacy)

If you have specific data handling requirements or need further assurances, please contact us at support@mathpix.com.

What if we want Mathpix to delete all images processed from our API key immediately?

If you want Mathpix to delete all images processed from your API key immediately after processing, you can enable **Data Retention Opt-Out** in your Convert API settings. With this option:

* **No Data Retention:** Images and associated processing results are deleted within 24 hours and are never saved to disk at any point.
* **Immediate Deletion Option:** If you require immediate deletion, contact support@mathpix.com to discuss custom configurations or specific data handling needs.

  

For more details on this feature and other privacy controls, refer to the [Convert API Privacy FAQ.](/docs/convert/privacy)

What is the OCR billing cycle for Pay as you Go users?

For Pay as you Go (PAYG) users, the billing cycle is as follows:

* You are billed on the **1st of each month** for the previous month's usage.
* The invoice includes the total number of Snips and PDFs processed during the previous month

  

For more details refer to the [Convert API Billing FAQ.](/docs/convert/billing)

I would like to try the Convert API before buying. Can I have a free trial?

While we don’t offer a free trial for the Convert API, you can try Mathpix’s capabilities using our [Snip app](/snip), which has a free plan. The Snip app and the Convert API offer exactly the same conversion features, so you can fully test Mathpix’s capabilities before using the API.

The Snip app is available for desktop and mobile, and it’s a great way to explore Mathpix before committing to the Convert API. If you’re interested in testing the API itself or need assistance, feel free to contact us at [support@mathpix.com](mailto:support@mathpix.com).

I am worried that if I make a mistake and send tons of requests, I could accidentally end up paying a lot of money. Is there a mechanism in place where the system would reject my requests instead of charging me?

Yes, there are several safeguards in place to help prevent unexpected high charges:

1. **Rate Limits:** The API key has default rate limits to ensure requests don’t spike unexpectedly. If the limit is exceeded, additional requests will be rejected.
2. **Monthly Limits for PDFs:** There is a total monthly limit on the number of PDF pages that can be processed per API key. Once this limit is reached, further requests will be blocked for that month.
3. **Usage Monitoring:** You can track your usage in real time via your Mathpix dashboard, so it’s easy to keep an eye on consumption and spot anything unusual.
4. **Billing Notifications:** We send email reminders when your usage approaches certain thresholds to keep you informed and help prevent accidental overuse.
5. **Custom Controls:** If needed, you can request custom rate or usage limits to better align with your requirements.

I need to process a high volume of images. How can I increase my monthly image limit?

If you need to process more images than your current limits allow, here’s what you can do:

1. Increase Limits on Your Dashboard:

   * Log in to [console.mathpix.com](https://console.mathpix.com).
   * Navigate to the **Requests** tab under your organization.
   * You can adjust the **rate limits and monthly page** limits directly from the dashboard to better match your processing needs.
2. Contact Support for Higher Limits:

   * If your required limits exceed what’s adjustable on the dashboard, contact us at support@mathpix.com.
   * We can work with you to create a custom plan tailored to your specific needs.

I have a large volume of documents and don’t need them converted in real time. Do you have another service that can handle this?

Yes, we offer [Secure Conversion Services (SCS)](/secure-conversion) for batch processing large volumes of documents. This service is designed for organizations that don’t require real-time processing and prioritize secure, efficient, and scalable conversion.

Key features of Secure Conversion Services include:

1. Increase Limits on Your Dashboard:

   * **Asynchronous Processing:** Upload your documents in bulk, and we’ll process them in the background.
   * **Data Security:** Built with strict privacy and security measures to handle sensitive data.
   * **Custom Integration:** Tailored to meet your workflow requirements.