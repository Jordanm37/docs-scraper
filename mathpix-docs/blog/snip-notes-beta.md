---
title: Snip web app (beta): OCR Powered Notes App With LaTeX Flavored Markdown
url: https://mathpix.com/blog/snip-notes-beta
---

# Snip web app (beta): OCR Powered Notes App With LaTeX Flavored Markdown

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-notes-beta)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-notes-beta)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-notes-beta&title=Snip web app (beta): OCR Powered Notes App With LaTeX Flavored Markdown)

*This post was updated on 31/5/2023 with new examples from the `mathpix-example` Snip account.*

Mathpix Snip was first released on MacOS as a native app. The reason was simple. We wanted to build the easiest way to extract LaTeX from equations in PDFs. Since building a screenshot app requires native functionality, we had to build native apps.

However, the downside of native apps is that they’re a lot more finicky than web apps, especially for Windows and Linux, which have less than stellar mechanisms for native app delivery. The most universal mechanism for delivering apps nowadays is Web. It works on every device and users will quickly abandon a web browser that doesn’t perform reliably.

Finally, [we have developed a web app](https://snip.mathpix.com) which we’re happy to share with the scientific and engineering community. Here’s a run down of the key features.

## Feature 1: paste images, edit content

We decided to release Snip for web in the form of a note taking environment. This is purposefully more of a lightweight, single-user, note taking app than a collaborative, serious, full-featured editing environment.

The coolest feature of our note taking app is that you can paste in an image, instantly see all the format options, and toggle between them (for example to insert a numbered equation, or a non-numbered one). If you paste an image of something that we can’t recognize, you can also still display it in your note.

## Feature 2: HTML first, PDF second experience with LaTeX Flavored Markdown (LFM)

We chose Markdown as the base language for our editor. It’s simple, popular, and fast. However, there are serious limitations with Markdown that make it unsuitable for serious academic work. For example, equation references, article titles, article authors, and abstracts cannot be represented in standard Markdown.

Therefore we decided to add elements of text mode LaTeX to Markdown. We call the resulting syntax: **LaTeX Flavored Markdown**. It was relatively simple to take a Markdown parser (we chose `markdown-it`) and augment it with these text mode LaTeX commands:

```
\title{My title}
\author{Author 1 \\ Author 2}
\begin{abstract} ... \end{abstract}
\section{Section name}
\subsection{Subsection name}
\eqref
\ref
\url{...}
\textbf{Bold font} 
\textit{Italicized font}
```

The beauty of this approach is two-fold.

First, users get a fast, flexible editing experience that is much faster than waiting around for PDFs to render. You can even have videos in your paper! SVGs are also supported natively. Note: you can still get a PDF by clicking on the Export to PDF button.

Secondly, users can now share convenient web links with their peers, making it much easier for them to digest content. Which brings us to the third big feature of our Notes app…

## Feature 3: easily share public links to beautiful web pages

We think it’s ridiculous that in 2019, the most cutting edge research in the world is being shared via PDFs, which require all sorts of zoom-in zoom-out gymnastics on phones to read.

By simply making a note public, you can share your hard won knowledge in a web friendly format that can be read easily on any device. No more sending links to huge PDF files. Here are some examples from the `mathpix-example` Snip account:

[LINEAR SUBSPACES IN CUBIC HYPERSURFACES](https://snip.mathpix.com/mathpix-example/notes/linear-subspaces-in-cubic-hypersurfaces-beccb38c-bfe2-4e8b-b24e-e600343164fa)

[Universal Kardar-Parisi-Zhang dynamics in integrable quantum systems](https://snip.mathpix.com/mathpix-example/notes/universal-kardar-parisi-zhang-dynamics-in-integrable-quantum-systems-8a85affe-4214-4a00-a465-f9acdf9dc6e3)

![Web and mobile reading example](/images/blog/web_and_mobile.webp)

These links make it much easier to digest content on a phone or tablet device than PDFs. Users get the best of both worlds. A fast HTML rendering engine, with shareable links, and an export to PDF option. This makes it easier to create documents, share them, read them online, and even print them and read them on paper.

## Feature 4: syncs with Snip mobile apps

Take a picture on mobile, and instantly insert it into your note. All you have to do is click on the image you want to insert, and the options menu will appear at your current cursor position:

## Feature 5: open source rendering engine (coming soon!)

We will soon be releasing an open source library for users to generate HTML from LaTeX Flavored Markdown, so users can publish content outside of Snip as well.

## Conclusion

Thoughts or comments? Try the app for yourself at [snip.mathpix.com](https://snip.mathpix.com) and send us feedback through the app!

![Mobile to web editor syncing example](/images/feedbackbutton.webp)