---
title:  Convert API User Guide: Billing
url: https://mathpix.com/docs/convert/billing
---

i

* [Docs](/docs)  >
* [Convert API](/docs/convert/overview)  >
* [Billing](billing)

* [Introduction](#introduction)
* [Accepted Payment Methods](#accepted-payment-methods)
* [Convert API Plans](#convert-api-plans)
  + [Monthly Pay As You Go](#monthly-pay-as-you-go)
    - [Pricing examples](#pricing-examples)
  + [Enterprise](#enterprise)
  + [Yearly License On-Prem](#yearly-license-on-prem)
* [Updating billing information](#updating-billing-information)
* [Invoicing](#invoicing)
* [FAQ](#faq)
  + [What is the OCR billing cycle for Pay as you Go users?](#what-is-the-ocr-billing-cycle-for-pay-as-you-go-users%3F)
  + [I would like to try Convert API before buying. Can I have a free trial?](#i-would-like-to-try-convert-api-before-buying.-can-i-have-a-free-trial%3F)
  + [I am worried that if I make a mistake and send off tons of requests, I could accidentally end up paying a lot of money. Is there a mechanism in place where the system would reject my requests instead of charging me?](#i-am-worried-that-if-i-make-a-mistake-and-send-off-tons-of-requests%2C-i-could-accidentally-end-up-paying-a-lot-of-money.-is-there-a-mechanism-in-place-where-the-system-would-reject-my-requests-instead-of-charging-me%3F)
  + [I need to process a huge amount of images. How can I increase my monthly image limit?](#i-need-to-process-a-huge-amount-of-images.-how-can-i-increase-my-monthly-image-limit%3F)

# Introduction

In this FAQ we will answer the most common questions we get about payments and billing for Convert API organizations. Can’t find the answer to your question here? Email us anytime at [support@mathpix.com](mailto:support@mathpix.com) and we would be happy to help you!

# Accepted Payment Methods

**Google Pay, Apple Pay, credit or debit card.**

Pay As You Go plan requires a credit or debit card payment on file, which will be charged at the beginning of the month for the usage made in the previous month.

ACH and bank transfers, POs, and other Enterprise payment options available on request. Please [contact Sales](https://mathpix.com/contact-us).

# Convert API Plans

### Monthly Pay As You Go

* $19.99 one-time setup fee
* $29 is applied to your account for testing any of our endpoints
* Visualization Dashboard
* Pay only for what you use
* Billing on 1st of each month for the previous month’s API usage

We price differently based on which [endpoints](/docs/convert/endpoints) are used. Usage tiers serve as a volume discount.

1. Process image (v3/text)\*  
   Process strokes (without live updates)(v3/strokes)  
   Process equation image (v3/latex)\*  
   Process batch (v3/batch)\*  
   Get results (v3/ocr-results)

   * $0.002/request (0-1M images)
   * $0.0015/request (1M+ images)

*Note:* each image with more than 12 rows of text shall count as one PDF page and will be priced at the PDF pricing rate.

2. Process PDF (v3/pdf)

   * $0.005/page (0-1M pages)
   * $0.0035/page (1M+ pages)
3. Digital ink with live updates included (v3/strokes using stroke session ID)

   * $0/session (0-1K sessions)
   * $0.01/session (1K-100K sessions)
   * $0.008/session (100K-1M sessions)
   * $0.005/session (1M+ sessions)

#### Pricing examples

**Example of v3/text billing**

Let’s say you have 1.5M requests of *v3/text* per month. The pricing for the first million requests is $0.002/request. The pricing for the next 500K requests is $0.0015/request. In total, you will have to pay:

* 1,000,000 \* $0.002 = $2000
* 500,000 \* $0.0015 = $750
* $2000 + $750 = ***$2750***

**Example of v3/pdf billing**

Let’s say you want to convert 2M pages of *v3/pdf* per month. The pricing for the first million pages is $0.005/page. When you reach a million pages, you pay $0.0035 for every next page. In total, you will have to pay:

* 1,000,000 \* $0.005 = $5000
* 1,000,000 \* $0.0035 = $3500
* $5000 + $3500 = ***$8500***

**Example of v3/strokes billing**

Let’s say you need 2,000,000 sessions of *v3/strokes* per month. The first thousand sessions is free. The pricing for the next 99K sessions is $0.01/session. The pricing for 100K-1M sessions is $0.008/session, and sessions after one million are $0.005. In total, you will have to pay:

* 1000 \* $0 = $0
* 99,000 \* $0.01 = $990
* 900,000 \* $0.008 = $7200
* 1,000,000 \* $0.005 = $5000
* $0 + $990 + $7200 + $5000 = ***$13190***

**Example of mixed billing**

Let’s say you have 3M requests of *v3/text*, 800K pages of *v3/pdf*, and 500K sessions of *v3/strokes* per month. In total, you will have to pay:

* 1,000,000 \* $0.002 = $2000
* 2,000,000 \* $0.0015 = $3000
* $2000 + $3000 = *$5000 for 3M requests of v3/text*

* 800,000 \* $0.005 = *$4000 for 800K pages of v3/pdf*

* 1000 \* $0 = $0
* 99,000 \* $0.01 = $990
* 400,000 \* $0.008 = $3200
* $0 + $990 + $3200 = *$4190 for 500K sessions of v3/strokes*.

Total amount: $5000 + $4000 + $4190 = ***$13190***.

### Enterprise

* Best for large customers
* Pay by invoice
* 24/7 support
* Custom API features
* Discounts for monthly subscriptions
* Discounts for special use cases

### Yearly License On-Prem

* Fully contained AMI
* Unlimited usage
* No access to outside internet needed
* Maintenance included
* Software improvements included
* GCP or Azure available upon request
* Docker image available upon request

# Updating billing information

You can update your billing information by going to [console.mathpix.com](https://console.mathpix.com/) > Your Convert Organization > Billing. Then find the **Payment method** section and click the **Update** button to enter your new credit card details.

![Update billing information](/images/convert-update-payment.webp)

# Invoicing

You can find and download all of your invoices by going to [console.mathpix.com](https://console.mathpix.com) > Your Convert Organization > Billing.

![Download Invoices](/images/convert-billing-invoices.webp)

# FAQ

### What is the OCR billing cycle for Pay as you Go users?

We charge on the 1st of the month for usage done in the previous month.

### I would like to try Convert API before buying. Can I have a free trial?

We don’t give a free trial for Convert API. But you can create an account for a $19.99 one-time non-refundable setup fee and you’ll get $29 applied to your account for testing any of our endpoints.

### I am worried that if I make a mistake and send off tons of requests, I could accidentally end up paying a lot of money. Is there a mechanism in place where the system would reject my requests instead of charging me?

We can offer a lower rate limit, which would limit the number of API requests you can make in a minute. In [accounts.mathpix.com](http://accounts.mathpix.com) you are able to check your usage at any time and make sure that too many requests are not being made. You can always request to lower your per minute rate limit by sending us an email at [support@mathpix.com](mailto:support@mathpix.com).

### I need to process a huge amount of images. How can I increase my monthly image limit?

There is no monthly limit if you are processing images. We have only limits for PDF processing (500 pages/month), which can be always topped up upon request. Learn more about our rate and page limits [here](/docs/convert/limits).

[<   Use Cases](/docs/convert/usecases)

[All Supported Math Characters   >](/docs/convert/supported_characters)