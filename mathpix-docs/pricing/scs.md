---
title: Mathpix SCS Pricing
url: https://mathpix.com/pricing/scs
---

# Secure Conversion Service

  

Accurately convert large PDF and image libraries into machine readable text files in hours, not months.

### Cost efficiency

Batch API offers cost savings over interactive API due to optimized processing of multiple files, allowing us to provide lower rates to customers.

### Higher throughput

SCS specializes in high-throughput batch processing, rapidly converting large directories, in contrast to Convert API's single-file optimization.

### Data privacy

Ensures document protection with robust encryption and compliance with industry-standard security protocols.

### Ease of use

No need to configure API and send one file at a time. Simply give us access to your data bucket, and your requirements, and we'll do the rest for you.

#### Frequently Asked Questions

When should I use SCS instead of Convert API?

* **High-volume processing:** If you need to process more than tens of millions of PDF pages in a short period of time, SCS is designed for large-scale batch jobs and can handle this efficiently.
* **Asynchronous workflows:** When real-time results aren’t necessary, SCS processes documents in the background, making it ideal for big jobs.
* **Advanced workflow needs:** While our API is highly secure, SCS is tailored for workflows that require additional customization and direct integration with storage providers like AWS S3, GCP GCS, Alibaba OSS, and Baidu BOS, ensuring seamless and secure data handling at scale.

What are some use cases for SCS?

Secure Conversion Services (SCS) is ideal for:

1. **Training and fine-tuning large language models (LLMs):** Preparing massive datasets from PDFs or images for training or fine-tuning LLMs. SCS’s scalability and ability to generate structured outputs make it perfect for producing high-quality training data.
2. **Enterprise document processing:** Converting large volumes of legal, financial, or technical documents into structured data for internal systems, analysis, or archival purposes.
3. **Large-scale academic archives:** Universities and research institutions digitizing and processing massive collections of research papers, lecture notes, or archives into accessible formats.
4. **Publishing and content digitization:** Publishers processing books, journals, or articles with complex layouts, including math, tables, and images, for online or print use.
5. **Custom workflows for sensitive data:** Organizations with strict privacy and data security requirements that need direct integration with storage providers such as AWS S3, Microsoft Azure, GCP GCS, Alibaba OSS, or Baidu BOS. SCS enables secure management of input and output data within designated storage buckets.
6. **High-volume projects with flexible timelines:** Handling tens of millions of documents asynchronously for projects where scalability and efficiency are key, but immediate, real-time results aren’t necessary.

  

SCS is particularly well-suited for industries leveraging LLMs and AI, as well as organizations requiring secure, efficient, and large-scale batch processing.

How do you use SCS?

Using SCS involves these steps:

1. Set up access to your storage provider:

   * Grant Mathpix access to your storage bucket (e.g., AWS S3, Microsoft Azure, GCP GCS, Alibaba OSS, Baidu BOS) via access tokens.
2. Upload input files to your bucket:

   * Place your input files (PDFs or images) in a designated folder within your storage bucket.
3. Configure SCS processing:

   * Mathpix processes the documents asynchronously, pulling input files from your bucket, running OCR or conversion, and writing the results back to an output folder in the same bucket.
4. Retrieve processed results:

   * Processed outputs, such as structured data (e.g., Mathpix Markdown), are saved in your designated output folder for easy retrieval.

For more details, or to get started with SCS, contact [support@mathpix.com](mailto:support@mathpix.com).

How fast can SCS process documents?

SCS is designed for large-scale, high-speed processing. It can handle hundreds of millions of pages per day and scale to process several billion pages in just a few weeks.

This speed makes it ideal for organizations managing massive workloads, like converting large archives or running extensive data extraction projects. The exact processing time depends on document complexity and file size, but SCS is built to maximize efficiency and throughput.

If you’re working with tight timelines, feel free to reach out to discuss your specific requirements, and we can help optimize the process for your needs.

What output formats are available?

SCS can generate outputs in the following formats:

* Markdown
* Mathpix Markdown
* LaTeX
* DOCX
* HTML
* lines.json

  

You can select one or multiple formats based on your requirements.

Does SCS use the latest OCR models?

Yes, SCS always runs the latest Mathpix OCR models to deliver the most accurate and reliable results.

What is the minimum volume required for SCS?

SCS is designed for large-scale projects, with a minimum recommended volume of tens of millions of pages.

Is there a maximum file size or page count?

There are no strict limits on file size or page count. However, for optimization, we recommend splitting files with more than 5,000 pages into smaller parts.