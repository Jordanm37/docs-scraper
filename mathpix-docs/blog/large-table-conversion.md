---
title: Improved Table Support: Introducing our new algorithm for converting large tables
url: https://mathpix.com/blog/large-table-conversion
---

# Improved Table Support: Introducing our new algorithm for converting large tables

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Flarge-table-conversion)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Flarge-table-conversion)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Flarge-table-conversion&title=Improved Table Support: Introducing our new algorithm for converting large tables)

# Support for large tables

We now support a new advanced algorithm for parsing large tables that can be enabled via the new `enable_tables_fallback` field, which is `false` by default.

Below are some examples of tables that didn’t work but they do now. Each example is a representative of a full class of tables for there will be an output as a result of the new algorithm.

*Example input:*

![Example input](/docs/snip/images/input-large-table.webp)

*MMD output:*

![MMD input](/docs/snip/images/output-large-table.webp)

*Example input:*

![Example input](/docs/snip/images/input-large-table1.webp)

*MMD output:*

![MMD input](/docs/snip/images/output-large-table1.webp)

For Mathpix Snip users the new algorithm is enabled by default. Check out the video that shows how you can digitize large tables of data and paste the results into a spreadsheet. Works like a charm.

# Asciimath fixes

We have fixed asciimath outputs for vertical math. Vertical addition and multiplication is now simplified and represented using standard math.

For example, the asciimath output for:

![Asciimath input](/docs/snip/images/input-asciimath.webp)

will be:

`2000-1999`

# PDF processing improvements

We have added a new parameter `auto_number_sections` which is `true` by default (<https://docs.mathpix.com/#process-a-pdf>), but can be set to `false` if you do not want section numbering in your outputs. Note that this parameter is considered in the initial parsing of the PDF and applies to all export options.

# Formatting consistency improvements for numbers inside of tables

Previously, integers were included as text inside tables, and negative numbers and decimal numbers were included as inline math inside tables. To resolve this inconsistency, we now include negative numbers and decimal numbers as normal text inside tables. This means we now will return:

```
\begin{tabular} { |l||c|c| } 
1 & - 0.142 & - 0.080 
\end{tabular}
```

instead of:

```
\begin{tabular} { |l||c|c| }
1 & \( - 0.142 \) & \( - 0.080 \) 
\end{tabular}
```

This impacts asciimath outputs because we no longer return numeric non-integer table cells as asciimath equations. Table cells that contain variables or equations will continue to be represented in text using inline math delimiters, and will continue to be captured as asciimath equation elements.

# Formatting consistency improvements for isolated numbers

All isolated numbers are now always recognized as inline math inside text outputs for v3/latex, v3/text, and v3/strokes. Previously, isolated responses for numbers could yield such responses as `3` or `\( 3.14 \)`. Now, we return `\( 3 \)` instead of `3` to increase consistency.

Since PDFs are text first, this change does not apply to v3/pdfs, where we are biased towards outputting numbers in text mode when they don’t appear inside an equation.

# Other improvements

We have also done the following:

* improved the robustness of PDF processing
* sped up the exporting of documents to DOCX for large documents
* fixed rare 502 and 504 responses