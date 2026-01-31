---
title: Mathpix now supports text OCR
url: https://mathpix.com/blog/mathpix-text-ocr
---

# Mathpix now supports text OCR

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fmathpix-text-ocr)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fmathpix-text-ocr)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fmathpix-text-ocr&title=Mathpix now supports text OCR)

Our customers frequently encounter images that contains words. To support text more naturally, and especially multi-lined text, we now offer the text format. If you include “text” it in the formats API input, you shall get a field resultJson.text which will be in math mode. This format uses newline characters to compose multi line equations and paragraphs of text, using `\( ... \)` delimiters for inline math, and `\[ ... \]` delimiters for block level math. These can be preprocessed as necessary to work with whatever markup delimiters your environment supports (e.g. `$$` and `$` for MathJax). For example, the following equation:

![Text example](/images/text_ocr_1.webp)

is represented as:

```
How do you multiply \( \frac { 7 x } { 5 x + 15 } \cdot \frac { x + 3 } { 8 } ?  \)
```

in text mode, and:

![Text example](/images/text_ocr_2.webp)

is represented as:

```
Solve the equation.
\( \log _ { 3 } ( 2 x - 3 ) = \log _ { 3 } ( x + 5 ) \)
```

in text mode (note the new line character!).