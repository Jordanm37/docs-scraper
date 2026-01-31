---
title: Image to AsciiMath
url: https://mathpix.com/image-to-asciimath
---

# Image to AsciiMath

Mathpix has an image to AsciiMath converter which can extract AsciiMath code from a picture just by taking a screenshot.

Works on printed and handwritten images

Works on simple and complicated math

[Get Started](https://snip.mathpix.com)

## The best OCR software for math and science

Mathpix is the only equation to AsciiMath converter with high-accuracy OCR features developed specifically for scientific documents like research papers

### Simple Math

![Simple Equation]()

### Complex Math

![Complex Equation]()

### Handwritten Math

![Handwritten Equation]()

### Mixed Text and Math

![Mixed Text and Math]()

## How to convert images to AsciiMath on desktop

![An image showing image to AsciiMath conversion]()

1. Use Snip to take a screenshot of the image.

2. Check your Snip result and click on AsciiMath string to copy to clipboard.

3. Paste directly into your workspace.

[Get Started](https://snip.mathpix.com)

FOR STUDENTS

## Snip

Use Snip's screenshot and copy to clipboard functionality to instantly digitize printed and handwritten math and science notes into AsciiMath.

![Snip an equation on your screen and convert it to AsciiMath instantly.]()

![Details small]()

[Learn more](/)

FOR EDTECH COMPANIES

## Convert API

Mathpix provides image recognition for the biggest Edtech companies in the world.

Our image processing APIs are easy to implement and works on all platforms.

### API request

{
"src": "https://cdn.mathpix.com/snip/images/qjYbq5h8rFdzP\_81hT6WCrAd-rSsqneMMt4PjDzs0Uc.original.fullsize.png",
"formats": ["text", "data", "html"],
"data\_options": {
"include\_asciimath": true,
"include\_latex": true
}
}

![Example image]()

### API response:

{
"request\_id": "2022\_04\_23\_a1f81f67398c98caea3fg",
"is\_printed": false,
"is\_handwritten": true,
"auto\_rotate\_confidence": 0.000006675675649603363,
"auto\_rotate\_degrees": 0,
"confidence": 0.998046875,
"confidence\_rate": 0.998046875,
"text": "\\( -\\ln \\left(1-\\left(1-p^{-1}\\right)^{\\mu}\\right)-\\frac{\\ln p \\cdot \\mu\\left(1-p^{-1}\\right)^{\\mu-1} p^{-1}}{1-\\left(1-p^{-1}\\right)^{\\mu}} \\geq 0 \\)",
"html": "

\n-ln(1-(1-p^(-1))^(mu))-(ln p\*mu(1-p^(-1))^(mu-1)p^(-1))/(1-(1-p^(-1))^(mu)) >= 0-\\ln \\left(1-\\left(1-p^{-1}\\right)^{\\mu}\\right)-\\frac{\\ln p \\cdot \\mu\\left(1-p^{-1}\\right)^{\\mu-1} p^{-1}}{1-\\left(1-p^{-1}\\right)^{\\mu}} \\geq 0

\n",
"data": [
{
"type": "asciimath",
"value": "-ln(1-(1-p^(-1))^(mu))-(ln p\*mu(1-p^(-1))^(mu-1)p^(-1))/(1-(1-p^(-1))^(mu)) >= 0"
},
{
"type": "latex",
"value": "-\\ln \\left(1-\\left(1-p^{-1}\\right)^{\\mu}\\right)-\\frac{\\ln p \\cdot \\mu\\left(1-p^{-1}\\right)^{\\mu-1} p^{-1}}{1-\\left(1-p^{-1}\\right)^{\\mu}} \\geq 0"
}
]
}

![Rendered result]()

Our  [partners](/convert#customers) choose Mathpix over AWS Textract, Google Vision API, and Azure Computer Vision for converting images to AsciiMath.

[Learn more](/convert)