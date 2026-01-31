---
title: Snip with OCR 2.0 on Desktop
url: https://mathpix.com/blog/snip-2.0
---

# Snip with OCR 2.0 on Desktop

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-2.0)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-2.0)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fsnip-2.0&title=Snip with OCR 2.0 on Desktop)

The new Snip app comes with a lot more functionality and customization, most notably the option to use the new OCR 2.0. Our old OCR (OCR 1.0) was optimized for small snippets of text or one equation at a time. Now, with OCR 2.0, you can scan images with much more content, like paragraphs and full pages!

## OCR 2.0

OCR 2.0 is optimized to scan Snips with a lot of content, like multiple paragraphs or a full page of text.

### Multiple paragraphs

OCR 2.0 can read up to a full page. Here is an example scanning two paragraphs and a block-mode equation in one Snip:

### Smart handling of new lines

OCR 2.0 can read a full page of text, but the output will not contain undesired line breaks. This way, you won’t need to delete each line break when you paste the text into an editor. The only exception is for images containing a list, where it’s clear that new lines should be preserved in the output.

### Easier to read syntax

We improved our recognition and syntax for multiline equations. Now, instead of expressing them with array syntax, we use `//` and `&` to denote new lines and alignment. We also add new lines to the LaTeX so it’s easy to read the source:

![Adding newlines to the code for readability](/images/newlines_example.webp)

### Other notes about OCR 2.0

* OCR 2.0 cannot read two-column pages.
* If there is anything in the image that we can’t read (like a figure), it will be skipped.
* OCR 2.0 works well, but we are considering it in beta while we continue to work out the kinks.

### How to activate OCR 2.0

OCR 2.0 can be activated in the **General** tab of your Settings.

![original image](/images/ocr_version_setting.webp)

If you want to continue using OCR 1.0 for individual equations and smaller bits of text, no need to do anything! It is still the default option.

## OCR option to ignore fonts

Many users have asked for an option to ignore any special math fonts in Snips. We have now added an option to ignore fonts in the **Formatting** tab of your app Settings. This option will be disabled by default.

![original image](/images/remove_fonts_setting.webp)

Here is an example of how Snip will recognize equations when ignoring fonts is enabled…

The source image:

![Source image remove fonts example](/images/blog/fonts_example_source.webp)

The result when **Remove math fonts** is enabled:

![Rendered image remove fonts example](/images/fonts_example_no_fonts.webp)

```
C^{n}, \psi=\psi(t) \in C^{n}
```

The result when **Remove math fonts** is disabled:

![Rendered with fonts image remove fonts example](/images/fonts_example_with_fonts.webp)

```
\mathbb{C}^{n}, \psi=\psi(t) \in \mathbb{C}^{n}
```

## More compact and navigable from the keyboard

Now that Snip can scan much bigger chunks of content with OCR 2.0, we wanted to make the app more compact to save you as much screen space as possible.

### Separate tabs

We separated **OCR** and **Original** tabs for viewing either image with their respective text/LaTeX or URL format options:

![OCR tab](/images/ocr_tab.webp)

### Open the original image during editing

We also removed the original image from the editing screen to save space, because usually the source is already somewhere on your screen during editing. If you need to refer to the original image while making edits, you can open the original image file to view it.

![OCR tab](/images/open_original_image.webp)

### More shortcuts for easier navigation

Even with the addition of tabs, you can still easily navigate your Snips with only your keyboard using these shortcuts:

`▶`: View next Snip

`◀`: View previous Snip

`shift + ▶`: View latest Snip

`shift + ◀`: View earliest Snip

`▲` and `▼`: Change selected format row

`shift + ▲` and `shift + ▼`:

For all shortcuts you can use in Snip, see our User Guide articles:

* [Shortcuts on Mac Snip](https://mathpix.com/docs/snip/macos-overview#shortcuts)
* [Shortcuts on Windows Snip](https://mathpix.com/docs/snip/windows-overview#shortcuts)

### Mouse-free editing

Editing a Snip can also be done completely mouse-free! Select your desired format, then hit `ENTER` to open the editor. While editing, you can use `ENTER` to create a new line and `SHIFT + ENTER` to save your changes.

## User guide

We have added a [Snip user guide](https://mathpix.com/docs/snip) with support and how-to articles for Snip users. It’s a great resource if you want to learn how to use the app, what it is most useful for, and answers to frequently asked questions.

For quick access, use the **User Guide** link in your app menu!

## Discounted yearly Pro plan

We have added a discounted yearly Pro subscription plan for individual Snip accounts. To upgrade to the yearly Pro plan, go to [accounts.mathpix.com/subscription](https://accounts.mathpix.com/subscription) and then choose **Switch to yearly billing and get two months free!** before clicking the **Upgrade** button.

![](/images/yearly-billing.webp)

For more on upgrading to the Pro plan, check out this [how-to guide](https://mathpix.com/docs/snip/upgrading-indv-subscription)!

## Minor improvements and bug fixes

**All:**

* A **Delete All** button has been added to your Snip List screen for deleting all Snips on your account at once
* All rendered images now have a transparent background (rather than white)
* Speed improvements for accounts with > 1,000 Snips

**Mac only:**

* Added TIFF image option for exporting (in Export Image Settings)
* Added way to configure the DPI of exported images (in Export Image Settings)

![Image setting button](/images/image_settings.webp)

**Windows only:**

* Add the ability to create a Snip from Markdown or LaTeX text
* Added support for HDPI screens and external monitors
* Improved preview size in List view