---
title:  Mathpix Markdown User Guide: Create & Format Tables
url: https://mathpix.com/docs/mathpix-markdown/tables
---

i

* [Docs](/docs)  >
* [Mathpix Markdown](/docs/mathpix-markdown/overview)  >
* [LaTeX Table Syntax](tables)

* [The tabular environment](#the-tabular-environment)
  + [Intro](#intro)
  + [Basic examples](#basic-examples)
  + [Text wrapping in tables](#text-wrapping-in-tables)
  + [Rows spanning multiple columns](#rows-spanning-multiple-columns)
  + [Columns spanning multiple rows](#columns-spanning-multiple-rows)
  + [Spanning in both directions simultaneously](#spanning-in-both-directions-simultaneously)
  + [Positioning tables](#positioning-tables)
  + [Captions, labels and references](#captions%2C-labels-and-references)
  + [Center-aligning captions](#center-aligning-captions)
  + [More examples](#more-examples)

# The tabular environment

## Intro

The `tabular` environment can be used to typeset tables with optional horizontal and vertical lines. The syntax looks as follows:

```
\begin{tabular}{<<table spec>>} <<table content>> \end{tabular}
```

The `table spec` argument tells LaTeX the alignment to be used in each column and the vertical lines to insert.

The number of columns does not need to be specified as it is inferred by looking at the number of arguments provided. It is also possible to add vertical lines between the columns here. The following symbols are available to describe the table columns

|  |  |
| --- | --- |
| `l` | left-justified column |
| `c` | centered column |
| `r` | right-justified column |
| `S` | align numbers at decimal point |
| `p{'width'}` | paragraph column with text vertically aligned at the top |
| `m{'width'}` | paragraph column with text vertically aligned in the middle |
| `b{'width'}` | paragraph column with text vertically aligned at the bottom |
| `|` | vertical line |
| `||` | double vertical line |
| `:` | dash vertical line |

By default, if the text in a column is too wide for the page, LaTeX won’t automatically wrap it. Using `p{'width'}` you can define a special type of column which will wrap-around the text as in a normal paragraph.

In the first line you have defined how many columns you want, their alignment and the vertical lines to separate them. Once in the environment, you have to introduce the text you want, separating between cells and introducing new lines. The commands you have to use are the following:

`&` - column separator;  
`\\` - start new row;  
`\hline` - horizontal line;  
`\hhline` - double horizontal line;  
`\hdashline` - horizontal dash line;  
`\cline{i-j}` - partial horizontal line beginning in column `i` and ending in column `j`.

## Basic examples

This example shows how to create a simple table in LaTeX. It is a three-by-three table, without any lines.

```
\begin{tabular}{ l c r }
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9 \\
\end{tabular}
```

|  |  |  |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Expanding upon that by including some vertical lines:

```
\begin{tabular}{ | l | c | r | }
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9 \\
\end{tabular}
```

|  |  |  |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

To add horizontal lines to the very top and bottom edges of the table:

```
\begin{tabular}{ | l | c | r | }
  \hline			
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9 \\
  \hline  
\end{tabular}
```

|  |  |  |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

And finally, to add lines between all rows, as well as centering

```
\begin{center}
  \begin{tabular}{ | l | c | r | }
    \hline
    1 & 2 & 3 \\ \hline
    4 & 5 & 6 \\ \hline
    7 & 8 & 9 \\
    \hline
  \end{tabular}
\end{center}
```

|  |  |  |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Aligning the same table to the left…

```
\begin{left}
  \begin{tabular}{ | l | c | r | }
    \hline
    1 & 2 & 3 \\ \hline
    4 & 5 & 6 \\ \hline
    7 & 8 & 9 \\
    \hline
  \end{tabular}
\end{left}
```

|  |  |  |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

An example of how you can align a column at a decimal point using `S`:

```
\begin{tabular}{l|S|r|l}
      \textbf{Value 1} & \textbf{Value 2} & \textbf{Value 3} & \textbf{Value 4}\\
      $\alpha$ & $\beta$ & $\gamma$ & $\delta$ \\
      \hline
      1 & 1110.1 & a & e\\
      2 & 10.1 & b & f\\
      3 & 23.113231 & c & g\\
    \end{tabular}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Value 1** | **Value 2** | **Value 3** | **Value 4** |
| α α alpha\alphaα | β β beta\betaβ | γ γ gamma\gammaγ | δ δ delta\deltaδ |
| 1 | 1110.1.00000 | a | e |
| 2 | 0010.1.00000 | b | f |
| 3 | 0023.113231. | c | g |

## Text wrapping in tables

The `p` attribute is used to specify the desired width of a column.  
Instead of `p`, use the `m` attribute to have the lines aligned toward the middle of the box or the `b` attribute to align along the bottom of the box.

Here is a simple example. The following code creates two tables with the same code; the only difference is that the last column of the second one has a defined width of 5 centimeters, while in the first one we did not specify any width. Compiling this code:

```
Without specifying width for last column:
\begin{center}
    \begin{tabular}{| l | l | l | l |}
    \hline
    Day & Min Temp & Max Temp & Summary \\ \hline
    Monday & 11C & 22C & A clear day with lots of sunshine.
    However, the strong breeze will bring down the temperatures. \\ \hline
    Tuesday & 9C & 19C & Cloudy with rain, across many northern regions. Clear spells
    across most of Scotland and Northern Ireland,
    but rain reaching the far northwest. \\ \hline
    Wednesday & 10C & 21C & Rain will still linger for the morning.
    Conditions will improve by early afternoon and continue
    throughout the evening. \\
    \hline
    \end{tabular}
\end{center}
```

Without specifying width for last column:

|  |  |  |  |
| --- | --- | --- | --- |
| Day | Min Temp | Max Temp | Summary |
| Monday | 11C | 22C | A clear day with lots of sunshine. However, the strong breeze will bring down the temperatures. |
| Tuesday | 9C | 19C | Cloudy with rain, across many northern regions. Clear spells across most of Scotland and Northern Ireland, but rain reaching the far northwest. |
| Wednesday | 10C | 21C | Rain will still linger for the morning. Conditions will improve by early afternoon and continue throughout the evening. |

```
With width specified:
\begin{center}
    \begin{tabular}{ | l | l | l | p{5cm} |}
    \hline
    Day & Min Temp & Max Temp & Summary \\ \hline
    Monday & 11C & 22C & A clear day with lots of sunshine. 
    However, the strong breeze will bring down the temperatures. \\ \hline
    Tuesday & 9C & 19C & Cloudy with rain, across many northern regions. Clear spells
    across most of Scotland and Northern Ireland,
    but rain reaching the far northwest. \\ \hline
    Wednesday & 10C & 21C & Rain will still linger for the morning.
    Conditions will improve by early afternoon and continue
    throughout the evening. \\
    \hline
    \end{tabular}
\end{center}
```

With width specified:

|  |  |  |  |
| --- | --- | --- | --- |
| Day | Min Temp | Max Temp | Summary |
| Monday | 11C | 22C | A clear day with lots of sunshine. However, the strong breeze will bring down the temperatures. |
| Tuesday | 9C | 19C | Cloudy with rain, across many northern regions. Clear spells across most of Scotland and Northern Ireland, but rain reaching the far northwest. |
| Wednesday | 10C | 21C | Rain will still linger for the morning. Conditions will improve by early afternoon and continue throughout the evening. |

## Rows spanning multiple columns

The command for this looks like this:  
`\multicolumn{num_cols}{alignment}{contents}`.

`num_cols` is the number of subsequent columns to merge;  
`alignment` is either `l`, `c`, `r` .  
`contents` is simply the actual data you want to be contained within that cell.

A simple example:

```
\begin{tabular}{ |l|l| }
  \hline
  \multicolumn{2}{|c|}{Team sheet} \\
  \hline
  GK & Paul Robinson \\
  LB & Lucas Radebe \\
  DC & Michael Duberry \\
  DC & Dominic Matteo \\
  RB & Dider Domi \\
  MC & David Batty \\
  MC & Eirik Bakke \\
  MC & Jody Morris \\
  FW & Jamie McMaster \\
  ST & Alan Smith \\
  ST & Mark Viduka \\
  \hline
\end{tabular}
```

|  |  |
| --- | --- |
| Team sheet | |
| GK | Paul Robinson |
| LB | Lucas Radebe |
| DC | Michael Duberry |
| DC | Dominic Matteo |
| RB | Dider Domi |
| MC | David Batty |
| MC | Eirik Bakke |
| MC | Jody Morris |
| FW | Jamie McMaster |
| ST | Alan Smith |
| ST | Mark Viduka |

## Columns spanning multiple rows

This then provides the command needed for spanning rows:  
`\multirow{''num_rows''}{''width''}{''contents''}`.

The arguments are pretty simple to deduce (`*` for the width means the content’s natural width).

```
\begin{tabular}{ |l|l|l| }
\hline
\multicolumn{3}{ |c| }{Team sheet} \\
\hline
Goalkeeper & GK & Paul Robinson \\ \hline
\multirow{4}{*}{Defenders} & LB & Lucas Radebe \\
 & DC & Michael Duburry \\
 & DC & Dominic Matteo \\
 & RB & Didier Domi \\ \hline
\multirow{3}{*}{Midfielders} & MC & David Batty \\
 & MC & Eirik Bakke \\
 & MC & Jody Morris \\ \hline
Forward & FW & Jamie McMaster \\ \hline
\multirow{2}{*}{Strikers} & ST & Alan Smith \\
 & ST & Mark Viduka \\
\hline
\end{tabular}
```

|  |  |  |
| --- | --- | --- |
| Team sheet | | |
| Goalkeeper | GK | Paul Robinson |
| Defenders | LB | Lucas Radebe |
| DC | Michael Duburry |
| DC | Dominic Matteo |
| RB | Didier Domi |
| Midfielders | MC | David Batty |
| MC | Eirik Bakke |
| MC | Jody Morris |
| Forward | FW | Jamie McMaster |
| Strikers | ST | Alan Smith |
| ST | Mark Viduka |

## Spanning in both directions simultaneously

Here is a nontrivial example of how to use spanning in both directions simultaneously and have the borders of the cells drawn correctly:

```
\begin{tabular}{cc|c|c|c|c|l}
\cline{3-6}
& & \multicolumn{4}{ c| }{Primes} \\ \cline{3-6}
& & 2 & 3 & 5 & 7 \\ \cline{1-6}
\multicolumn{1}{ |c  }{\multirow{2}{*}{Powers} } &
\multicolumn{1}{ |c| }{504} & 3 & 2 & 0 & 1 &     \\ \cline{2-6}
\multicolumn{1}{ |c  }{}                        &
\multicolumn{1}{ |c| }{540} & 2 & 3 & 1 & 0 &     \\ \cline{1-6}
\multicolumn{1}{ |c  }{\multirow{2}{*}{Powers} } &
\multicolumn{1}{ |c| }{gcd} & 2 & 2 & 0 & 0 & min \\ \cline{2-6}
\multicolumn{1}{ |c  }{}                        &
\multicolumn{1}{ |c| }{lcm} & 3 & 3 & 1 & 1 & max \\ \cline{1-6}
\end{tabular}
```

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Primes | | | |  |
|  |  | 2 | 3 | 5 | 7 |  |
| Powers | 504 | 3 | 2 | 0 | 1 |  |
| 540 | 2 | 3 | 1 | 0 |  |
| Powers | gcd | 2 | 2 | 0 | 0 | min |
| lcm | 3 | 3 | 1 | 1 | max |

Here is another example exploiting the same ideas to make the familiar and popular “2x2” or double dichotomy:

```
\begin{tabular}{ r|c|c| }
\multicolumn{1}{r}{}
 &  \multicolumn{1}{c}{noninteractive}
 & \multicolumn{1}{c}{interactive} \\
\cline{2-3}
massively multiple & Library & University \\
\cline{2-3}
one-to-one & Book & Tutor \\
\cline{2-3}
\end{tabular}
```

|  |  |  |
| --- | --- | --- |
|  | noninteractive | interactive |
| massively multiple | Library | University |
| one-to-one | Book | Tutor |

## Positioning tables

Positioning a table is easy if they’re inside a float table environment.

```
\begin{table}[h!]
\centering
\begin{tabular}{||c c c c||}
\hline
Col1 & Col2 & Col2 & Col3 \\ [0.5ex]
\hline\hline
1 & 6 & 87837 & 787 \\
2 & 7 & 78 & 5415 \\
3 & 545 & 778 & 7507 \\
4 & 545 & 18744 & 7560 \\
5 & 88 & 788 & 6344 \\ [1ex]
\hline
\end{tabular}
\end{table}
```

|  |  |  |  |
| --- | --- | --- | --- |
| Col1 | Col2 | Col2 | Col3 |
| 1 | 6 | 87837 | 787 |
| 2 | 7 | 78 | 5415 |
| 3 | 545 | 778 | 7507 |
| 4 | 545 | 18744 | 7560 |
| 5 | 88 | 788 | 6344 |

```
\begin{table}[h!]
\begin{left}
\begin{tabular}{||c c c c||}
\hline
Col1 & Col2 & Col2 & Col3 \\ [0.5ex]
\hline\hline
1 & 6 & 87837 & 787 \\
2 & 7 & 78 & 5415 \\
3 & 545 & 778 & 7507 \\
4 & 545 & 18744 & 7560 \\
5 & 88 & 788 & 6344 \\ [1ex]
\hline
\end{tabular}
\end{left}
\end{table}
```

|  |  |  |  |
| --- | --- | --- | --- |
| Col1 | Col2 | Col2 | Col3 |
| 1 | 6 | 87837 | 787 |
| 2 | 7 | 78 | 5415 |
| 3 | 545 | 778 | 7507 |
| 4 | 545 | 18744 | 7560 |
| 5 | 88 | 788 | 6344 |

## Captions, labels and references

Tables can be captioned, labelled and referenced by wrapping the `\tabular` environment inside of a `\table` environment.

`\caption` and `\label` commands must be added between `\begin{table}` and `\begin{tabular}` or between `\end{tabular}` and `\end{table}`.

By default, captions are left-aligned.

```
The table \ref{table:1} is an example of referenced \LaTeX elements.

\begin{table}[h!]
\centering
\begin{tabular}{||c c c c||}
\hline
Col1 & Col2 & Col2 & Col3 \\ [0.5ex]
\hline\hline
1 & 6 & 87837 & 787 \\
2 & 7 & 78 & 5415 \\
3 & 545 & 778 & 7507 \\
4 & 545 & 18744 & 7560 \\
5 & 88 & 788 & 6344 \\ [1ex]
\hline
\end{tabular}
\caption{Table to test captions and labels}
\label{table:1}
\end{table}
```

The table [1](#table%3A1) is an example of referenced \LaTeX elements.

|  |  |  |  |
| --- | --- | --- | --- |
| Col1 | Col2 | Col2 | Col3 |
| 1 | 6 | 87837 | 787 |
| 2 | 7 | 78 | 5415 |
| 3 | 545 | 778 | 7507 |
| 4 | 545 | 18744 | 7560 |
| 5 | 88 | 788 | 6344 |

Table 1: Table to test captions and labels

There are three important commands in the example:

`\caption{Table to test captions and labels}`  
As you may expect this command sets the caption for the table, if you create a list of tables this caption will be used there. You can place it above or below the table.

`\label{table:1}`  
If you need to refer the table within your document, set a label with this command. The label will number the table, and combined with the `\ref` command will allow you to reference it.

`\ref{table:1}`  
This code will be substituted by the number corresponding to the referenced table.

## Center-aligning captions

To center-align caption and remove the label prefix (like “Table 1.”), use the `\captionsetup` command with these options:

```
\captionsetup{labelformat=empty, singlelinecheck=true}
```

* `labelformat=empty` — hides automatic labels like “Table 1.”;
* `singlelinecheck=true` — ensures the caption is centered.

```
\begin{table}
\begin{tabular}{ | l | c | r | }
\hline
1 & 2 & 3 \\\hline
4 & 5 & 6 \\\hline
7 & 8 & 9 \\\hline
\end{tabular}
\captionsetup{labelformat=empty, singlelinecheck=true}
\caption{The caption should be center aligned.}
\end{table}
```

|  |  |  |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

The caption should be center aligned.

## More examples

```
\begin{table}[h]
\centering
\begin{tabular}{|c||c|c|} \hline
& A & B \\ \hline\hline
Foo &
\begin{tabular}{c} 1 \\ 2 \\ 3 \\ 4 \\
\end{tabular} &
\begin{tabular}{c} 2 \\ 5 \\ 9 \\ 8 \\
\end{tabular} \\ \hline
Bar &
\begin{tabular}{c} 1 \\ 2 \\ 3 \\ 4 \\
\end{tabular} &
\begin{tabular}{c} 31 \\ 23 \\ 16 \\ 42 \\
\end{tabular} \\ \hline
\end{tabular}
\caption{this is the table!}
\label{table:4}
\end{table}
```

|  |  |  |
| --- | --- | --- |
|  | A | B |
| Foo | |  | | --- | | 1 | | 2 | | 3 | | 4 | | |  | | --- | | 2 | | 5 | | 9 | | 8 | |
| Bar | |  | | --- | | 1 | | 2 | | 3 | | 4 | | |  | | --- | | 31 | | 23 | | 16 | | 42 | |

Table 3: this is the table!

```
\begin{table}[h]
\centering
\begin{tabular}{ :c|c|c: }
 \multicolumn{3}{|c|}{My cells2}\\
 \hline
 \multirow{3}{4em}{Multiple rows} & cell2 & cell3 \\\hline
 & cell5 & cell6 \\ \hline
 & cell8 & cell9 \\
 \hhline
\end{tabular}
\caption{this is the table!}
\label{table:5}
\end{table}
```

|  |  |  |
| --- | --- | --- |
| My cells2 | | |
| Multiple rows | cell2 | cell3 |
| cell5 | cell6 |
| cell8 | cell9 |

Table 4: this is the table!

```
\begin{table}[h]
\centering
\begin{tabular}{ ||c: c|| c||: }
\hhline
  {\(cell^1\)} & dd$$\frac{\nabla^{2} A}{A}=-k^{2}$$ dd & {cell3} \\ \hdashline
  {\(cell^4\)} & {cell5} & \(cell^6\) \\  \hline\hline
  cell7 & {cell $f^f$ 8} & cell9\\\hhline   
\end{tabular}
\caption{this is the table!}
\label{table:6}
\end{table}
```

|  |  |  |
| --- | --- | --- |
| c e l  l 1 c e l  l 1 cell^(1)cell^1cell1 | dd    ∇  2 A A = −  k  2  ∇  2 A A = −  k  2 (grad^(2)A)/(A)=-k^(2)\frac{\nabla^{2} A}{A}=-k^{2}∇2AA=−k2 dd | cell3 |
| c e l  l 4 c e l  l 4 cell^(4)cell^4cell4 | cell5 | c e l  l 6 c e l  l 6 cell^(6)cell^6cell6 |
| cell7 | cell   f f  f f f^(f)f^fff 8 | cell9 |

Table 5: this is the table!

```
\begin{table}[h]
\centering
\begin{tabular}{ |c|c|c| }
\hhline
{ formula $\frac{\nabla^{2} A}{A}=-k^{2}$} & cell2 & cell3 \\
 \hline
\end{tabular}
\caption{this is the table!}
\label{table:7}
\end{table}
```

|  |  |  |
| --- | --- | --- |
| formula     ∇  2 A A = −  k  2  ∇  2 A A = −  k  2 (grad^(2)A)/(A)=-k^(2)\frac{\nabla^{2} A}{A}=-k^{2}∇2AA=−k2 | cell2 | cell3 |

Table 6: this is the table!

```
\begin{table}[h]
\centering
\begin{tabular}{|l:l:l|}
\hline
1& \multirow{2}{5em}{\multicolumn{2}{:c:}{Day}}\\  \hline
1&2&3&4\\  \hline
1&2&3&4\\  \hline
\end{tabular}
\end{table}
```

|  |  |  |  |
| --- | --- | --- | --- |
| 1 | Day | |  |
| 1 | 4 |
| 1 | 2 | 3 | 4 |

```
\begin{table}[h]
\centering
\begin{tabular} {|||c|c|c|c|c|c|c|c|:::}
\hline \hhline {alms's} & \multicolumn{4}{|c|} {economizes} & {recondition} & {bailing} & {asymptotically} \\ \hline
\multicolumn{1}{|||c|} {fiddle} & \multicolumn{5}{|c|} {kitchenettes} & {misstates} \\ \hline
\end{tabular}
\caption{this is the table!}
\label{table:7}
\end{table}

Table \ref{table:4} is an example.
```

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alms's | economizes | | | | recondition | bailing | asymptotically |
| fiddle | kitchenettes | | | | | misstates |  |

Table 7: this is the table!

Table [3](#table%3A4) is an example.

[<   Syntax Reference](/docs/mathpix-markdown/syntax-reference)

[LaTeX Figure Syntax   >](/docs/mathpix-markdown/figures)