---
title:  Mathpix Markdown User Guide: LaTeX Style Figures
url: https://mathpix.com/docs/mathpix-markdown/figures
---

i

* [Docs](/docs)  >
* [Mathpix Markdown](/docs/mathpix-markdown/overview)  >
* [LaTeX Figure Syntax](figures)

* [LaTeX Style Figures](#latex-style-figures)
  + [Captions](#captions)
  + [Center-aligning captions](#center-aligning-captions)
  + [Labels](#labels)
  + [More examples](#more-examples)

# LaTeX Style Figures

To create a figure that floats, use the `figure` environment:

```
\begin{figure}[h]
\includegraphics[width=0.5\textwidth, center]{https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png}
\end{figure}
```

![](https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png)

The `\includegraphics[...]{...}` command is the one that actually included the image in the document.  
`[...]` contains image size and alignment information;  
`{...}` contains the file path/name (in our case it will contain the image URL)

`[width=..., height=..., left]` - contains image size and alignment information.

The default alignment for figures is center aligned.  
So, if it does not include alignment information, the figure is center aligned (see example below).  
If the figure should be left aligned, use `[width=..., left]`, if it should be right aligned, use `[width=..., right]` (see examples below)

The default size for images is `[width=0.5\textwidth]` - this means the width of the image will be half the width of the text area, not the page (so not including margin space). Also it supports `pt`, `px`, `in` …

Simplest figure syntax:

```
\begin{figure}
\includegraphics{https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png}
\end{figure}
```

![](https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png)

Same figure, left aligned:

```
\begin{figure}
\includegraphics[width=0.5\textwidth, left]{https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png}
\end{figure}
```

![](https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png)

Same figure, right aligned:

```
\begin{figure}
\includegraphics[width=0.5\textwidth, right]{https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png}
\end{figure}
```

![](https://cdn.mathpix.com/snip/images/MJT22mwBq-bwqrOYwhrUrVKxO3Xcu4vyHSabfbG8my8.original.fullsize.png)

## Captions

It is always a good practice to add a caption to any figure or table. Fortunately, it is very easy in LaTeX. All you need to do is to use the `\caption{''text''}` command within the float environment. LaTeX will automatically keep track of numbering the figures, so you do not need to include this within the caption text.

The location of the caption is traditionally underneath the float. However, it is up to you to insert the caption command after the actual contents of the float (but still within the environment). If you place it before, then the caption will appear above the float.  
By default, captions are left-aligned.  
The following example demonstrates this effect:

```
\begin{figure}
\caption{The caption is at the top.}
\centering
\includegraphics[width=0.5\textwidth]{https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cappuccino_at_Sightglass_Coffee.jpg/1599px-Cappuccino_at_Sightglass_Coffee.jpg}
\end{figure}

\begin{figure}
\centering
\includegraphics[width=0.5\textwidth]{https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cappuccino_at_Sightglass_Coffee.jpg/1599px-Cappuccino_at_Sightglass_Coffee.jpg}}
\caption{The caption is at the bottom.}
\end{figure}

\begin{table}
\centering
\begin{tabular}{| l c r |}
\hline
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\hline
\end{tabular}
\caption{A simple table}
\end{table}

Notice how the tables and figures have independent counters.
```

Figure 1: The caption is at the top.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cappuccino_at_Sightglass_Coffee.jpg/1599px-Cappuccino_at_Sightglass_Coffee.jpg)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cappuccino_at_Sightglass_Coffee.jpg/1599px-Cappuccino_at_Sightglass_Coffee.jpg)

Figure 2: The caption is at the bottom.

|  |  |  |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Table 1: A simple table

Notice that the tables and figures have independent counters.

## Center-aligning captions

To center-align caption and remove the label prefix (like “Figure 1.”), use the `\captionsetup` command with these options:

```
\captionsetup{labelformat=empty, singlelinecheck=true}
```

* `labelformat=empty` — hides automatic labels like “Figure 1.”;
* `singlelinecheck=true` — ensures the caption is centered.

```
\begin{figure}
\centering
\includegraphics[width=0.5\textwidth]{https://mathpix-ocr-examples.s3.amazonaws.com/graph.jpg}
\captionsetup{labelformat=empty, singlelinecheck=true}
\caption{The caption should be center aligned.}
\end{figure}
```

![](https://mathpix-ocr-examples.s3.amazonaws.com/graph.jpg)

The caption should be center aligned.

## Labels

Figures, just as many other elements in a LaTeX document (equations, tables) can be referenced within the text. It is very easy, just add a label to the figure environment, then later use that label to refer to the picture.

```
\begin{figure}[h]
\centering
\includegraphics[width=0.25\textwidth]{https://cdn.mathpix.com/snip/images/g1XhFj6GfjHL6KSxW6sPe3vISkV6qk6aCLaEDPbdVZM.original.fullsize.png}
\caption{a nice plot}
\label{fig:mesh1}
\end{figure}
 
As you can see in the figure \ref{fig:mesh1}
As you can see in the figure \ref{fig:NASA_Logo}.
```

![](https://cdn.mathpix.com/snip/images/g1XhFj6GfjHL6KSxW6sPe3vISkV6qk6aCLaEDPbdVZM.original.fullsize.png)

Figure 4: a nice plot

As you can see in the figure [4](#fig%3Amesh1).  
As you can see in the figure [6](#fig%3ANASA_Logo).

## More examples

```
\begin{figure}
\includegraphics[width=350px, height=70px, right]{https://cdn.mathpix.com/snip/images/-HM3WXo8kgdk8VtayBtn1_pJlgq9Cb7qV4JtM47Hgn0.original.fullsize.png}
\caption{Equation}
\label{fig:figure1}
\end{figure}
```

![](https://cdn.mathpix.com/snip/images/-HM3WXo8kgdk8VtayBtn1_pJlgq9Cb7qV4JtM47Hgn0.original.fullsize.png)

Figure 5: Equation

```
\begin{figure}[H]
\centering
\includegraphics[height=1in]{https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/725px-NASA_logo.svg.png}
\caption{Example LaTeX Figure} 
\label{fig:NASA_Logo}
\end{figure
```

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/725px-NASA_logo.svg.png)

Figure 6: Example LaTeX Figure

[<   LaTeX Table Syntax](/docs/mathpix-markdown/tables)

[LaTeX List Syntax   >](/docs/mathpix-markdown/lists)