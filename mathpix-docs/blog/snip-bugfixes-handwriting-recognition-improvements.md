---
title: Improved handwriting recognition, Snip bugfixes, and more
url: https://mathpix.com/blog/snip-bugfixes-handwriting-recognition-improvements
---

# Improved handwriting recognition, Snip bugfixes, and more

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-bugfixes-handwriting-recognition-improvements)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-bugfixes-handwriting-recognition-improvements)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-bugfixes-handwriting-recognition-improvements&title=Improved handwriting recognition, Snip bugfixes, and more)

*Update (4/1/2022): We have extended the deadline for the current Spectra competition to May 1, 2022.*

# Spectra review paper writing competition deadline extended by two weeks

We are extending the [Spectra](https://spectra.mathpix.com) review paper writing competition another two weeks to allow for more submissions. The total prize money is $10K so don’t miss out! We have removed downvoting from the site, after noticing the emergence of downvoting others’ work as a competitive strategy.

We thank participants for their hard work and patience as we experiment with publishing our user’s knowledge and expertise in a web-friendly manner. Our thesis is that if we can make it easier for the STEM community to create and publish content as well as read it on any device, free from PDFs, there will be more such content, which will foster curiosity and discovery in STEM fields.

[Learn more about the contest and how to submit your work.](/blog/second-spectra-competition)

# Improved math handwriting recognition

We have recently introduced visual transformers to our core architecture, along with some secret sauce. The improvements are especially dramatic on graduate-level math handwriting recognition. If you haven’t [tried Mathpix out on handwritten math](/handwriting-recognition) in a while, definitely take it out for a spin! We bet you’ll be pleasantly surprised at how accurate it is for professors and students.

![An example of our improved handwriting recognition on linear algebra notes](/images/handwriting-reco-example.webp)

# Bugfixes in Snip web app

We have fixed issues related to exporting files from [Snip](https://snip.mathpix.com) to DOCX and LaTeX, including corrupt DOCX files and timeouts on big files (document conversion now works asynchronously).

We have also implemented an autosave feature to Notes to make sure people never ever lose their work — that’s the worst thing that an editor can possibly do.

# Deprecated `\atop` in favor of `\substack`

In the latest release, we deprecated `\atop` command in favor of `\substack`. The `\atop` has infix syntax and is much less readable in complex cases compared to the `\substack`. Moreover, `\atop` was built specifically to create fractions without horizontal fraction bar, while `\substack` is a more general command used to create multiline subscripts or superscripts.

Here’s an example:

![An example equation](/images/example-equation-substack.webp)

LaTeX before:  
`\lim _{x \rightarrow 0 \atop y \rightarrow 0} \frac{e^{-x^{2}-y^{2}}-1}{x^{2}+y^{2}}`

LaTeX after:  
`\lim _{\substack{x \rightarrow 0 \\ y \rightarrow 0}} \frac{e^{-x^{2}-y^{2}}-1}{x^{2}+y^{2}}`

# Syntax error bugfixes

Our new OCR models feature stringent guarantees of syntactic correctness. This resolves a rare but long-standing problem of occasionally malformed LaTeX strings, resulting in rendering errors due to double subscripts, double superscripts, malformed tables, and other syntax issues. This has been fixed at a fundamental level. Syntax issues are essentially completely fixed.