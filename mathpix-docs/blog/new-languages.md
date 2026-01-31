---
title: SuperNet‑108: OCR support for new languages, more reliable results for old scanned documents, and more
url: https://mathpix.com/blog/new-languages
---

# SuperNet‑108: OCR support for new languages, more reliable results for old scanned documents, and more

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fnew-languages)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fnew-languages)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fnew-languages&title=SuperNet‑108: OCR support for new languages, more reliable results for old scanned documents, and more)

## OCR improvements

We are now supporting text recognition for two new languages:

* Greek
* Georgian (modern alphabets, Mkhedruli and Mtavruli)

We have also improved recognition for challenging old scanned documents. To illustrate, the following paragraph of text:

![Sample of old document scan](/images/blog/old-scanned-sample.png)

will now be recognized as:

```
Posto tal Letterario contante in vista di chi legge non saprei dir, di qual peso, è da notarsi, che questo nome sustantivo proprio Livorno , il quale in latina lingua dicesi Liburnus Labro , specificatamente , anzi individualmente indica la Città , e. Porto di Livorno come si legge in Cicerone, nel Volterrano , e nell' Alberti (1) , ma che sotto quel nome di Liburnus esser può soggetto a più significazioni, che lo rendono equivoco.
```

Finally, we are changing our output to be more Unicode aware, and to output Unicode symbols instead of Latex commands where appropriate (in text). For example, the following image:

![Sample of text containing ★](/images/blog/star-sample.png)

will now return the following response:

```
Text sentence that contains ★ will be recognized without Latex command for a star.
```

instead of the response that we used to return:

```
Text sentence that contains $\star$ will be recognized without Latex command for a star.
```

Note, that while many other Unicode symbols are supported in-text context, when present in math context, we will still return proper Latex commands for equations.

## Output formatting changes

Output formatting changes are related to our efforts to have more Unicode friendly results. We are changing the way form fields are represented in the output:

* We are now using □ in cases where 
  ◻
  ◻
  ◻\square◻ was used (e.g. checkboxes, and some other form boxes)
* We are now using ◯ in cases where 
  ◯
  ◯
  ◯\bigcirc◯ was used (e.g. radiobuttons)