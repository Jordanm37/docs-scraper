---
title: New spell check feature significantly improves English handwriting OCR
url: https://mathpix.com/blog/spellcheck-english-handwriting
---

# New spell check feature significantly improves English handwriting OCR

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fspellcheck-english-handwriting)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fspellcheck-english-handwriting)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fspellcheck-english-handwriting&title=New spell check feature significantly improves English handwriting OCR)

We have added a new `enable_spell_check` option to the [v3/text](https://docs.mathpix.com/#process-an-image) and [v3/pdfs](https://docs.mathpix.com/#process-a-pdf) endpoints. This API option enables a predictive mode for English handwriting that takes word frequencies into account to disambiguate words that are hard to read. This option is skipped when the language is not detected as English. Incorrectly spelled words that are clearly written will not be changed: this predictive mode is only enabled when the underlying handwritten word is visually ambiguous.

Demonstrating the new feature on the image below:

![A messy handwriting sample](/images/handwriting-sample-eng.webp)

Before spell check the output `text` is:

*Dolution:*  
*Ans 24). In developing a chart to flot a course of action, with many of the events or milestones, we will we Process deciscon pirogram chart.*  
*so, optison (A) is cossect ansuver.*

After spell check:

*Solution:*  
*Ans 24). In developing a chart to plot a course of action, with many of the events or milestones, we will we Process decision program chart.*  
*so, option (A) is correct answer.*

Notice the big improvement! The spelling-aware improvements are only live for English and have no impact on other languages. These improvements will be coming soon for Spanish, French, and German. We are excited to continue improving our math and text handwriting recognition capabilities.

Please note that incorrectly spelled words that are clearly written will not be changed: this predictive mode is only enabled when the underlying handwritten word is visually ambiguous.

Improved English handwriting recognition using spell check is also live in all [Snip Apps](/)!