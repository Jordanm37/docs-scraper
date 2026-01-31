---
title: Convert whole PDFs to LaTeX, DOCX, Markdown; updated pricing
url: https://mathpix.com/blog/pdf-processing-new-pricing
---

# Convert whole PDFs to LaTeX, DOCX, Markdown; updated pricing

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fpdf-processing-new-pricing)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fpdf-processing-new-pricing)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fpdf-processing-new-pricing&title=Convert whole PDFs to LaTeX, DOCX, Markdown; updated pricing)

*This post was updated on 10/5/2023 with new information about the API pricing for PDF processing.*

We are very excited to announce the release of a new feature that we have been working on for a long time: full PDF processing in Snip and the API!

Now, instead of taking Snips of sections of a PDF, you have the ability digitize the whole PDF file at once and receive a LaTeX, DOCX, Markdown, or HTML file.

This feature relies completely on visual information and extracts text, equations, and diagrams together. You can use this feature to convert printed, scientific PDFs into editable Mathpix Markdown, which can then be exported to DOCX, LaTeX, HTML, PDF, and Overleaf.

PDF processing can handle two-column scientific articles without any issues. Section headers are recognized as well. Documents with strange layouts, lots of content in margins are not supported, or PDFs generated with handwritten content are not supported at this time.

## PDF processing in Snip

This feature is currently live in the web version of Snip at [snip.mathpix.com](https://snip.mathpix.com), which is essentially the Snip app formulated as an interoperable document editing experience.

To use the feature, simply drag a PDF file that you want to convert into the editor, or use the file picker in the PDF menu at the upper left:

![](/images/upload-pdf-button.webp)

After the document has been converted to Mathpix Markdown format, you can use Snip in your browser to edit the document with instant rendering updates. Once you are done editing, you can export to any number of output formats or destinations using the menu at the top right:

![](/images/export-pdf-button.webp)

Here is short video showing all the steps:

Users on the Free plan get up to 20 PDF pages processed per month for free. Users on the Pro plan get up to 1000 PDF pages processed per month included with their subscription.

## Updates to Snip pricing with new PDF processing features

In order for us to support this new PDF digitization feature without potentially incurring unbounded processing fees, we are introducing limits to the previously unlimited Pro plan. These changes will have no impact on pricing for 99% of users.

For users creating more than 5K Snips per month, and organizations creating over 5K Snips per month per user, we will be providing an opt-in to enable extra usage above these new limits. The opt-in will prevent any surprise billing due to the new extra usage fees.

You can enable extra usage by going to [your account settings](https://accounts.mathpix.com/upgrade). Extra usage billing will only be available for users with a PayPal or a Credit/Debit card payment method on file. If you paid for your subscription with Alipay, you will need to add an additional payment method to take Snips or process PDFs above your monthly limit.

For customers on the Pro plan who enable extra usage, an extra usage fee of:

* $0.002 per Snip
* $0.0035 per PDF page

will apply for all usage beyond the 5,000 Snips and 1000 PDF pages included with their monthly subscription (or 12 times that for yearly subscriptions).

Users on the Free plan will get 20 PDF pages worth of processing for free with their Snip subscription.

Snip Organizations will get 5K Snips per month per user and 1000 PDF pages per user per month included with their subscriptions. The same extra pricing of of $0.002 per Snip and $0.0035 per PDF page will apply.

### FAQ for Snip Subscription Updates

**Q: Where is the new pricing page?**  
**A:** <https://mathpix.com/#pricing>

**Q: Where can I check detailed billing page to check usage and extra usage?**  
**A:** To check your overages incurred in the current billing term, visit <https://accounts.mathpix.com/subscription>.

**Q: What happens if I do not want to enable overage billing?**  
**A:** If you are on the Pro plan and reach your monthly Snip or PDF page limit, you will be asked if you would like to enable overage billing. If you agree, you will  be able to continue taking Snips and processing PDFs. If not, you will not be able to take more Snips or process more PDF pages until your account resets on the day of the month you originally upgraded to the Pro plan.

## PDF processing in Convert API

Convert API customers can access the new PDF processing feature via the [v3/pdf](https://docs.mathpix.com/#process-pdf-v3-pdf) API endpoint.

For processing PDF files from your local machine, you can also use the [Spectra CLI tool](https://github.com/Mathpix/spectra) with your API key.

The [API pricing](https://mathpix.com/convert#pricing) for PDF processing is:

* $0.005/page (0-1M pages)
* $0.0035/page (1M+ pages)