---
title:  Mathpix Markdown User Guide: What is Mathpix Markdown?
url: https://mathpix.com/docs/mathpix-markdown
---

* [Docs](/docs)  >
* [Mathpix Markdown](/docs/mathpix-markdown/overview)  >
* [What is Mathpix Markdown?](overview)

# What is Mathpix Markdown?

Mathpix Markdown is a superset of Markdown that adds helpful syntax for the STEM community, such as advanced equation, table, and chemistry support. Wherever possible, we borrow syntax from LaTeX. In other cases (such as chemistry) we invent new syntax that is backward compatible with Markdown.

![Mathpix Markdown details](/images/snip-app/mmd-diagram-big.webp)

Here are the key benefits over plain Markdown:

* better equation support via LaTeX syntax (powered by MathJax), including equation numbering and referencing conventions from LaTeX
* better support for [tables](/docs/mathpix-markdown/tables), via the LaTeX `tabular` syntax, which allows for complex, nested tables often seen in scientific publications
* advanced [figure referencing](/docs/mathpix-markdown/figures) via LaTeX syntax
* support for abstracts, author [lists](/docs/mathpix-markdown/lists), and linkable sections; these are a fact of life for academic publications
* support for chemistry diagrams represented with SMILES markup, compatible with popular chemistry tools like Chemdraw
* support for images: parse and render additional parameters such as width, height, alignment
* support for [theorems and proofs](/docs/mathpix-markdown/theorems-and-proofs)

![Editing an MMD file in VS Code](/images/mmd-vscode.webp)

## How to use Mathpix Markdown to manage scientific content?

Mathpix Markdown is an open format with multiple implementations:

* you can use the [VS Code plugin](/docs/mathpix-markdown/how-to-mmd-vscode) (see picture above) to edit mmd files
* use can use our [web editor](https://snip.mathpix.com) to edit, export, and publish mmd files (with exports to pdf and docx formats)
* you can use our open source implementation of the Mathpix Markdown spec on [Github](https://github.com/mathpix/mathpix-markdown-it) to render content on your website
* you can use our command line tool for converting document types and experimental static site generator [MPX CLI](https://github.com/mathpix/mpx-cli)

[Syntax Reference   >](/docs/mathpix-markdown/syntax-reference)