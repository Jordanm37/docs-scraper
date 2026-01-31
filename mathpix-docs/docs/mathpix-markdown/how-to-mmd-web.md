---
title:  Mathpix Markdown User Guide: Using MMD in a web browser
url: https://mathpix.com/docs/mathpix-markdown/how-to-mmd-web
---

* [Docs](/docs)  >
* [Mathpix Markdown](/docs/mathpix-markdown/overview)  >
* [Using MMD in a web browser](how-to-mmd-web)

# Using mathpix-markdown-it in web browsers

If you are loading mathpix-markdown-it from a CDN into a web page, there is no need to install anything. Simply use a script tag that loads mathpix-markdown-it from the CDN. E.g.,

```
  <script>
    let script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/npm/mathpix-markdown-it@1.0.40/es5/bundle.js";
    document.head.append(script);

    script.onload = function() {
      const isLoaded = window.loadMathJax();
      if (isLoaded) {
        console.log('Styles loaded!')
      }
    }
  </script>
```

## Example of mathpix-markdown-it usage in the web browsers

* [Example of render function usage](https://github.com/Mathpix/mathpix-markdown-it/blob/master/examples/html/content-mmd-to-html.html.md) ([View Demo](https://htmlpreview.github.io/?https://github.com/Mathpix/mathpix-markdown-it/blob/master/examples/html/content-mmd-to-html.html))
* [Example of markdownToHTML function usage](https://github.com/Mathpix/mathpix-markdown-it/blob/master/examples/html/input-mmd-to-html.html.md)([View Demo](https://htmlpreview.github.io/?https://github.com/Mathpix/mathpix-markdown-it/blob/master/examples/html/input-mmd-to-html.html))

[README](https://github.com/Mathpix/mathpix-markdown-it#using-mathpix-markdown-it-in-web-browsers)

[<   Using MMD with VS Code](/docs/mathpix-markdown/how-to-mmd-vscode)