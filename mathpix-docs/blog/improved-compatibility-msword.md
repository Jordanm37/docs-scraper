---
title: Major improvements to MS Word compatibility
url: https://mathpix.com/blog/improved-compatibility-msword
---

# Major improvements to MS Word compatibility

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fimproved-compatibility-msword)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fimproved-compatibility-msword)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fimproved-compatibility-msword&title=Major improvements to MS Word compatibility)

We have just released major improvements to Snip that include much better compatibility with Microsoft Word. Word sometimes requires special MathML syntax to render certain types of equations correctly, and for that reason we have added a new format called **MathML (MS Word)**. This is the format that should always be used when inserting equations from Snip into an MS Word document.

# Improvements and bug fixes

### Proper sizing of brackets and braces

There is no longer a need to update an equation with matrices or tall braces to “Professional” after pasting into MS Word to fix the size of the brackets or braces. Now, all equations are formatted as professional by default.

![An example of tall matrices working well in MS Word](/images/matrices.webp)

### Multi-line equations, aligned equations, arrays

We fixed issues related to the formatting of multi-line, aligned equations, and arrays. All different types of alignments are working well in the latest version.

![An example of an aligned equation working well in MS Word](/images/snip-user-guide/aligned.webp)

### Summations and integrals

Some summations and integrals, when pasted into MS Word, were rendering with an empty box after the `\sum` or `\int`. This bug has been fixed.

![An example of a summation working well in MS Word](/images/summation.webp)

![An example of an integral working well in MS Word](/images/integral.webp)

### Dots and other characters

Some bugs like dots over characters rendering incorrectly has been fixed.

![An example of dots working well over characters in MS Word](/images/dots.webp)

# How to use

On your **OCR** tab, you will now see **Copy MS Word** button appear instead of the **Copy MathML** button.

![Find the Copy MS Word button on your OCR tab](/images/copy-msword.webp)

Clicking this button or navigating to it with your keyboard (new feature!) will now copy the MS Word optimized format to your clipboard instead of plain MathML. You can also access this format as the first option on the **Data** tab.

![Find the Copy MS Word button on your OCR tab](/images/msword-data.webp)