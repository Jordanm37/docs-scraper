---
title:  Snip with Overleaf
url: https://mathpix.com/docs/snip/snip-with-overleaf
---

i

* [Docs](/docs)  >
* [Snip](/docs/snip/overview)  >
* [Compatibility](compatibility)  >
* [Using Snip with Overleaf](snip-with-overleaf)

* [Using Snip with Overleaf](#using-snip-with-overleaf)
  + [The Preamble](#the-preamble)
  + [Inserting math into Overleaf from Snip](#inserting-math-into-overleaf-from-snip)
  + [Inserting tables into Overleaf from Snip](#inserting-tables-into-overleaf-from-snip)
    - [More information on the LaTeX packages Mathpix-markdown supports](#more-information-on-the-latex-packages-mathpix-markdown-supports)

# Using Snip with Overleaf

[Overleaf](https://www.overleaf.com/) is the most commonly used online LaTeX editor, and Snip is very convenient to use with Overleaf since Snip is optimized to give you a LaTeX output for your math and tables.

Follow the steps below to use Snip with Overleaf. You can also watch a full video about [Using Snip with Overleaf](https://www.youtube.com/watch?v=JwHoZPvsNVA) on our Youtube channel.

## The Preamble

When using Snip with Overleaf, or any other LaTeX document editor, it is important to add the following commands to the document’s Preamble. The Preamble is the first section of your LaTeX document, all the text in your `.tex` file before `\begin{document}`. Here you will define which [packages](https://ctan.org/) you want to use when compiling your document into a PDF.

This is what you need to include in your document’s Preamble so that all special LaTeX features that Mathpix supports will display correctly when LaTeX copied from Snip is pasted into your Overleaf document:

```
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{multirow}
\usepackage{graphicx}
```

## Inserting math into Overleaf from Snip

1. Display the equation want to insert into your document on your screen:

![Display your desired equation](/images/display-equation1.webp)

2. Click the screenshot button or enter the keyboard shortcut `ctrl+alt+m`/`ctrl+command+m`:

![Click the screenshot button](/images/screenshot-button1.webp)

3. Click and drag the crop box around your desired equation, release to Snip:

![Snip your equation](/images/snip-equation.webp)

4. Check your Snip result, then click the row with your desired LaTeX format to copy to your clipboard:

![Click the 2nd row to copy inline math](/images/row-modes.webp)

5. Open your Overleaf document and put your cursor at the location in the document where you would like to insert an equation, and paste!

If you paste the **inline math** format into your Overleaf document, it will look like this:

![Click the 2nd row to copy inline math](/images/inline-example.webp)

If you paste the **block mode math** format into your Overleaf document, it will look like this:

![Click the 3rd row to copy block mode math](/images/block-mode-example.webp)

If you paste the **numbered block mode math** format into your Overleaf document, it will look like this:

![Click the 4th row to copy numbered block mode math](/images/numbered-block.webp)

Here is a short video showing all the steps together (using block mode math in this example):

## Inserting tables into Overleaf from Snip

Inserting a table into Overleaf from Snip requires the same steps as inserting an equation, the only difference is that you want to make sure to copy the 2nd LaTeX row, because that will have the `\begin{tabular}...\end{tabular}` LaTeX text mode format. This format is optimal for rendering tables in LaTeX documents.

![Copy the tabular format to use in Overleaf](/images/copy-tabular.webp)

For more information on the using the LaTeX `tabular` and `table` environments, see our [syntax guide](/docs/mathpix-markdown/tables).

### More information on the LaTeX packages [Mathpix-markdown](/docs/mathpix-markdown/overview) supports

* [multirow](https://ctan.org/pkg/multirow) package
* [amsmath](https://ctan.org/pkg/amsmath) package
* [graphicx](https://ctan.org/pkg/graphicx) package
* [amsfonts](https://ctan.org/pkg/amsfonts?lang=en) package

[<   Compatibility](/docs/snip/compatibility)

[Using Snip with Microsoft Word   >](/docs/snip/snip-with-microsoft-word)