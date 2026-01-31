---
title: Improved handling of rotated content in PDF processing
url: https://mathpix.com/blog/improved-handling-of-rotated-content
---

# Improved handling of rotated content in PDF processing

* [xml version="1.0" encoding="UTF-8"?](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fmathpix.com%2Fblog%2Fimproved-handling-of-rotated-content)
* [xml version="1.0" encoding="UTF-8"?](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fmathpix.com%2Fblog%2Fimproved-handling-of-rotated-content)
* [xml version="1.0" encoding="UTF-8"?](https://www.reddit.com/submit?url=https%3A%2F%2Fmathpix.com%2Fblog%2Fimproved-handling-of-rotated-content&title=Improved handling of rotated content in PDF processing)

We are excited to share an update regarding an improvement in our `v3/pdf` processing.

Previously, PDF pages with rotated content were not handled correctly, causing certain parts of the page to be digitized as image links rather than being properly recognized as content. With the latest update, this issue has been resolved.

For example, a PDF page like this one used to be processed as an image link:

![Rotated table](/images/blog/rotated-table.webp)

With the current version of `v3/pdf`, the same PDF page is processed into the following MMD:

```
\begin{tabular}{|c|c|c|c|} 
\hline Characteristic & Test & Acceptance criteria ${ }^{a}$ & Observed differences ${ }^{\text {b }}$ \\ 
\hline Molecular mass & MALDI-TOF & $\leq 3 \mathrm{kDa}$ per monomer & $0.4-0.8 \mathrm{kDa}$ \\ 
\hline Extent of pegylation (1) & SEC-MALS & $\leq 3 \mathrm{~mol}$ PEG per mole protein & $1.7-2.4 \mathrm{~mol}$ \\ 
\hline Extent of pegylation (2) & HPLC-MS ${ }^{\text {C }}$ & $$ \begin{aligned} & \leq 10 \% \text { difference in pegylation at each potential binding } \\ & \text { site } \end{aligned} $$ & Comparable, despite differences in peptides containing multiple lysine groups ${ }^{\mathrm{d}}$ \\ 
\hline Calorimetry & DSC & $$ \begin{aligned} & \leq 2{ }^{\circ} \mathrm{C} \text { for } \mathrm{Tm} \\ & \leq 15 \% \text { for calorimetric enthalpy } \end{aligned} $$ & \begin{tabular}{l} $$ \operatorname{Tm} 0.06-0.54^{\circ} \mathrm{C} $$ \\ Calorimetric enthalpy $4-19 \%^{\text {e }}$ \end{tabular} \\ 
\hline Secondary structure & \begin{tabular}{l} CD spectroscopy: \\ Far-UV scan (190-250 nm) \end{tabular} & $\leq 10 \%$ difference in each secondary structure motif ${ }^{f}$ & $\leq 2 \%$ difference in proportions of any motif \\ 
\hline Tertiary structure & \begin{tabular}{l} CD spectroscopy: \\ Near-UV scan ( $250-350 \mathrm{~nm}$ ) \end{tabular} & No obvious differences when CD spectra overlaid & No obvious differences in CD spectroscopy scans \\ 
\hline Thermal unfolding & CD spectroscopy at fixed wavelength of 220 nm , over a range of temperatures & No obvious differences when CD spectra overlaid & \begin{tabular}{l} No significant differences in CD spectroscopy scans ${ }^{g}$ \\ Consistent melting temperatures \end{tabular} \\ 
\hline Purity & SDS-PAGE & Similar banding profiles; no additional bands (representing new impurities) & Similar banding profiles with no new impurities \\ 
\hline Enzyme kinetics & & $$ \begin{aligned} & K_{\mathrm{m}}: 10-20 \mu \mathrm{M} \\ & V_{\mathrm{max}}: 0.10-0.15 \mu \mathrm{~mol} / \mathrm{min} / \mu \mathrm{g} \\ & K_{\mathrm{cat}}: 58-88 \mathrm{~s}^{-1} \end{aligned} $$ & Within defined ranges ${ }^{\text {h }}$ \\ 
\hline \end{tabular} 
\footnotetext{ $C D$ circular dichroism, DSC differential scanning calorimetry, $H P L C-M S$ high-performance liquid chromatography-mass spectrometry, $K_{\text {cat }}$ catalytic rate constant, $K_{\mathrm{m}}$ Michaelis constant, $M A L D I$ TOF matrix assisted laser desorption ionization time-of-flight, $P E G$ polyethylene glycol, $S D S$ - $P A G E$ sodium dodecyl sulfate polyacrylamide gel electrophoresis, $S E C$ - $M A L S$ size-exclusion chromatography with multi-angle static light scattering, Tm transition peak midpoint (melting temperature), UV ultraviolet, $V_{\text {max }}$ maximum velocity ${ }^{2}$ Maximum difference between lyophilized and liquid pegaspargase to conclude equivalence between formulations Range for differences between paired lots of lyophilized and liquid pegaspargase ${ }^{c}$ L-Asparaginase was reacted with succinic anhydride under similar conditions to those used for pegylation, resulting in a conformation similar to that found during the manufacturing pegylation step.
```

And it renders correctly as:

![Rotated table](/images/blog/rotated-table-new.webp)

### Other OCR updates and bugfixes

* Improved table recognition, with accent on math-heavy tables
* Added parameter `include_chemistry_as_image` to return chemistry as an image crop with SMILES content in the alt-text
* Fixed double output in `latex_styled` format in some cases
* Code blocks now have double newline separation when multiple pages are joined which is more consistent (it used to be a single newline)
* Fixed a bug where a single line footnote text was sometimes left unclosed, without a matching closing `}`