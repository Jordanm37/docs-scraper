---
title:  Snip Solver
url: https://mathpix.com/docs/snip/snip-solver-capabilities
---

i

* [Docs](/docs)  >
* [Snip](/docs/snip/overview)  >
* [Try Examples!](try-examples)  >
* [Solver](snip-solver-capabilities)

* [Array](#array)
* [Integrals](#integrals)
* [Matrices](#matrices)
* [Generic](#generic)
* [Concrete](#concrete)
* [Relationals](#relationals)
* [Equation](#equation)
* [System of Equations](#system-of-equations)
* [Limits](#limits)
* [Function](#function)
* [Derivatives](#derivatives)
* [Elementary](#elementary)
* [Numericals](#numericals)

The solver takes in inputs in the form of 
L

A

T

E

X
L

A

T

E

X
L"A"T"E"X\LaTeXLATEX expressions and  
gives you an appropriate result based on the 
L

A

T

E

X
L

A

T

E

X
L"A"T"E"X\LaTeXLATEX query.

* Currently, the supported Result types are:
  + [Array](#array)
  + [Integrals](#integrals)
  + [Matrices](#matrices)
  + [Generic](#generic)
  + [Concrete](#concrete)
  + [Relationals](#relationals)
  + [Equation](#equation)
  + [System of Equations](#system-of-equations)
  + [Limits](#limits)
  + [Function](#function)
  + [Derivatives](#derivatives)
  + [Elementary](#elementary)
  + [Numericals](#numericals)

---

* Each Result contains a plethora of relevant subsections such as
  + Graphs
  + Numerical Results
  + Simplifications
  + Factorizations
  + Alternate Forms etc

---

* The subsections that are returned correspond to the query type.  
  Querying a Matrix would give you
  + Determinants
  + Eigenvectors
  + Eigenvalues
  + Inverses etc

**Examples of queries and their corresponding outputs are given below.**

# Array

---

* Input

  {

  x

  x
  ≥
  0

  (

  e

  x
  −
  1
  )

  x
  <
  0

  x
      

  x
  ≥
  0

  e

  x
  −
  1
      

  x
  <
  0
  {[x,x >= 0],[(e^(x)-1),x < 0]:}\left\{\begin{array}{ll} x & x \geq 0 \\ \left(e^{x}-1\right) & x<0 \end{array}\right.{xx≥0(ex−1)x<0

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/3aea5d3b74f5feca5a3b228c27e498aa.png)

---

# Integrals

---

* Input

  ∫

  x

  4
  +
  7

  x

  3
  +
  5
  x
  d
  x
  ∫

  x

  4
  +
  7

  x

  3
  +
  5
  x
  d
  x
  int(x^(4)+7)/(x^(3)+5x)dx\int \frac{x^{4}+7}{x^{3}+5 x} d x∫x4+7x3+5xdx

  ---

  + Result

  x

  2
  2
  +

  7
  ln
  ⁡

  (
  x
  )
  5
  −

  16
  ln
  ⁡

  (

  x

  2
  +
  5
  )
  5

  x

  2
  2
  +

  7
  ln
  ⁡

  x
  5
  −

  16
  ln
  ⁡

  x

  2
  +
  5
  5
  (x^(2))/(2)+(7ln ((x)))/(5)-(16 ln ((x^(2)+5)))/(5)\frac{x^{2}}{2} + \frac{7 \ln{\left(x \right)}}{5} - \frac{16 \ln{\left(x^{2} + 5 \right)}}{5}x22+7ln⁡(x)5−16ln⁡(x2+5)5

  ---

  + Simplification

  ∫

  x

  4
  +
  7

  x

  (

  x

  2
  +
  5
  )

  d
  x
  ∫

  x

  4
  +
  7

  x

  x

  2
  +
  5

  d
  x
  int(x^(4)+7)/(x(x^(2)+5))dx\int \frac{x^{4} + 7}{x \left(x^{2} + 5\right)}\, dx∫x4+7x(x2+5)dx

---

* Input

  ∫
  0
  1

  x
  2
  d
  x

  ∫
  0
  1

   

  x
  2
  d
  x
  int\_(0)^(1)x^(2)dx\int\_0^1 x^2 dx∫01x2dx

  ---

  + Result

  1
  3

  1
  3
  (1)/(3)\frac{1}{3}13

---

* Input

  ∫

  x

  2

  e

  −
  2
  x
  d
  x
  ∫

  x

  2

  e

  −
  2
  x
  d
  x
  intx^(2)e^(-2x)dx\int x^{2} e^{-2 x} d x∫x2e−2xdx

  ---

  + Result

  (
  −
  2

  x

  2
  −
  2
  x
  −
  1
  )

  e

  −
  2
  x
  4

  −
  2

  x

  2
  −
  2
  x
  −
  1

  e

  −
  2
  x
  4
  ((-2x^(2)-2x-1)e^(-2x))/(4)\frac{\left(- 2 x^{2} - 2 x - 1\right) e^{- 2 x}}{4}(−2x2−2x−1)e−2x4

---

* Input

  ∫
  8
  x

  e

  7
  x
  d
  x
  ∫
  8
  x

  e

  7
  x
  d
  x
  int8xe^(7x)dx\int 8 x e^{7 x} d x∫8xe7xdx

  ---

  + Result

  (
  56
  x
  −
  8
  )

  e

  7
  x
  49

  56
  x
  −
  8

  e

  7
  x
  49
  ((56 x-8)e^(7x))/(49)\frac{\left(56 x - 8\right) e^{7 x}}{49}(56x−8)e7x49

  ---

  + Simplification

  8

  (
  7
  x
  −
  1
  )

  e

  7
  x
  49

  8

  7
  x
  −
  1

  e

  7
  x
  49
  (8(7x-1)e^(7x))/(49)\frac{8 \left(7 x - 1\right) e^{7 x}}{49}8(7x−1)e7x49

---

* Input

  ∫

  x
  −
  3

  (
  x
  −
  1
  )
  (
  x
  −
  2
  )
  d
  x
  ∫

  x
  −
  3

  (
  x
  −
  1
  )
  (
  x
  −
  2
  )
  d
  x
  int(x-3)/((x-1)(x-2))dx\int \frac{x-3}{(x-1)(x-2)} d x∫x−3(x−1)(x−2)dx

  ---

  + Result

  −
  ln
  ⁡

  (
  x
  −
  2
  )
  +
  2
  ln
  ⁡

  (
  x
  −
  1
  )
  −
  ln
  ⁡

  x
  −
  2
  +
  2
  ln
  ⁡

  x
  −
  1
  -ln (x-2)+2ln (x-1)- \ln{\left(x - 2 \right)} + 2 \ln{\left(x - 1 \right)}−ln⁡(x−2)+2ln⁡(x−1)

  ---

  + Simplification

  ∫

  x
  −
  3

  (
  x
  −
  2
  )

  (
  x
  −
  1
  )

  d
  x
  ∫

  x
  −
  3

  x
  −
  2

  x
  −
  1

  d
  x
  int(x-3)/((x-2)(x-1))dx\int \frac{x - 3}{\left(x - 2\right) \left(x - 1\right)}\, dx∫x−3(x−2)(x−1)dx

---

* Input

  ∫

  x

  2
  −

  x

  2
  d
  x
  ∫

  x

  2
  −

  x

  2
  d
  x
  int(x)/(sqrt(2-x^(2)))dx\int \frac{x}{\sqrt{2-x^{2}}} d x∫x2−x2dx

  ---

  + Result

  −

  2
  −

  x

  2
  −

  2
  −

  x

  2
  -sqrt(2-x^(2))- \sqrt{2 - x^{2}}−2−x2

  ---

  + Simplification

  ∫

  x

  2
  −

  x

  2

  d
  x
  ∫

  x

  2
  −

  x

  2

  d
  x
  int(x)/(sqrt(2-x^(2)))dx\int \frac{x}{\sqrt{2 - x^{2}}}\, dx∫x2−x2dx

---

* Input

  ∫

  e

  x
  cos
  ⁡
  4
  x
  d
  x
  ∫

  e

  x
  cos
  ⁡
  4
  x
  d
  x
  inte^(x)cos 4xdx\int e^{x} \cos 4 x d x∫excos⁡4xdx

  ---

  + Result

  4

  e

  x
  sin
  ⁡

  (
  4
  x
  )
  17
  +

  e

  x
  cos
  ⁡

  (
  4
  x
  )
  17

  4

  e

  x
  sin
  ⁡

  4
  x
  17
  +

  e

  x
  cos
  ⁡

  4
  x
  17
  (4e^(x)sin ((4x)))/(17)+(e^(x)cos ((4x)))/(17)\frac{4 e^{x} \sin{\left(4 x \right)}}{17} + \frac{e^{x} \cos{\left(4 x \right)}}{17}4exsin⁡(4x)17+excos⁡(4x)17

---

* Input

  ∫

  0

  1

  ∫

  0

  1
  −

  x

  2

  ∫

  3

  4
  −

  x

  2
  −
  y
  x
  d
  z
  d
  y
  d
  x

  ∫

  0

  1

   

  ∫

  0

  1
  −

  x

  2

   

  ∫

  3

  4
  −

  x

  2
  −
  y

   
  x
  d
  z
  d
  y
  d
  x
  int\_(0)^(1)int\_(0)^(1-x^(2))int\_(3)^(4-x^(2)-y)xdzdydx\int\_{0}^{1} \int\_{0}^{1-x^{2}} \int\_{3}^{4-x^{2}-y} x d z d y d x∫01∫01−x2∫34−x2−yxdzdydx

  ---

  + Result

  1
  12

  1
  12
  (1)/(12)\frac{1}{12}112

  ---

  + Simplification

  ∫

  0

  1

  ∫

  0

  1
  −

  x

  2

  ∫

  3

  −

  x

  2
  −
  y
  +
  4
  x

  d
  z

  d
  y

  d
  x

  ∫

  0

  1

   

  ∫

  0

  1
  −

  x

  2

   

  ∫

  3

  −

  x

  2
  −
  y
  +
  4

   
  x

  d
  z

  d
  y

  d
  x
  int\_(0)^(1)int\_(0)^(1-x^(2))int\_(3)^(-x^(2)-y+4)xdzdydx\int\limits\_{0}^{1}\int\limits\_{0}^{1 - x^{2}}\int\limits\_{3}^{- x^{2} - y + 4} x\, dz\, dy\, dx∫01∫01−x2∫3−x2−y+4xdzdydx

---

* Input

  ∫

  e

  x

  1
  +

  e

  2
  x
  d
  x
  =
  ∫

  e

  x

  1
  +

  e

  2
  x
  d
  x
  =
  int(e^(x))/(1+e^(2x))dx=\int \frac{e^{x}}{1+e^{2 x}} d x=∫ex1+e2xdx=

  ---

  + Result

  tan

  −
  1
  ⁡

  (

  e

  x
  )

  tan

  −
  1
  ⁡

  e

  x
  tan^(-1)(e^(x))\tan^{-1}{\left(e^{x} \right)}tan−1⁡(ex)

  ---

  + Simplification

  ∫

  1

  2
  cosh
  ⁡

  (
  x
  )

  d
  x
  ∫

  1

  2
  cosh
  ⁡

  x

  d
  x
  int(1)/(2cosh ((x)))dx\int \frac{1}{2 \cosh{\left(x \right)}}\, dx∫12cosh⁡(x)dx

---

* Input

  ∫

  (

  4

  3
  y
  +

  3

  y

  2
  −

  2

  y
  7
  )
  d
  y
  ∫

  4

  3
  y
  +

  3

  y

  2
  −

  2

  y
  7
  d
  y
  int((4)/(3y)+(3)/(y^(2))-(2)/(root(7)(y)))dy\int\left(\frac{4}{3 y}+\frac{3}{y^{2}}-\frac{2}{\sqrt[7]{y}}\right) d y∫(43y+3y2−2y7)dy

  ---

  + Result

  −

  7

  y

  6
  7
  3
  +

  4
  ln
  ⁡

  (
  y
  )
  3
  −

  3
  y
  −

  7

  y

  6
  7
  3
  +

  4
  ln
  ⁡

  y
  3
  −

  3
  y
  -(7y^((6)/(7)))/(3)+(4ln ((y)))/(3)-(3)/(y)- \frac{7 y^{\frac{6}{7}}}{3} + \frac{4 \ln{\left(y \right)}}{3} - \frac{3}{y}−7y673+4ln⁡(y)3−3y

  ---

  + Simplification

  ∫

  (

  4

  3
  y
  +

  3

  y

  2
  −

  2

  y
  7
  )

  d
  y
  ∫

  4

  3
  y
  +

  3

  y

  2
  −

  2

  y
  7

  d
  y
  int((4)/(3y)+(3)/(y^(2))-(2)/(root(7)(y)))dy\int \left(\frac{4}{3 y} + \frac{3}{y^{2}} - \frac{2}{\sqrt[7]{y}}\right)\, dy∫(43y+3y2−2y7)dy

---

* Input

  ∫

  1

  5
  1
  +

  1
  u
  +

  1

  u

  2
  d
  u

  ∫

  1

  5

   
  1
  +

  1
  u
  +

  1

  u

  2
  d
  u
  int\_(1)^(5)1+(1)/(u)+(1)/(u^(2))du\int\_{1}^{5} 1+\frac{1}{u}+\frac{1}{u^{2}} d u∫151+1u+1u2du

  ---

  + Result

  ln
  ⁡

  (
  5
  )
  +

  24
  5
  ln
  ⁡

  5
  +

  24
  5
  ln (5)+(24)/(5)\ln{\left(5 \right)} + \frac{24}{5}ln⁡(5)+245

---

* Input

  ∫

  (
  −
  8

  e

  t
  +
  19
  t
  )
  d
  t
  ∫

  −
  8

  e

  t
  +
  19
  t
  d
  t
  int(-8e^(t)+19 t)dt\int\left(-8 e^{t}+19 t\right) d t∫(−8et+19t)dt

  ---

  + Result

  19

  t

  2
  2
  −
  8

  e

  t

  19

  t

  2
  2
  −
  8

  e

  t
  (19t^(2))/(2)-8e^(t)\frac{19 t^{2}}{2} - 8 e^{t}19t22−8et

---

* Input

  ∫

  e

  3
  x
  +
  9
  d
  x
  ∫

  e

  3
  x
  +
  9
  d
  x
  inte^(3x+9)dx\int e^{3 x+9} d x∫e3x+9dx

  ---

  + Result

  e

  3
  x
  +
  9
  3

  e

  3
  x
  +
  9
  3
  (e^(3x+9))/(3)\frac{e^{3 x + 9}}{3}e3x+93

---

# Matrices

---

* Input

  [

  −
  1

  7

  3

  7
  ]

  [

  −
  1

  7

  3

  7
  ]

  −
  1

  7

  3

  7

  −
  1
      

  7

  3
      

  7
  [[-1,7],[3,7]][[-1,7],[3,7]]\left[\begin{array}{cc}-1 & 7 \\ 3 & 7\end{array}\right]\left[\begin{array}{rr}-1 & 7 \\ 3 & 7\end{array}\right][−1737][−1737]

  ---

  + Result

  [

  22

  42

  18

  70
  ]

  22

  42

  18

  70
  [[22,42],[18,70]]\left[\begin{matrix}22 & 42\\18 & 70\end{matrix}\right][22421870]

  ---

  + Inverse

  [

  5
  56

  −

  3
  56

  −

  9
  392

  11
  392
  ]

  5
  56

  −

  3
  56

  −

  9
  392

  11
  392
  [[(5)/(56),-(3)/(56)],[-(9)/(392),(11)/(392)]]\left[\begin{matrix}\frac{5}{56} & - \frac{3}{56}\\- \frac{9}{392} & \frac{11}{392}\end{matrix}\right][556−356−939211392]

  ---

  + Determinant

  784
  784
  784784784

  ---

  + Eigenvectors

  {

  v

  λ
  1
  =

  [

  −

  42

  −
  24
  +
  6

  37

  1
  ]

  v

  λ
  2
  =

  [

  −

  42

  −
  6

  37
  −
  24

  1
  ]

  v

  λ
  1
  =

  −

  42

  −
  24
  +
  6

  37

  1

  v

  λ
  2
  =

  −

  42

  −
  6

  37
  −
  24

  1
  {[v\_(lambda\_(1))=[[-(42)/(-24+6sqrt37)],[1]]],[v\_(lambda\_(2))=[[-(42)/(-6sqrt37-24)],[1]]]:}\left\{ \begin{array} {l} \,v\_{\lambda\_1}=\left[\begin{matrix}- \frac{42}{-24 + 6 \sqrt{37}}\\1\end{matrix}\right] \\\,
  v\_{\lambda\_2}=\left[\begin{matrix}- \frac{42}{- 6 \sqrt{37} - 24}\\1\end{matrix}\right] \end{array} \right.{vλ1=[−42−24+6371]vλ2=[−42−637−241]

  ---

  + Eigenvalues

  {

  λ
  1
  =
  46
  −
  6

  37

  λ
  2
  =
  6

  37
  +
  46

  λ
  1
  =
  46
  −
  6

  37

  λ
  2
  =
  6

  37
  +
  46
  {[lambda\_(1)=46-6sqrt37],[lambda\_(2)=6sqrt37+46]:}\left\{ \begin{array} {l} \,\lambda\_1=46 - 6 \sqrt{37} \\\,
  \lambda\_2=6 \sqrt{37} + 46 \end{array} \right.{λ1=46−637λ2=637+46

  ---

  + Characteristic Polynomial

  p

  (
  λ
  )
  =

  λ

  2
  −
  92
  λ
  +
  784
  p

  λ
  =

  λ

  2
  −
  92
  λ
  +
  784
  p(lambda)=lambda^(2)-92 lambda+784p{\left(\lambda \right)} = \lambda^{2} - 92 \lambda + 784p(λ)=λ2−92λ+784

  ---

  + Dimensions

  (
  2
  ,
   
  2
  )

  2
  ,

  2
  (2,2)\left( 2, \ 2\right)(2, 2)

  ---

  + Multiplicities

  {

  μ
  A
  (

  λ
  1
  )
  =
  1

  μ
  A
  (

  λ
  2
  )
  =
  1

  μ
  A
  (

  λ
  1
  )
  =
  1

  μ
  A
  (

  λ
  2
  )
  =
  1
  {[mu \_(A)(lambda\_(1))=1],[mu \_(A)(lambda\_(2))=1]:}\left\{ \begin{array} {l} \,\mu\_A(\lambda\_1)=1 \\\,
  \mu\_A(\lambda\_2)=1 \end{array} \right.{μA(λ1)=1μA(λ2)=1

---

* Input

  [

  −
  3

  −
  5

  −
  3

  1

  3

  5
  ]
  +

  [

  3

  1

  0

  −
  2

  6

  −
  2
  ]

  −
  3
      

  −
  5
      

  −
  3

  1
      

  3
      

  5
  +

  3
      

  1
      

  0

  −
  2
      

  6
      

  −
  2
  [[-3,-5,-3],[1,3,5]]+[[3,1,0],[-2,6,-2]]\left[\begin{array}{rrr}-3 & -5 & -3 \\ 1 & 3 & 5\end{array}\right]+\left[\begin{array}{rrr}3 & 1 & 0 \\ -2 & 6 & -2\end{array}\right][−3−5−3135]+[310−26−2]

  ---

  + Result

  [

  0

  −
  4

  −
  3

  −
  1

  9

  3
  ]

  0

  −
  4

  −
  3

  −
  1

  9

  3
  [[0,-4,-3],[-1,9,3]]\left[\begin{matrix}0 & -4 & -3\\-1 & 9 & 3\end{matrix}\right][0−4−3−193]

---

* Input

  [

  4

  −
  5

  −
  6

  5

  −
  1

  4
  ]
  −

  [

  2

  −
  4

  −
  6

  2

  3

  −
  1
  ]

  4

  −
  5

  −
  6

  5

  −
  1

  4
  −

  2

  −
  4

  −
  6

  2

  3

  −
  1
  [[4,-5],[-6,5],[-1,4]]-[[2,-4],[-6,2],[3,-1]]\left[\begin{array}{cc}4 & -5 \\ -6 & 5 \\ -1 & 4\end{array}\right]-\left[\begin{array}{cc}2 & -4 \\ -6 & 2 \\ 3 & -1\end{array}\right][4−5−65−14]−[2−4−623−1]

  ---

  + Result

  [

  2

  −
  1

  0

  3

  −
  4

  5
  ]

  2

  −
  1

  0

  3

  −
  4

  5
  [[2,-1],[0,3],[-4,5]]\left[\begin{matrix}2 & -1\\0 & 3\\-4 & 5\end{matrix}\right][2−103−45]

---

* Input

  (

  cos
  ⁡
  θ

  sin
  ⁡
  θ

  −
  sin
  ⁡
  θ

  cos
  ⁡
  θ
  )

  cos
  ⁡
  θ

  sin
  ⁡
  θ

  −
  sin
  ⁡
  θ

  cos
  ⁡
  θ
  ([cos theta,sin theta],[-sin theta,cos theta])\left(\begin{array}{cc}
  \cos \theta & \sin \theta \\
  -\sin \theta & \cos \theta
  \end{array}\right)(cos⁡θsin⁡θ−sin⁡θcos⁡θ)

  ---

  + Result

  [

  cos
  ⁡

  (
  θ
  )

  sin
  ⁡

  (
  θ
  )

  −
  sin
  ⁡

  (
  θ
  )

  cos
  ⁡

  (
  θ
  )
  ]

  cos
  ⁡

  θ

  sin
  ⁡

  θ

  −
  sin
  ⁡

  θ

  cos
  ⁡

  θ
  [[cos (theta),sin (theta)],[-sin (theta),cos (theta)]]\left[\begin{matrix}\cos{\left(\theta \right)} & \sin{\left(\theta \right)}\\- \sin{\left(\theta \right)} & \cos{\left(\theta \right)}\end{matrix}\right][cos⁡(θ)sin⁡(θ)−sin⁡(θ)cos⁡(θ)]

  ---

  + Inverse

  [

  1
  −

  sin

  2
  ⁡

  (
  θ
  )

  cos
  ⁡

  (
  θ
  )

  −
  sin
  ⁡

  (
  θ
  )

  sin
  ⁡

  (
  θ
  )

  cos
  ⁡

  (
  θ
  )
  ]

  1
  −

  sin

  2
  ⁡

  θ

  cos
  ⁡

  θ

  −
  sin
  ⁡

  θ

  sin
  ⁡

  θ

  cos
  ⁡

  θ
  [[(1-sin^(2)((theta)))/(cos ((theta))),-sin (theta)],[sin (theta),cos (theta)]]\left[\begin{matrix}\frac{1 - \sin^{2}{\left(\theta \right)}}{\cos{\left(\theta \right)}} & - \sin{\left(\theta \right)}\\\sin{\left(\theta \right)} & \cos{\left(\theta \right)}\end{matrix}\right][1−sin2⁡(θ)cos⁡(θ)−sin⁡(θ)sin⁡(θ)cos⁡(θ)]

  ---

  + Determinant

  sin

  2
  ⁡

  (
  θ
  )
  +

  cos

  2
  ⁡

  (
  θ
  )

  sin

  2
  ⁡

  θ
  +

  cos

  2
  ⁡

  θ
  sin^(2)(theta)+cos^(2)(theta)\sin^{2}{\left(\theta \right)} + \cos^{2}{\left(\theta \right)}sin2⁡(θ)+cos2⁡(θ)

  ---

  + Eigenvectors

  {

  v

  λ
  1
  =

  [

  −

  sin
  ⁡

  (
  θ
  )

  (
  cos
  ⁡

  (
  θ
  )
  −
  1
  )

  (
  cos
  ⁡

  (
  θ
  )
  +
  1
  )

  1
  ]

  v

  λ
  2
  =

  [

  sin
  ⁡

  (
  θ
  )

  (
  cos
  ⁡

  (
  θ
  )
  −
  1
  )

  (
  cos
  ⁡

  (
  θ
  )
  +
  1
  )

  1
  ]

  v

  λ
  1
  =

  −

  sin
  ⁡

  θ

  cos
  ⁡

  θ
  −
  1

  cos
  ⁡

  θ
  +
  1

  1

  v

  λ
  2
  =

  sin
  ⁡

  θ

  cos
  ⁡

  θ
  −
  1

  cos
  ⁡

  θ
  +
  1

  1
  {[v\_(lambda\_(1))=[[-(sin ((theta)))/(sqrt((cos ((theta))-1)(cos ((theta))+1)))],[1]]],[v\_(lambda\_(2))=[[(sin ((theta)))/(sqrt((cos ((theta))-1)(cos ((theta))+1)))],[1]]]:}\left\{ \begin{array} {l} \,v\_{\lambda\_1}=\left[\begin{matrix}- \frac{\sin{\left(\theta \right)}}{\sqrt{\left(\cos{\left(\theta \right)} - 1\right) \left(\cos{\left(\theta \right)} + 1\right)}}\\1\end{matrix}\right] \\\,
  v\_{\lambda\_2}=\left[\begin{matrix}\frac{\sin{\left(\theta \right)}}{\sqrt{\left(\cos{\left(\theta \right)} - 1\right) \left(\cos{\left(\theta \right)} + 1\right)}}\\1\end{matrix}\right] \end{array} \right.{vλ1=[−sin⁡(θ)(cos⁡(θ)−1)(cos⁡(θ)+1)1]vλ2=[sin⁡(θ)(cos⁡(θ)−1)(cos⁡(θ)+1)1]

  ---

  + Eigenvalues

  {

  λ
  1
  =
  −

  (
  cos
  ⁡

  (
  θ
  )
  −
  1
  )

  (
  cos
  ⁡

  (
  θ
  )
  +
  1
  )
  +
  cos
  ⁡

  (
  θ
  )

  λ
  2
  =

  (
  cos
  ⁡

  (
  θ
  )
  −
  1
  )

  (
  cos
  ⁡

  (
  θ
  )
  +
  1
  )
  +
  cos
  ⁡

  (
  θ
  )

  λ
  1
  =
  −

  cos
  ⁡

  θ
  −
  1

  cos
  ⁡

  θ
  +
  1
  +
  cos
  ⁡

  θ

  λ
  2
  =

  cos
  ⁡

  θ
  −
  1

  cos
  ⁡

  θ
  +
  1
  +
  cos
  ⁡

  θ
  {[lambda\_(1)=-sqrt((cos ((theta))-1)(cos ((theta))+1))+cos (theta)],[lambda\_(2)=sqrt((cos ((theta))-1)(cos ((theta))+1))+cos (theta)]:}\left\{ \begin{array} {l} \,\lambda\_1=- \sqrt{\left(\cos{\left(\theta \right)} - 1\right) \left(\cos{\left(\theta \right)} + 1\right)} + \cos{\left(\theta \right)} \\\,
  \lambda\_2=\sqrt{\left(\cos{\left(\theta \right)} - 1\right) \left(\cos{\left(\theta \right)} + 1\right)} + \cos{\left(\theta \right)} \end{array} \right.{λ1=−(cos⁡(θ)−1)(cos⁡(θ)+1)+cos⁡(θ)λ2=(cos⁡(θ)−1)(cos⁡(θ)+1)+cos⁡(θ)

  ---

  + Characteristic Polynomial

  p

  (
  λ
  )
  =

  λ

  2
  −
  2
  λ
  cos
  ⁡

  (
  θ
  )
  +
  1
  p

  λ
  =

  λ

  2
  −
  2
  λ
  cos
  ⁡

  θ
  +
  1
  p(lambda)=lambda^(2)-2lambda cos (theta)+1p{\left(\lambda \right)} = \lambda^{2} - 2 \lambda \cos{\left(\theta \right)} + 1p(λ)=λ2−2λcos⁡(θ)+1

  ---

  + Dimensions

  (
  2
  ,
   
  2
  )

  2
  ,

  2
  (2,2)\left( 2, \ 2\right)(2, 2)

  ---

  + Multiplicities

  {

  μ
  A
  (

  λ
  1
  )
  =
  1

  μ
  A
  (

  λ
  2
  )
  =
  1

  μ
  A
  (

  λ
  1
  )
  =
  1

  μ
  A
  (

  λ
  2
  )
  =
  1
  {[mu \_(A)(lambda\_(1))=1],[mu \_(A)(lambda\_(2))=1]:}\left\{ \begin{array} {l} \,\mu\_A(\lambda\_1)=1 \\\,
  \mu\_A(\lambda\_2)=1 \end{array} \right.{μA(λ1)=1μA(λ2)=1

---

# Generic

---

* Input

  (
  −
  18

  m

  2
  n
  )

  2
  ∗

  (
  −

  1
  6
  m

  n

  2
  )
  =

  −
  18

  m

  2
  n

  2
  ∗

  −

  1
  6
  m

  n

  2
  =
  (-18m^(2)n)^(2)\*\*(-(1)/(6)mn^(2))=\left(-18 m^{2} n\right)^{2} \*\left(-\frac{1}{6} m n^{2}\right)=(−18m2n)2∗(−16mn2)=

  ---

  + Roots

  {

  m
  =
  0

  n
  =
  0

  m
  =
  0

  n
  =
  0
  {[m=0],[n=0]:}\left\{ \begin{array} {l} \,m = 0 \\\,
  n = 0 \end{array} \right.{m=0n=0

  ---

  + Result

  −
  54

  m

  5

  n

  4
  −
  54

  m

  5

  n

  4
  -54m^(5)n^(4)- 54 m^{5} n^{4}−54m5n4

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/5e6df4d1491441ffbe26214bfb058f1b.png)

---

* Input

  log

  6
  ⁡

  1
  6

  log

  6
  ⁡

  1
  6
  log\_(6)((1)/(6))\log \_{6} \frac{1}{6}log6⁡16

  ---

  + Result

  −
  1
  −
  1
  -1-1−1

---

* Input

  (
  −
  7
  +
  6
  i
  )
  (
  3
  +
  i
  )
  (
  −
  7
  +
  6
  i
  )
  (
  3
  +
  i
  )
  (-7+6i)(3+i)(-7+6 i)(3+i)(−7+6i)(3+i)

  ---

  + Result

  (
  −
  7
  +
  6
  i
  )

  (
  3
  +
  i
  )

  −
  7
  +
  6
  i

  3
  +
  i
  (-7+6i)(3+i)\left(-7 + 6 i\right) \left(3 + i\right)(−7+6i)(3+i)

  ---

  + Numerical

  −
  27.0
  +
  11.0
  i
  −
  27.0
  +
  11.0
  i
  -27.0+11.0 i-27.0 + 11.0 i−27.0+11.0i

  ---

  + Simplification

  −
  27
  +
  11
  i
  −
  27
  +
  11
  i
  -27+11 i-27 + 11 i−27+11i

---

* Input

  252

  q

  6

  k

  16

  175
  q

  k

  4

  252

  q

  6

  k

  16

  175
  q

  k

  4
  sqrt((252q^(6)k^(16))/(175 qk^(4)))\sqrt{\frac{252 q^{6} k^{16}}{175 q k^{4}}}252q6k16175qk4

  ---

  + Result

  6

  k

  12

  q

  5
  5

  6

  k

  12

  q

  5
  5
  (6sqrt(k^(12)q^(5)))/(5)\frac{6 \sqrt{k^{12} q^{5}}}{5}6k12q55

  ---

  + Expansion

  6

  7

  7

  k

  12

  q

  5
  35
  6

  7

  7

  k

  12

  q

  5
  35
  6sqrt7(sqrt7sqrt(k^(12)q^(5)))/(35)6 \sqrt{7} \frac{\sqrt{7} \sqrt{k^{12} q^{5}}}{35}677k12q535

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/9a4adaec77e4a7bedf94592cf4462749.png)

---

* Input

  160

  y

  10

  2

  y

  2

  160

  y

  10

  2

  y

  2
  (sqrt(160y^(10)))/(sqrt(2y^(2)))\frac{\sqrt{160 y^{10}}}{\sqrt{2 y^{2}}}160y102y2

  ---

  + Result

  4

  5

  y

  10

  y

  2

  4

  5

  y

  10

  y

  2
  (4sqrt5sqrt(y^(10)))/(sqrt(y^(2)))\frac{4 \sqrt{5} \sqrt{y^{10}}}{\sqrt{y^{2}}}45y10y2

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/7469c057962771993d26b53767dafdbb.png)

---

* Input

  z

  z

  2
  +
  9
  z
  +
  14
  +

  2

  z

  2
  +
  9
  z
  +
  14

  z

  z

  2
  +
  9
  z
  +
  14
  +

  2

  z

  2
  +
  9
  z
  +
  14
  (z)/(z^(2)+9z+14)+(2)/(z^(2)+9z+14)\frac{z}{z^{2}+9 z+14}+\frac{2}{z^{2}+9 z+14}zz2+9z+14+2z2+9z+14

  ---

  + Result

  z

  z

  2
  +
  9
  z
  +
  14
  +

  2

  z

  2
  +
  9
  z
  +
  14

  z

  z

  2
  +
  9
  z
  +
  14
  +

  2

  z

  2
  +
  9
  z
  +
  14
  (z)/(z^(2)+9z+14)+(2)/(z^(2)+9z+14)\frac{z}{z^{2} + 9 z + 14} + \frac{2}{z^{2} + 9 z + 14}zz2+9z+14+2z2+9z+14

  ---

  + Simplification

  1

  z
  +
  7

  1

  z
  +
  7
  (1)/(z+7)\frac{1}{z + 7}1z+7

  ---

  + Expansion

  z

  (

  z

  2
  +
  9
  z
  )
  +
  14
  +

  2

  (

  z

  2
  +
  9
  z
  )
  +
  14

  z

  z

  2
  +
  9
  z
  +
  14
  +

  2

  z

  2
  +
  9
  z
  +
  14
  (z)/((z^(2)+9z)+14)+(2)/((z^(2)+9z)+14)\frac{z}{\left(z^{2} + 9 z\right) + 14} + \frac{2}{\left(z^{2} + 9 z\right) + 14}z(z2+9z)+14+2(z2+9z)+14

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/4433b445942d511023627dda17aa76f4.png)

---

* Input

  14
  !

  (
  14
  −
  4
  )
  !

  14
  !

  (
  14
  −
  4
  )
  !
  (14!)/((14-4)!)\frac{14 !}{(14-4) !}14!(14−4)!

  ---

  + Factorization

  14
  !

  (
  −
  4
  +
  14
  )
  !

  14
  !

  −
  4
  +
  14
  !
  (14!)/((-4+14)!)\frac{14!}{\left(-4 + 14\right)!}14!(−4+14)!

  ---

  + Result

  24024
  24024
  240242402424024

---

* Input

  (
  5
  −
  9
  i
  )
  (
  5
  +
  9
  i
  )
  (
  5
  −
  9
  i
  )
  (
  5
  +
  9
  i
  )
  (5-9i)(5+9i)(5-9 i)(5+9 i)(5−9i)(5+9i)

  ---

  + Result

  (
  5
  −
  9
  i
  )

  (
  5
  +
  9
  i
  )

  5
  −
  9
  i

  5
  +
  9
  i
  (5-9i)(5+9i)\left(5 - 9 i\right) \left(5 + 9 i\right)(5−9i)(5+9i)

  ---

  + Numerical

  106.0
  106.0
  106.0106.0106.0

  ---

  + Simplification

  106
  106
  106106106

---

* Input

  125

  x

  3
  −
  216

  m

  3
  125

  x

  3
  −
  216

  m

  3
  125x^(3)-216m^(3)125 x^{3}-216 m^{3}125x3−216m3

  ---

  + Factorization

  (
  −
  6
  m
  +
  5
  x
  )

  (
  36

  m

  2
  +
  30
  m
  x
  +
  25

  x

  2
  )

  −
  6
  m
  +
  5
  x

  36

  m

  2
  +
  30
  m
  x
  +
  25

  x

  2
  (-6m+5x)(36m^(2)+30 mx+25x^(2))\left(- 6 m + 5 x\right) \left(36 m^{2} + 30 m x + 25 x^{2}\right)(−6m+5x)(36m2+30mx+25x2)

  ---

  + Roots

  {

  m
  =

  5
  x
  6

  ,

  m
  =
  x

  (
  −

  5
  12
  −

  5

  3
  i
  12
  )

  ,

  m
  =
  x

  (
  −

  5
  12
  +

  5

  3
  i
  12
  )

  x
  =

  6
  m
  5

  ,

  x
  =
  6
  m

  (
  −

  1
  10
  −

  3
  i
  10
  )

  ,

  x
  =
  6
  m

  (
  −

  1
  10
  +

  3
  i
  10
  )

  m
  =

  5
  x
  6

  ,

  m
  =
  x

  −

  5
  12
  −

  5

  3
  i
  12

  ,

  m
  =
  x

  −

  5
  12
  +

  5

  3
  i
  12

  x
  =

  6
  m
  5

  ,

  x
  =
  6
  m

  −

  1
  10
  −

  3
  i
  10

  ,

  x
  =
  6
  m

  −

  1
  10
  +

  3
  i
  10
  {[m=(5x)/(6)","quad m=x(-(5)/(12)-(5sqrt3i)/(12))","quad m=x(-(5)/(12)+(5sqrt3i)/(12))],[x=(6m)/(5)","quad x=6m(-(1)/(10)-(sqrt3i)/(10))","quad x=6m(-(1)/(10)+(sqrt3i)/(10))]:}\left\{ \begin{array} {l} \,m = \frac{5 x}{6}\,,\quad m = x \left(- \frac{5}{12} - \frac{5 \sqrt{3} i}{12}\right)\,,\quad m = x \left(- \frac{5}{12} + \frac{5 \sqrt{3} i}{12}\right) \\\,
  x = \frac{6 m}{5}\,,\quad x = 6 m \left(- \frac{1}{10} - \frac{\sqrt{3} i}{10}\right)\,,\quad x = 6 m \left(- \frac{1}{10} + \frac{\sqrt{3} i}{10}\right) \end{array} \right.{m=5x6,m=x(−512−53i12),m=x(−512+53i12)x=6m5,x=6m(−110−3i10),x=6m(−110+3i10)

  ---

  + Result

  −
  216

  m

  3
  +
  125

  x

  3
  −
  216

  m

  3
  +
  125

  x

  3
  -216m^(3)+125x^(3)- 216 m^{3} + 125 x^{3}−216m3+125x3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/01743e01902679b0845aeee693314963.png)

---

* Input

  (
  5
  +
  2
  i

  )

  2
  (
  5
  +
  2
  i

  )

  2
  (5+2i)^(2)(5+2 i)^{2}(5+2i)2

  ---

  + Result

  (
  5
  +
  2
  i
  )

  2

  5
  +
  2
  i

  2
  (5+2i)^(2)\left(5 + 2 i\right)^{2}(5+2i)2

  ---

  + Numerical

  21.0
  +
  20.0
  i
  21.0
  +
  20.0
  i
  21.0+20.0 i21.0 + 20.0 i21.0+20.0i

  ---

  + Simplification

  21
  +
  20
  i
  21
  +
  20
  i
  21+20 i21 + 20 i21+20i

---

* Input

  x

  2
  +
  3
  x
  −
  18

  x

  2
  +
  3
  x
  −
  18
  x^(2)+3x-18x^{2}+3 x-18x2+3x−18

  ---

  + Factorization

  (
  x
  −
  3
  )

  (
  x
  +
  6
  )

  x
  −
  3

  x
  +
  6
  (x-3)(x+6)\left(x - 3\right) \left(x + 6\right)(x−3)(x+6)

  ---

  + Roots

  x
  ∈

  {
  −
  6
  ,

  3
  }
  x
  ∈

  −
  6
  ,

  3
  x in{-6,3}x \in \left\{ -6,\, 3\right\}x∈{−6,3}

  ---

  + Result

  x

  2
  +
  3
  x
  −
  18

  x

  2
  +
  3
  x
  −
  18
  x^(2)+3x-18x^{2} + 3 x - 18x2+3x−18

  ---

  + Expansion

  (

  x

  2
  +
  3
  x
  )
  −
  18

  x

  2
  +
  3
  x
  −
  18
  (x^(2)+3x)-18\left(x^{2} + 3 x\right) - 18(x2+3x)−18

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/3bcafc3ffdd54f1eb4ccd229cf5261cf.png)

---

* Input

  2

  cos

  2
  ⁡

  (

  44

  ∘
  )
  −
  1
  2

  cos

  2
  ⁡

  44

  ∘
  −
  1
  2cos^(2)(44^(@))-12 \cos ^{2}\left(44^{\circ}\right)-12cos2⁡(44∘)−1

  ---

  + Result

  −
  1
  +
  2

  cos

  2
  ⁡

  (

  11
  π
  45
  )
  −
  1
  +
  2

  cos

  2
  ⁡

  11
  π
  45
  -1+2cos^(2)((11 pi)/(45))-1 + 2 \cos^{2}{\left(\frac{11 \pi}{45} \right)}−1+2cos2⁡(11π45)

  ---

  + Numerical

  0.034899496702501
  0.034899496702501
  0.0348994967025010.0348994967025010.034899496702501

  ---

  + Simplification

  cos
  ⁡

  (

  22
  π
  45
  )
  cos
  ⁡

  22
  π
  45
  cos ((22 pi)/(45))\cos{\left(\frac{22 \pi}{45} \right)}cos⁡(22π45)

---

* Input

  (
  −
  18
  )
  ÷
  6
  ×
  (
  −
  12
  )
  =
  (
  −
  18
  )
  ÷
  6
  ×
  (
  −
  12
  )
  =
  (-18)-:6xx(-12)=(-18) \div 6 \times(-12)=(−18)÷6×(−12)=

  ---

  + Result

  36
  36
  363636

---

* Input

  ln
  ⁡

  (

  e

  5
  6
  )
  ln
  ⁡

  e

  5
  6
  ln((e^(5))/(6))\ln \left(\frac{e^{5}}{6}\right)ln⁡(e56)

  ---

  + Result

  ln
  ⁡

  (

  e

  5
  6
  )
  ln
  ⁡

  e

  5
  6
  ln ((e^(5))/(6))\ln{\left(\frac{e^{5}}{6} \right)}ln⁡(e56)

  ---

  + Numerical

  3.20824053077195
  3.20824053077195
  3.208240530771953.208240530771953.20824053077195

  ---

  + Simplification

  5
  −
  ln
  ⁡

  (
  6
  )
  5
  −
  ln
  ⁡

  6
  5-ln (6)5 - \ln{\left(6 \right)}5−ln⁡(6)

---

* Input

  a
  2
  +

  b
  2
  +
  2
  a
  b

  a
  2
  +

  b
  2
  +
  2
  a
  b
  a^(2)+b^(2)+2aba^2 + b^2 + 2 a ba2+b2+2ab

  ---

  + Factorization

  (
  a
  +
  b
  )

  2

  a
  +
  b

  2
  (a+b)^(2)\left(a + b\right)^{2}(a+b)2

  ---

  + Roots

  {

  a
  =
  −
  b

  b
  =
  −
  a

  a
  =
  −
  b

  b
  =
  −
  a
  {[a=-b],[b=-a]:}\left\{ \begin{array} {l} \,a = - b \\\,
  b = - a \end{array} \right.{a=−bb=−a

  ---

  + Result

  a

  2
  +
  2
  a
  b
  +

  b

  2

  a

  2
  +
  2
  a
  b
  +

  b

  2
  a^(2)+2ab+b^(2)a^{2} + 2 a b + b^{2}a2+2ab+b2

  ---

  + Expansion

  2
  a
  b
  +

  (

  a

  2
  +

  b

  2
  )
  2
  a
  b
  +

  a

  2
  +

  b

  2
  2ab+(a^(2)+b^(2))2 a b + \left(a^{2} + b^{2}\right)2ab+(a2+b2)

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/ba43cb4caf2316c3cb9b35119295f460.png)

---

* Input

  (

  6
  5
  )

  4
  ×

  (

  6
  5
  )

  2
  =

  6
  5

  4
  ×

  6
  5

  2
  =
  ((6)/(5))^(4)xx((6)/(5))^(2)=\left(\frac{6}{5}\right)^{4} \times\left(\frac{6}{5}\right)^{2}=(65)4×(65)2=

  ---

  + Result

  46656
  15625

  46656
  15625
  (46656)/(15625)\frac{46656}{15625}4665615625

  ---

  + Numerical

  2.985984
  2.985984
  2.9859842.9859842.985984

---

* Input

  −

  1
  2
  +

  33
  2
  −

  1
  2
  +

  33
  2
  -(1)/(2)+(sqrt33)/(2)-\frac{1}{2}+\frac{\sqrt{33}}{2}−12+332

  ---

  + Factorization

  −
  1
  +

  33
  2

  −
  1
  +

  33
  2
  (-1+sqrt33)/(2)\frac{-1 + \sqrt{33}}{2}−1+332

  ---

  + Result

  −

  1
  2
  +

  33
  2
  −

  1
  2
  +

  33
  2
  -(1)/(2)+(sqrt33)/(2)- \frac{1}{2} + \frac{\sqrt{33}}{2}−12+332

  ---

  + Numerical

  2.37228132326901
  2.37228132326901
  2.372281323269012.372281323269012.37228132326901

---

* Input

  f
  (
  x
  )
  =

  2
  x

  3
  +
  x
  f
  (
  x
  )
  =

  2
  x

  3
  +
  x
  f(x)=(2x)/(3+x)f(x)=\frac{2 x}{3+x}f(x)=2x3+x

  ---

  + Roots

  x
  =
  0
  x
  =
  0
  x=0x = 0x=0

  ---

  + Result

  2
  x

  x
  +
  3

  2
  x

  x
  +
  3
  (2x)/(x+3)\frac{2 x}{x + 3}2xx+3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/fb9283ef5958a1d23bf1622ce013ecb2.png)

---

* Input

  −

  x

  2
  +
  14
  x
  −
  20
  −

  x

  2
  +
  14
  x
  −
  20
  -x^(2)+14 x-20-x^{2}+14 x-20−x2+14x−20

  ---

  + Roots

  x
  ∈

  {
  7
  −

  29
  ,

  29
  +
  7
  }
  x
  ∈

  7
  −

  29
  ,

  29
  +
  7
  x in{7-sqrt29,sqrt29+7}x \in \left\{ 7 - \sqrt{29},\, \sqrt{29} + 7\right\}x∈{7−29,29+7}

  ---

  + Result

  −

  x

  2
  +
  14
  x
  −
  20
  −

  x

  2
  +
  14
  x
  −
  20
  -x^(2)+14 x-20- x^{2} + 14 x - 20−x2+14x−20

  ---

  + Expansion

  (
  −

  x

  2
  +
  14
  x
  )
  −
  20

  −

  x

  2
  +
  14
  x
  −
  20
  (-x^(2)+14 x)-20\left(- x^{2} + 14 x\right) - 20(−x2+14x)−20

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/e45a051a727049c76f189291cbc11f3a.png)

---

* Input

  π
  4

  π
  4
  (pi)/(4)\frac{\pi}{4}π4

  ---

  + Numerical

  0.785398163397448
  0.785398163397448
  0.7853981633974480.7853981633974480.785398163397448

---

* Input

  2

  x

  2
  −
  18

  x

  4
  +
  2

  x

  3
  −
  3

  x

  2
  ⋅

  x

  2
  −
  11
  x
  +
  10

  x

  2
  −
  13
  x
  +
  30

  2

  x

  2
  −
  18

  x

  4
  +
  2

  x

  3
  −
  3

  x

  2
  ⋅

  x

  2
  −
  11
  x
  +
  10

  x

  2
  −
  13
  x
  +
  30
  (2x^(2)-18)/(x^(4)+2x^(3)-3x^(2))\*(x^(2)-11 x+10)/(x^(2)-13 x+30)\frac{2 x^{2}-18}{x^{4}+2 x^{3}-3 x^{2}} \cdot \frac{x^{2}-11 x+10}{x^{2}-13 x+30}2x2−18x4+2x3−3x2⋅x2−11x+10x2−13x+30

  ---

  + Result

  (
  2

  x

  2
  −
  18
  )

  (

  x

  2
  −
  11
  x
  +
  10
  )

  (

  x

  2
  −
  13
  x
  +
  30
  )

  (

  x

  4
  +
  2

  x

  3
  −
  3

  x

  2
  )

  2

  x

  2
  −
  18

  x

  2
  −
  11
  x
  +
  10

  x

  2
  −
  13
  x
  +
  30

  x

  4
  +
  2

  x

  3
  −
  3

  x

  2
  ((2x^(2)-18)(x^(2)-11 x+10))/((x^(2)-13 x+30)(x^(4)+2x^(3)-3x^(2)))\frac{\left(2 x^{2} - 18\right) \left(x^{2} - 11 x + 10\right)}{\left(x^{2} - 13 x + 30\right) \left(x^{4} + 2 x^{3} - 3 x^{2}\right)}(2x2−18)(x2−11x+10)(x2−13x+30)(x4+2x3−3x2)

  ---

  + Simplification

  2

  x

  2

  2

  x

  2
  (2)/(x^(2))\frac{2}{x^{2}}2x2

  ---

  + Expansion

  2

  x

  4

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  −

  22

  x

  3

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  +

  2

  x

  2

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  +

  198
  x

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  −

  180

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2

  2

  x

  4

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  −

  22

  x

  3

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  +

  2

  x

  2

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  +

  198
  x

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  −

  180

  x

  6
  −
  11

  x

  5
  +

  x

  4
  +
  99

  x

  3
  −
  90

  x

  2
  (2x^(4))/(x^(6)-11x^(5)+x^(4)+99x^(3)-90x^(2))-(22x^(3))/(x^(6)-11x^(5)+x^(4)+99x^(3)-90x^(2))+(2x^(2))/(x^(6)-11x^(5)+x^(4)+99x^(3)-90x^(2))+(198 x)/(x^(6)-11x^(5)+x^(4)+99x^(3)-90x^(2))-(180)/(x^(6)-11x^(5)+x^(4)+99x^(3)-90x^(2))\frac{2 x^{4}}{x^{6} - 11 x^{5} + x^{4} + 99 x^{3} - 90 x^{2}} - \frac{22 x^{3}}{x^{6} - 11 x^{5} + x^{4} + 99 x^{3} - 90 x^{2}} + \frac{2 x^{2}}{x^{6} - 11 x^{5} + x^{4} + 99 x^{3} - 90 x^{2}} + \frac{198 x}{x^{6} - 11 x^{5} + x^{4} + 99 x^{3} - 90 x^{2}} - \frac{180}{x^{6} - 11 x^{5} + x^{4} + 99 x^{3} - 90 x^{2}}2x4x6−11x5+x4+99x3−90x2−22x3x6−11x5+x4+99x3−90x2+2x2x6−11x5+x4+99x3−90x2+198xx6−11x5+x4+99x3−90x2−180x6−11x5+x4+99x3−90x2

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/b4534ed5e2b330e1f48c9940fd89232f.png)

---

* Input

  x
  2
  +

  y
  3

  x
  2
  +

  y
  3
  x^(2)+y^(3)x^2 + y^3x2+y3

  ---

  + Roots

  {

  x
  =
  −

  −

  y

  3

  ,

  x
  =

  −

  y

  3

  y
  =

  −

  x

  2
  3

  ,

  y
  =
  −

  −

  x

  2
  3
  2
  −

  3
  i

  −

  x

  2
  3
  2

  ,

  y
  =
  −

  −

  x

  2
  3
  2
  +

  3
  i

  −

  x

  2
  3
  2

  x
  =
  −

  −

  y

  3

  ,

  x
  =

  −

  y

  3

  y
  =

  −

  x

  2
  3

  ,

  y
  =
  −

  −

  x

  2
  3
  2
  −

  3
  i

  −

  x

  2
  3
  2

  ,

  y
  =
  −

  −

  x

  2
  3
  2
  +

  3
  i

  −

  x

  2
  3
  2
  {[x=-sqrt(-y^(3))","quad x=sqrt(-y^(3))],[y=root(3)(-x^(2))","quad y=-(root(3)(-x^(2)))/(2)-(sqrt3iroot(3)(-x^(2)))/(2)","quad y=-(root(3)(-x^(2)))/(2)+(sqrt3iroot(3)(-x^(2)))/(2)]:}\left\{ \begin{array} {l} \,x = - \sqrt{- y^{3}}\,,\quad x = \sqrt{- y^{3}} \\\,
  y = \sqrt[3]{- x^{2}}\,,\quad y = - \frac{\sqrt[3]{- x^{2}}}{2} - \frac{\sqrt{3} i \sqrt[3]{- x^{2}}}{2}\,,\quad y = - \frac{\sqrt[3]{- x^{2}}}{2} + \frac{\sqrt{3} i \sqrt[3]{- x^{2}}}{2} \end{array} \right.{x=−−y3,x=−y3y=−x23,y=−−x232−3i−x232,y=−−x232+3i−x232

  ---

  + Result

  x

  2
  +

  y

  3

  x

  2
  +

  y

  3
  x^(2)+y^(3)x^{2} + y^{3}x2+y3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/230dc4250405b6080951cdd652fc6cac.png)

---

* Input

  x
  2
  +

  y
  2

  x
  2
  +

  y
  2
  x^(2)+y^(2)x^2 + y^2x2+y2

  ---

  + Roots

  {

  x
  =
  −
  i
  y

  ,

  x
  =
  i
  y

  y
  =
  −
  i
  x

  ,

  y
  =
  i
  x

  x
  =
  −
  i
  y

  ,

  x
  =
  i
  y

  y
  =
  −
  i
  x

  ,

  y
  =
  i
  x
  {[x=-iy","quad x=iy],[y=-ix","quad y=ix]:}\left\{ \begin{array} {l} \,x = - i y\,,\quad x = i y \\\,
  y = - i x\,,\quad y = i x \end{array} \right.{x=−iy,x=iyy=−ix,y=ix

  ---

  + Result

  x

  2
  +

  y

  2

  x

  2
  +

  y

  2
  x^(2)+y^(2)x^{2} + y^{2}x2+y2

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/1a1519b10a419c5764d8db13a6423fdf.png)

---

* Input

  8

  /
  (
  2
  +
  360
  )
  8

  /
  (
  2
  +
  360
  )
  8//(2+360)8 / (2 + 360)8/(2+360)

  ---

  + Result

  4
  181

  4
  181
  (4)/(181)\frac{4}{181}4181

  ---

  + Numerical

  0.0220994475138122
  0.0220994475138122
  0.02209944751381220.02209944751381220.0220994475138122

  ---

  + Expansion

  8

  2
  +
  360

  8

  2
  +
  360
  (8)/(2+360)\frac{8}{2 + 360}82+360

---

* Input

  0.3
  ⋅

  10

  −
  2
  +
  0.8
  c

  1
  +

  0.3
  ⋅

  10

  −
  2
  ⋅
  0.8
  c

  c
  2

  0.3
  ⋅

  10

  −
  2
  +
  0.8
  c

  1
  +

  0.3
  ⋅

  10

  −
  2
  ⋅
  0.8
  c

  c
  2
  (0.3\*10^(-2)+0.8 c)/(1+(0.3\*10^(-2)\*0.8 c)/(c^(2)))\frac{0.3\cdot10^{-2} + 0.8c}{1 + \frac{0.3\cdot10^{-2}\cdot 0.8c}{c^2}}0.3⋅10−2+0.8c1+0.3⋅10−2⋅0.8cc2

  ---

  + Factorization

  0.8
  c

  (
  1.0
  c
  +
  0.00375
  )

  1.0
  c
  +
  0.0024

  0.8
  c

  1.0
  c
  +
  0.00375

  1.0
  c
  +
  0.0024
  (0.8 c(1.0 c+0.00375))/(1.0 c+0.0024)\frac{0.8 c \left(1.0 c + 0.00375\right)}{1.0 c + 0.0024}0.8c(1.0c+0.00375)1.0c+0.0024

  ---

  + Roots

  c
  =
  −
  0.00375
  c
  =
  −
  0.00375
  c=-0.00375c = -0.00375c=−0.00375

  ---

  + Result

  0.8
  c
  +
  0.003

  1
  +

  0.0024
  c

  0.8
  c
  +
  0.003

  1
  +

  0.0024
  c
  (0.8 c+0.003)/(1+(0.0024 )/(c))\frac{0.8 c + 0.003}{1 + \frac{0.0024}{c}}0.8c+0.0031+0.0024c

  ---

  + Simplification

  c

  (
  0.8
  c
  +
  0.003
  )

  c
  +
  0.0024

  c

  0.8
  c
  +
  0.003

  c
  +
  0.0024
  (c(0.8 c+0.003))/(c+0.0024)\frac{c \left(0.8 c + 0.003\right)}{c + 0.0024}c(0.8c+0.003)c+0.0024

  ---

  + Expansion

  0.8
  c

  1
  +

  0.0024
  c
  +

  0.003

  1
  +

  0.0024
  c

  0.8
  c

  1
  +

  0.0024
  c
  +

  0.003

  1
  +

  0.0024
  c
  (0.8 c)/(1+(0.0024 )/(c))+(0.003)/(1+(0.0024 )/(c))\frac{0.8 c}{1 + \frac{0.0024}{c}} + \frac{0.003}{1 + \frac{0.0024}{c}}0.8c1+0.0024c+0.0031+0.0024c

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/1b470d9d40e8cb6a42b2540202f5ea71.png)

---

* Input

  0.8
  c
  +
  0.3

  0.24
  c
  +
  1

  0.8
  c
  +
  0.3

  0.24
  c
  +
  1
  (0.8 c+0.3)/((0.24 )/(c)+1)\frac{0.8 c+0.3}{\frac{0.24}{c}+1}0.8c+0.30.24c+1

  ---

  + Factorization

  0.8
  c

  (
  1.0
  c
  +
  0.375
  )

  1.0
  c
  +
  0.24

  0.8
  c

  1.0
  c
  +
  0.375

  1.0
  c
  +
  0.24
  (0.8 c(1.0 c+0.375))/(1.0 c+0.24)\frac{0.8 c \left(1.0 c + 0.375\right)}{1.0 c + 0.24}0.8c(1.0c+0.375)1.0c+0.24

  ---

  + Roots

  c
  =
  −
  0.375
  c
  =
  −
  0.375
  c=-0.375c = -0.375c=−0.375

  ---

  + Result

  0.8
  c
  +
  0.3

  1
  +

  0.24
  c

  0.8
  c
  +
  0.3

  1
  +

  0.24
  c
  (0.8 c+0.3)/(1+(0.24 )/(c))\frac{0.8 c + 0.3}{1 + \frac{0.24}{c}}0.8c+0.31+0.24c

  ---

  + Simplification

  c

  (
  0.8
  c
  +
  0.3
  )

  c
  +
  0.24

  c

  0.8
  c
  +
  0.3

  c
  +
  0.24
  (c(0.8 c+0.3))/(c+0.24)\frac{c \left(0.8 c + 0.3\right)}{c + 0.24}c(0.8c+0.3)c+0.24

  ---

  + Expansion

  0.8
  c

  1
  +

  0.24
  c
  +

  0.3

  1
  +

  0.24
  c

  0.8
  c

  1
  +

  0.24
  c
  +

  0.3

  1
  +

  0.24
  c
  (0.8 c)/(1+(0.24 )/(c))+(0.3)/(1+(0.24 )/(c))\frac{0.8 c}{1 + \frac{0.24}{c}} + \frac{0.3}{1 + \frac{0.24}{c}}0.8c1+0.24c+0.31+0.24c

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/d474276c69ca46ee5ebc6d2aed856561.png)

---

* Input

  a
  2
  +

  b
  3

  a
  2
  +

  b
  3
  a^(2)+b^(3)a^2 + b^3a2+b3

  ---

  + Roots

  {

  a
  =
  −

  −

  b

  3

  ,

  a
  =

  −

  b

  3

  b
  =

  −

  a

  2
  3

  ,

  b
  =
  −

  −

  a

  2
  3
  2
  −

  3
  i

  −

  a

  2
  3
  2

  ,

  b
  =
  −

  −

  a

  2
  3
  2
  +

  3
  i

  −

  a

  2
  3
  2

  a
  =
  −

  −

  b

  3

  ,

  a
  =

  −

  b

  3

  b
  =

  −

  a

  2
  3

  ,

  b
  =
  −

  −

  a

  2
  3
  2
  −

  3
  i

  −

  a

  2
  3
  2

  ,

  b
  =
  −

  −

  a

  2
  3
  2
  +

  3
  i

  −

  a

  2
  3
  2
  {[a=-sqrt(-b^(3))","quad a=sqrt(-b^(3))],[b=root(3)(-a^(2))","quad b=-(root(3)(-a^(2)))/(2)-(sqrt3iroot(3)(-a^(2)))/(2)","quad b=-(root(3)(-a^(2)))/(2)+(sqrt3iroot(3)(-a^(2)))/(2)]:}\left\{ \begin{array} {l} \,a = - \sqrt{- b^{3}}\,,\quad a = \sqrt{- b^{3}} \\\,
  b = \sqrt[3]{- a^{2}}\,,\quad b = - \frac{\sqrt[3]{- a^{2}}}{2} - \frac{\sqrt{3} i \sqrt[3]{- a^{2}}}{2}\,,\quad b = - \frac{\sqrt[3]{- a^{2}}}{2} + \frac{\sqrt{3} i \sqrt[3]{- a^{2}}}{2} \end{array} \right.{a=−−b3,a=−b3b=−a23,b=−−a232−3i−a232,b=−−a232+3i−a232

  ---

  + Result

  a

  2
  +

  b

  3

  a

  2
  +

  b

  3
  a^(2)+b^(3)a^{2} + b^{3}a2+b3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/c72b58c6786558f64bbae762b557771f.png)

---

* Input

  sin
  ⁡
  (
  x
  )
  ×
  sin
  ⁡
  (
  y
  )
  sin
  ⁡
  (
  x
  )
  ×
  sin
  ⁡
  (
  y
  )
  sin(x)xx sin(y)\sin(x) \times \sin(y)sin⁡(x)×sin⁡(y)

  ---

  + Roots

  {

  x
  =
  0

  ,

  x
  =
  π

  y
  =
  0

  ,

  y
  =
  π

  x
  =
  0

  ,

  x
  =
  π

  y
  =
  0

  ,

  y
  =
  π
  {[x=0","quad x=pi],[y=0","quad y=pi]:}\left\{ \begin{array} {l} \,x = 0\,,\quad x = \pi \\\,
  y = 0\,,\quad y = \pi \end{array} \right.{x=0,x=πy=0,y=π

  ---

  + Result

  sin
  ⁡

  (
  x
  )
  sin
  ⁡

  (
  y
  )
  sin
  ⁡

  x
  sin
  ⁡

  y
  sin (x)sin (y)\sin{\left(x \right)} \sin{\left(y \right)}sin⁡(x)sin⁡(y)

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/0437974778ec07c246ca87cdcb2ffdc7.png)

---

* Input

  sin
  ⁡
  (
  x
  )
  ⋅
  sin
  ⁡
  (
  y
  )
  sin
  ⁡
  (
  x
  )
  ⋅
  sin
  ⁡
  (
  y
  )
  sin(x)\*sin(y)\sin (x) \cdot \sin (y)sin⁡(x)⋅sin⁡(y)

  ---

  + Roots

  {

  x
  =
  0

  ,

  x
  =
  π

  y
  =
  0

  ,

  y
  =
  π

  x
  =
  0

  ,

  x
  =
  π

  y
  =
  0

  ,

  y
  =
  π
  {[x=0","quad x=pi],[y=0","quad y=pi]:}\left\{ \begin{array} {l} \,x = 0\,,\quad x = \pi \\\,
  y = 0\,,\quad y = \pi \end{array} \right.{x=0,x=πy=0,y=π

  ---

  + Result

  sin
  ⁡

  (
  x
  )
  sin
  ⁡

  (
  y
  )
  sin
  ⁡

  x
  sin
  ⁡

  y
  sin (x)sin (y)\sin{\left(x \right)} \sin{\left(y \right)}sin⁡(x)sin⁡(y)

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/0437974778ec07c246ca87cdcb2ffdc7.png)

---

* Input

  x

  2

  x

  2
  x^(2)x^{2}x2

  ---

  + Roots

  x
  =
  0
  x
  =
  0
  x=0x = 0x=0

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/c36a6878f80a36706e7a176b7dc92d4f.png)

---

* Input

  x

  2

  /
  3
  +

  y

  2

  /
  3

  x

  2

  /
  3
  +

  y

  2

  /
  3
  x^(2//3)+y^(2//3)x^{2 / 3}+y^{2 / 3}x2/3+y2/3

  ---

  + Roots

  {

  x
  =
  −
  i
  y

  ,

  x
  =
  i
  y

  y
  =
  −
  i
  x

  ,

  y
  =
  i
  x

  x
  =
  −
  i
  y

  ,

  x
  =
  i
  y

  y
  =
  −
  i
  x

  ,

  y
  =
  i
  x
  {[x=-iy","quad x=iy],[y=-ix","quad y=ix]:}\left\{ \begin{array} {l} \,x = - i y\,,\quad x = i y \\\,
  y = - i x\,,\quad y = i x \end{array} \right.{x=−iy,x=iyy=−ix,y=ix

  ---

  + Result

  x

  2
  3
  +

  y

  2
  3

  x

  2
  3
  +

  y

  2
  3
  x^((2)/(3))+y^((2)/(3))x^{\frac{2}{3}} + y^{\frac{2}{3}}x23+y23

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/e324dc54931183a38851d5c8d265434f.png)

---

* Input

  f
  (
  x
  )
  =

  {

  x

  e

  2
  x

   si 

  x
  <
  0

  ln
  ⁡
  (
  x
  +
  1
  )

  x
  +
  1

   si 

  x
  ≥
  0

  f
  (
  x
  )
  =

  x

  e

  2
  x

   si 

  x
  <
  0

  ln
  ⁡
  (
  x
  +
  1
  )

  x
  +
  1

   si 

  x
  ≥
  0
  f(x)={[xe^(2x)," si ",x < 0],[(ln(x+1))/(x+1)," si ",x >= 0]:}f(x)=\left\{\begin{array}{ccc} x e^{2 x} & \text { si } & x<0 \\ \frac{\ln (x+1)}{x+1} & \text { si } & x \geq 0 \end{array}\right.f(x)={xe2x si x<0ln⁡(x+1)x+1 si x≥0

  ---

  + Roots

  x
  =
  0
  x
  =
  0
  x=0x = 0x=0

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/a5c4392db323b917b2551777ea9bfc72.png)

---

# Concrete

---

* Input

  ∑

  n
  =
  1

  7
  2
  (
  −
  2

  )

  n
  −
  1

  ∑

  n
  =
  1

  7

   
  2
  (
  −
  2

  )

  n
  −
  1
  sum\_(n=1)^(7)2(-2)^(n-1)\sum\_{n=1}^{7} 2(-2)^{n-1}∑n=172(−2)n−1

  ---

  + Result

  86
  86
  868686

  ---

  + Simplification

  −

  ∑

  n
  =
  1

  7

  (
  −
  1
  )

  n

  2

  n
  −

  ∑

  n
  =
  1

  7

   

  −
  1

  n

  2

  n
  -sum\_(n=1)^(7)(-1)^(n)2^(n)- \sum\_{n=1}^{7} \left(-1\right)^{n} 2^{n}−∑n=17(−1)n2n

---

# Relationals

---

* Input

  (
  u
  +
  5
  )
  (
  u
  +
  3
  )
  ≤
  −
  1
  (
  u
  +
  5
  )
  (
  u
  +
  3
  )
  ≤
  −
  1
  (u+5)(u+3) <= -1(u+5)(u+3) \leq-1(u+5)(u+3)≤−1

  ---

  + Solution

  u
  =
  −
  4
  u
  =
  −
  4
  u=-4u = -4u=−4

  ---

  + Simplification

  u

  2
  +
  8
  u
  ≤
  −
  16

  u

  2
  +
  8
  u
  ≤
  −
  16
  u^(2)+8u <= -16u^{2} + 8 u \leq -16u2+8u≤−16

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/0e1e386bec004be7258825da42aa9b79.png)

---

* Input

  x
  −
  y
  ≤
  10
  x
  −
  y
  ≤
  10
  x-y <= 10x - y \leq 10x−y≤10

  ---

  + Solution

  {

  x
  ≤
  y
  +
  10
  ∧
  −
  ∞
  <
  x

  y
  ≥
  x
  −
  10
  ∧
  y
  <
  ∞

  x
  ≤
  y
  +
  10
  ∧
  −
  ∞
  <
  x

  y
  ≥
  x
  −
  10
  ∧
  y
  <
  ∞
  {[x <= y+10^^-oo < x],[y >= x-10^^y < oo]:}\left\{ \begin{array} {l} \,x \leq y + 10 \wedge -\infty < x \\\,
  y \geq x - 10 \wedge y < \infty \end{array} \right.{x≤y+10∧−∞<xy≥x−10∧y<∞

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/0e9df5666cb904787400d13ee51e8fd8.png)

---

* Input

  x

  2
  +

  y

  3
  ≥
  4

  x

  2
  +

  y

  3
  ≥
  4
  x^(2)+y^(3) >= 4x^{2}+y^{3} \geq 4x2+y3≥4

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/0a80083a32f262241c30ad01fdaf2b4d.png)

---

* Input

  x
  4
  +

  y
  6
  ≤
  3

  x
  4
  +

  y
  6
  ≤
  3
  x^(4)+y^(6) <= 3x^4 + y^6 \leq 3x4+y6≤3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/7a96c9130752a370f3d4297556d35bd0.png)

---

* Input

  x
  2
  +

  y
  3
  ≤
  3

  x
  2
  +

  y
  3
  ≤
  3
  x^(2)+y^(3) <= 3x^2 + y^3 \leq 3x2+y3≤3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/c40f2586f9d5b03e2d8c1d10c971dbbc.png)

---

* Input

  x
  +
  y
  ≤
  10
  x
  +
  y
  ≤
  10
  x+y <= 10x + y \leq 10x+y≤10

  ---

  + Solution

  {

  x
  ≤
  10
  −
  y
  ∧
  −
  ∞
  <
  x

  y
  ≤
  10
  −
  x
  ∧
  −
  ∞
  <
  y

  x
  ≤
  10
  −
  y
  ∧
  −
  ∞
  <
  x

  y
  ≤
  10
  −
  x
  ∧
  −
  ∞
  <
  y
  {[x <= 10-y^^-oo < x],[y <= 10-x^^-oo < y]:}\left\{ \begin{array} {l} \,x \leq 10 - y \wedge -\infty < x \\\,
  y \leq 10 - x \wedge -\infty < y \end{array} \right.{x≤10−y∧−∞<xy≤10−x∧−∞<y

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/375f949b4ae9d9d1d93f466b1093281e.png)

---

* Input

  x
  2
  +

  y
  2
  ≤
  20

  x
  2
  +

  y
  2
  ≤
  20
  x^(2)+y^(2) <= 20x^2 + y^2 \leq 20x2+y2≤20

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/8ae658b238cbab93d101ea9a7e523f82.png)

---

* Input

  x

  2
  +

  y

  2
  ≤
  10

  x

  2
  +

  y

  2
  ≤
  10
  x^(2)+y^(2) <= 10x^{2}+y^{2} \leq 10x2+y2≤10

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/04345723a028955a7b2a68ecf7c5e02a.png)

---

* Input

  x

  2
  −

  y

  2
  ≤
  10

  x

  2
  −

  y

  2
  ≤
  10
  x^(2)-y^(2) <= 10x^{2}-y^{2} \leq 10x2−y2≤10

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/03043a375ac4628eabed2304e9635c77.png)

---

# Equation

---

* Input

  x

  2
  3
  −
  4

  x

  1
  3
  −
  5
  =
  0

  x

  2
  3
  −
  4

  x

  1
  3
  −
  5
  =
  0
  x^((2)/(3))-4x^((1)/(3))-5=0x^{\frac{2}{3}}-4 x^{\frac{1}{3}}-5=0x23−4x13−5=0

  ---

  + Solution

  x
  =
  125
  x
  =
  125
  x=125x = 125x=125

  ---

  + Simplification

  −

  x

  2
  3
  +
  4

  x
  3
  +
  5
  =
  0
  −

  x

  2
  3
  +
  4

  x
  3
  +
  5
  =
  0
  -x^((2)/(3))+4root(3)(x)+5=0- x^{\frac{2}{3}} + 4 \sqrt[3]{x} + 5 = 0−x23+4x3+5=0

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/5f81bbc322000f05db9aa4b005cca207.png)

---

* Input

  |

  x

  2

  6

  6

  x

  0

  5

  1

  −
  6
  |
  =
  108

  x

  2

  6

  6

  x

  0

  5

  1

  −
  6
  =
  108
  |[x,2,6],[6,x,0],[5,1,-6]|=108\left|\begin{array}{ccc}x & 2 & 6 \\ 6 & x & 0 \\ 5 & 1 & -6\end{array}\right|=108|x266x051−6|=108

  ---

  + Solution

  x
  ∈

  {
  −
  5
  ,

  0
  }
  x
  ∈

  −
  5
  ,

  0
  x in{-5,0}x \in \left\{ -5,\, 0\right\}x∈{−5,0}

  ---

  + Simplification

  x

  2
  +
  5
  x
  =
  0

  x

  2
  +
  5
  x
  =
  0
  x^(2)+5x=0x^{2} + 5 x = 0x2+5x=0

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/c94be54b6ae983af2684c2520ed867e5.png)

---

* Input

  x
  2
  +
  2
  x
  +
  1
  =
  0

  x
  2
  +
  2
  x
  +
  1
  =
  0
  x^(2)+2x+1=0x ^ 2 + 2 x + 1 = 0x2+2x+1=0

  ---

  + Solution

  x
  =
  −
  1
  x
  =
  −
  1
  x=-1x = -1x=−1

  ---

  + Simplification

  x

  2
  +
  2
  x
  =
  −
  1

  x

  2
  +
  2
  x
  =
  −
  1
  x^(2)+2x=-1x^{2} + 2 x = -1x2+2x=−1

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/6a3d97c21db6ab08169078109aaa5dcc.png)

---

* Input

  cot
  ⁡

  (

  180

  ∘
  −
  θ
  )
  =
  cot
  ⁡
  θ
  cot
  ⁡

  180

  ∘
  −
  θ
  =
  cot
  ⁡
  θ
  cot(180^(@)-theta)=cot theta\cot \left(180^{\circ}-\theta\right)=\cot \thetacot⁡(180∘−θ)=cot⁡θ

  ---

  + Solution

  θ
  =

  π
  2
  θ
  =

  π
  2
  theta=(pi)/(2)\theta = \frac{\pi}{2}θ=π2

  ---

  + Simplification

  cot
  ⁡

  (
  θ
  )
  =
  −
  cot
  ⁡

  (
  θ
  )
  cot
  ⁡

  θ
  =
  −
  cot
  ⁡

  θ
  cot (theta)=-cot (theta)\cot{\left(\theta \right)} = - \cot{\left(\theta \right)}cot⁡(θ)=−cot⁡(θ)

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/ad10a43806874bbbf14220bca2441fde.png)

---

* Input

  9

  x
  ⋅

  3

  x

  2
  =

  81

  2

  9

  x
  ⋅

  3

  x

  2
  =

  81

  2
  9^(x)\*3^(x^(2))=81^(2)9^{x} \cdot 3^{x^{2}}=81^{2}9x⋅3x2=812

  ---

  + Solution

  x
  ∈

  {
  −
  4
  ,

  2
  }
  x
  ∈

  −
  4
  ,

  2
  x in{-4,2}x \in \left\{ -4,\, 2\right\}x∈{−4,2}

  ---

  + Simplification

  3

  x

  (
  x
  +
  2
  )
  =
  6561

  3

  x

  x
  +
  2
  =
  6561
  3^(x(x+2))=65613^{x \left(x + 2\right)} = 65613x(x+2)=6561

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/5c0f03fd3cfe189b06b47e09333ed713.png)

---

* Input

  x
  +
  73
  =
  x
  +
  1

  x
  +
  73
  =
  x
  +
  1
  sqrt(x+73)=x+1\sqrt{x+73}=x+1x+73=x+1

  ---

  + Solution

  x
  =
  8
  x
  =
  8
  x=8x = 8x=8

  ---

  + Simplification

  x
  +
  1
  =

  x
  +
  73
  x
  +
  1
  =

  x
  +
  73
  x+1=sqrt(x+73)x + 1 = \sqrt{x + 73}x+1=x+73

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/296185a3ace097facf0229f3eae9633b.png)

---

* Input

  (

  5
  2

  )
  =
  2
  y

  (

  5
  2

  )
  =
  2
  y
  ((5)/(2))=2y\binom{5}{2} = 2 y(52)=2y

  ---

  + Solution

  y
  =
  5
  y
  =
  5
  y=5y = 5y=5

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/e9f522f69728a441f6cf057d9e54915f.png)

---

* Input

  ∫
  0
  1

  x
  2
  d
  x
  =
  2
  y

  ∫
  0
  1

   

  x
  2
  d
  x
  =
  2
  y
  int\_(0)^(1)x^(2)dx=2y\int\_0^1 x^2 dx = 2 y∫01x2dx=2y

  ---

  + Solution

  y
  =

  1
  6
  y
  =

  1
  6
  y=(1)/(6)y = \frac{1}{6}y=16

  ---

  + Simplification

  y
  =

  ∫

  0

  1

  x

  2

  d
  x
  2
  y
  =

  ∫

  0

  1

   

  x

  2

  d
  x
  2
  y=(int\_(0)^(1)x^(2)dx)/(2)y = \frac{\int\limits\_{0}^{1} x^{2}\, dx}{2}y=∫01x2dx2

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/4b8bc38bb7c65568ec4739269f87615c.png)

---

* Input

  5

  7
  x
  +
  2
  =

  2

  x
  −
  3

  5

  7
  x
  +
  2
  =

  2

  x
  −
  3
  5^(7x+2)=2^(x-3)5^{7 x+2}=2^{x-3}57x+2=2x−3

  ---

  + Solution

  x
  =
  ln
  ⁡

  (

  200

  1

  ln
  ⁡

  (

  2
  78125
  )
  )
  x
  =
  ln
  ⁡

  200

  1

  ln
  ⁡

  2
  78125
  x=ln (200^((1)/(ln (((2)/(78125))))))x = \ln{\left(200^{\frac{1}{\ln{\left(\frac{2}{78125} \right)}}} \right)}x=ln⁡(2001ln⁡(278125))

  ---

  + Simplification

  2

  x
  −
  3
  =

  5

  7
  x
  +
  2

  2

  x
  −
  3
  =

  5

  7
  x
  +
  2
  2^(x-3)=5^(7x+2)2^{x - 3} = 5^{7 x + 2}2x−3=57x+2

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/c88a8fa5fa285d5917523d382d9f2109.png)

---

* Input

  sin
  ⁡
  (
  4
  π
  x
  )
  =

  3
  2
  sin
  ⁡
  (
  4
  π
  x
  )
  =

  3
  2
  sin(4pi x)=(sqrt3)/(2)\sin (4 \pi x)=\frac{\sqrt{3}}{2}sin⁡(4πx)=32

  ---

  + Solution

  x
  ∈

  {

  1
  12
  ,

  1
  6
  }
  x
  ∈

  1
  12
  ,

  1
  6
  x in{(1)/(12),(1)/(6)}x \in \left\{ \frac{1}{12},\, \frac{1}{6}\right\}x∈{112,16}

  ---

  + Simplification

  sin
  ⁡

  (
  4
  π
  x
  )
  =

  3
  2
  sin
  ⁡

  4
  π
  x
  =

  3
  2
  sin (4pi x)=(sqrt3)/(2)\sin{\left(4 \pi x \right)} = \frac{\sqrt{3}}{2}sin⁡(4πx)=32

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/4a5e96006f5ddb61ffb09ced396c84ae.png)

---

* Input

  log

  x
  ⁡
  64
  =
  3

  log

  x
  ⁡
  64
  =
  3
  log\_(x)64=3\log \_{x} 64=3logx⁡64=3

  ---

  + Solution

  x
  =
  4
  x
  =
  4
  x=4x = 4x=4

  ---

  + Simplification

  log

  x
  ⁡

  (
  64
  )
  =
  3

  log

  x
  ⁡

  64
  =
  3
  log\_(x)(64)=3\log\_{x} {\left(64 \right)} = 3logx⁡(64)=3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/7a0e83bf0054f7dd5dcb7e959a755144.png)

---

* Input

  4
  −
  3
  x

  3
  x
  =
  2

  4
  −
  3
  x

  3
  x
  =
  2
  (sqrt(4-3x))/(sqrt(3x))=2\frac{\sqrt{4-3 x}}{\sqrt{3 x}}=24−3x3x=2

  ---

  + Solution

  x
  =

  4
  15
  x
  =

  4
  15
  x=(4)/(15)x = \frac{4}{15}x=415

  ---

  + Simplification

  12
  −
  9
  x

  3

  x
  =
  2

  12
  −
  9
  x

  3

  x
  =
  2
  (sqrt(12-9x))/(3sqrtx)=2\frac{\sqrt{12 - 9 x}}{3 \sqrt{x}} = 212−9x3x=2

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/3ba77158b9ade9329dfffa27f55b0b55.png)

---

* Input

  log

  49
  ⁡

  7
  3
  =
  x

  log

  49
  ⁡

  7
  3
  =
  x
  log\_(49)root(3)(7)=x\log \_{49} \sqrt[3]{7}=xlog49⁡73=x

  ---

  + Solution

  x
  =

  1
  6
  x
  =

  1
  6
  x=(1)/(6)x = \frac{1}{6}x=16

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/e705fae857048450dac2f885cbec3655.png)

---

* Input

  x
  2
  =
  4

  x
  2
  =
  4
  x^(2)=4x ^ 2 = 4x2=4

  ---

  + Solution

  x
  ∈

  {
  −
  2
  ,

  2
  }
  x
  ∈

  −
  2
  ,

  2
  x in{-2,2}x \in \left\{ -2,\, 2\right\}x∈{−2,2}

  ---

  + Simplification

  x

  2
  =
  4

  x

  2
  =
  4
  x^(2)=4x^{2} = 4x2=4

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/b4c29b38f648473e26c4a81a89c591cf.png)

---

* Input

  3
  4
  =
  3
  x

  3
  4
  =
  3
  x
  (3)/(4)=3x\frac{3}{4} = 3 x34=3x

  ---

  + Solution

  x
  =

  1
  4
  x
  =

  1
  4
  x=(1)/(4)x = \frac{1}{4}x=14

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/2aa72ab58d7cfa1d4b3a01d90d813651.png)

---

* Input

  3

  a
  +
  2
  +

  4

  a
  −
  1
  =
  0

  3

  a
  +
  2
  +

  4

  a
  −
  1
  =
  0
  (3)/(a+2)+(4)/(a-1)=0\frac{3}{a+2}+\frac{4}{a-1}=03a+2+4a−1=0

  ---

  + Solution

  a
  =
  −

  5
  7
  a
  =
  −

  5
  7
  a=-(5)/(7)a = - \frac{5}{7}a=−57

  ---

  + Simplification

  7
  a
  +
  5

  (
  a
  −
  1
  )

  (
  a
  +
  2
  )
  =
  0

  7
  a
  +
  5

  a
  −
  1

  a
  +
  2
  =
  0
  (7a+5)/((a-1)(a+2))=0\frac{7 a + 5}{\left(a - 1\right) \left(a + 2\right)} = 07a+5(a−1)(a+2)=0

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/5bf6a5a0f33735774e53247e2bef608b.png)

---

* Input

  y
  =

  2
  x

  3
  +
  x
  y
  =

  2
  x

  3
  +
  x
  y=(2x)/(3+x)y=\frac{2 x}{3+x}y=2x3+x

  ---

  + Solution

  {

  x
  =
  −

  3
  y

  y
  −
  2

  y
  =

  2
  x

  x
  +
  3

  x
  =
  −

  3
  y

  y
  −
  2

  y
  =

  2
  x

  x
  +
  3
  {[x=-(3y)/(y-2)],[y=(2x)/(x+3)]:}\left\{ \begin{array} {l} \,x = - \frac{3 y}{y - 2} \\\,
  y = \frac{2 x}{x + 3} \end{array} \right.{x=−3yy−2y=2xx+3

  ---

  + Simplification

  y
  =

  2
  x

  x
  +
  3
  y
  =

  2
  x

  x
  +
  3
  y=(2x)/(x+3)y = \frac{2 x}{x + 3}y=2xx+3

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/10c14fbb97abc824964b2c01f0750b64.png)

---

* Input

  x
  +
  y
  =
  10
  x
  +
  y
  =
  10
  x+y=10x + y = 10x+y=10

  ---

  + Solution

  {

  x
  =
  10
  −
  y

  y
  =
  10
  −
  x

  x
  =
  10
  −
  y

  y
  =
  10
  −
  x
  {[x=10-y],[y=10-x]:}\left\{ \begin{array} {l} \,x = 10 - y \\\,
  y = 10 - x \end{array} \right.{x=10−yy=10−x

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/323a840d4a252ef101904a65e3023dfe.png)

---

* Input

  y

  2
  +

  x

  2
  =

  z

  2

  y

  2
  +

  x

  2
  =

  z

  2
  y^(2)+x^(2)=z^(2)y^{2}+x^{2}=z^{2}y2+x2=z2

  ---

  + Solution

  {

  x
  =
  −

  −

  y

  2
  +

  z

  2

  ,

  x
  =

  −

  y

  2
  +

  z

  2

  y
  =
  −

  −

  x

  2
  +

  z

  2

  ,

  y
  =

  −

  x

  2
  +

  z

  2

  z
  =
  −

  x

  2
  +

  y

  2

  ,

  z
  =

  x

  2
  +

  y

  2

  x
  =
  −

  −

  y

  2
  +

  z

  2

  ,

  x
  =

  −

  y

  2
  +

  z

  2

  y
  =
  −

  −

  x

  2
  +

  z

  2

  ,

  y
  =

  −

  x

  2
  +

  z

  2

  z
  =
  −

  x

  2
  +

  y

  2

  ,

  z
  =

  x

  2
  +

  y

  2
  {[x=-sqrt(-y^(2)+z^(2))","quad x=sqrt(-y^(2)+z^(2))],[y=-sqrt(-x^(2)+z^(2))","quad y=sqrt(-x^(2)+z^(2))],[z=-sqrt(x^(2)+y^(2))","quad z=sqrt(x^(2)+y^(2))]:}\left\{ \begin{array} {l} \,x = - \sqrt{- y^{2} + z^{2}}\,,\quad x = \sqrt{- y^{2} + z^{2}} \\\,
  y = - \sqrt{- x^{2} + z^{2}}\,,\quad y = \sqrt{- x^{2} + z^{2}} \\\,
  z = - \sqrt{x^{2} + y^{2}}\,,\quad z = \sqrt{x^{2} + y^{2}} \end{array} \right.{x=−−y2+z2,x=−y2+z2y=−−x2+z2,y=−x2+z2z=−x2+y2,z=x2+y2

  ---

  + Simplification

  z

  2
  =

  x

  2
  +

  y

  2

  z

  2
  =

  x

  2
  +

  y

  2
  z^(2)=x^(2)+y^(2)z^{2} = x^{2} + y^{2}z2=x2+y2

---

* Input

  x
  2
  +

  y
  2
  =
  100

  x
  2
  +

  y
  2
  =
  100
  x^(2)+y^(2)=100x^2 + y^2 = 100x2+y2=100

  ---

  + Solution

  {

  x
  =
  −

  100
  −

  y

  2

  ,

  x
  =

  100
  −

  y

  2

  y
  =
  −

  100
  −

  x

  2

  ,

  y
  =

  100
  −

  x

  2

  x
  =
  −

  100
  −

  y

  2

  ,

  x
  =

  100
  −

  y

  2

  y
  =
  −

  100
  −

  x

  2

  ,

  y
  =

  100
  −

  x

  2
  {[x=-sqrt(100-y^(2))","quad x=sqrt(100-y^(2))],[y=-sqrt(100-x^(2))","quad y=sqrt(100-x^(2))]:}\left\{ \begin{array} {l} \,x = - \sqrt{100 - y^{2}}\,,\quad x = \sqrt{100 - y^{2}} \\\,
  y = - \sqrt{100 - x^{2}}\,,\quad y = \sqrt{100 - x^{2}} \end{array} \right.{x=−100−y2,x=100−y2y=−100−x2,y=100−x2

  ---

  + Simplification

  x

  2
  +

  y

  2
  =
  100

  x

  2
  +

  y

  2
  =
  100
  x^(2)+y^(2)=100x^{2} + y^{2} = 100x2+y2=100

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/649edc8bcaccec89ba976a1216b8fa31.png)

---

* Input

  x
  2
  +

  y
  3
  =
  100

  x
  2
  +

  y
  3
  =
  100
  x^(2)+y^(3)=100x^2 + y^3 = 100x2+y3=100

  ---

  + Solution

  {

  x
  =
  −

  100
  −

  y

  3

  ,

  x
  =

  100
  −

  y

  3

  y
  =

  100
  −

  x

  2
  3

  ,

  y
  =
  −

  100
  −

  x

  2
  3
  2
  −

  3
  i

  100
  −

  x

  2
  3
  2

  ,

  y
  =
  −

  100
  −

  x

  2
  3
  2
  +

  3
  i

  100
  −

  x

  2
  3
  2

  x
  =
  −

  100
  −

  y

  3

  ,

  x
  =

  100
  −

  y

  3

  y
  =

  100
  −

  x

  2
  3

  ,

  y
  =
  −

  100
  −

  x

  2
  3
  2
  −

  3
  i

  100
  −

  x

  2
  3
  2

  ,

  y
  =
  −

  100
  −

  x

  2
  3
  2
  +

  3
  i

  100
  −

  x

  2
  3
  2
  {[x=-sqrt(100-y^(3))","quad x=sqrt(100-y^(3))],[y=root(3)(100-x^(2))","quad y=-(root(3)(100-x^(2)))/(2)-(sqrt3iroot(3)(100-x^(2)))/(2)","quad y=-(root(3)(100-x^(2)))/(2)+(sqrt3iroot(3)(100-x^(2)))/(2)]:}\left\{ \begin{array} {l} \,x = - \sqrt{100 - y^{3}}\,,\quad x = \sqrt{100 - y^{3}} \\\,
  y = \sqrt[3]{100 - x^{2}}\,,\quad y = - \frac{\sqrt[3]{100 - x^{2}}}{2} - \frac{\sqrt{3} i \sqrt[3]{100 - x^{2}}}{2}\,,\quad y = - \frac{\sqrt[3]{100 - x^{2}}}{2} + \frac{\sqrt{3} i \sqrt[3]{100 - x^{2}}}{2} \end{array} \right.{x=−100−y3,x=100−y3y=100−x23,y=−100−x232−3i100−x232,y=−100−x232+3i100−x232

  ---

  + Simplification

  x

  2
  +

  y

  3
  =
  100

  x

  2
  +

  y

  3
  =
  100
  x^(2)+y^(3)=100x^{2} + y^{3} = 100x2+y3=100

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/c5469d37b0c0dbf9ca345b0a173175cb.png)

---

* Input

  u
  =

  0.3
  ⋅

  10

  −
  2
  +
  2.4
  ⋅

  10
  8

  1
  +
  (
  0.3
  ⋅

  10

  −
  2
  )
  ⋅
  (
  2.66851
  ⋅

  10

  −
  9
  )
  u
  =

  0.3
  ⋅

  10

  −
  2
  +
  2.4
  ⋅

  10
  8

  1
  +
  (
  0.3
  ⋅

  10

  −
  2
  )
  ⋅
  (
  2.66851
  ⋅

  10

  −
  9
  )
  u=(0.3\*10^(-2)+2.4\*10^(8))/(1+(0.3\*10^(-2))\*(2.66851\*10^(-9)))u=\frac{0.3 \cdot 10^{-2} + 2.4\cdot10^8}{1+ (0.3 \cdot 10^{-2}) \cdot (2.66851\cdot10^{-9})}u=0.3⋅10−2+2.4⋅1081+(0.3⋅10−2)⋅(2.66851⋅10−9)

  ---

  + Solution

  u
  =
  240000000.001079
  u
  =
  240000000.001079
  u=240000000.001079u = 240000000.001079u=240000000.001079

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/ae94150c4998ebb6641ceff4b87d9bdc.png)

---

* Input

  u
  =

  u

  ′
  +
  v

  1
  +

  u

  ′
  v

  /

  c

  2
  u
  =

  u

  ′
  +
  v

  1
  +

  u

  ′
  v

  /

  c

  2
  u=(u^(')+v)/(1+u^(')v//c^(2))u=\frac{u^{\prime}+v}{1+u^{\prime} v / c^{2}}u=u′+v1+u′v/c2

  ---

  + Solution

  {

  c
  =
  −

  u

  u

  ′
  v

  −
  u
  +

  u

  ′
  +
  v

  ,

  c
  =

  u

  u

  ′
  v

  −
  u
  +

  u

  ′
  +
  v

  u
  =

  c

  2

  (

  u

  ′
  +
  v
  )

  c

  2
  +

  u

  ′
  v

  u

  ′
  =

  c

  2

  (
  u
  −
  v
  )

  c

  2
  −
  u
  v

  v
  =

  c

  2

  (
  u
  −

  u

  ′
  )

  c

  2
  −
  u

  u

  ′

  c
  =
  −

  u

  u

  ′
  v

  −
  u
  +

  u

  ′
  +
  v

  ,

  c
  =

  u

  u

  ′
  v

  −
  u
  +

  u

  ′
  +
  v

  u
  =

  c

  2

  u

  ′
  +
  v

  c

  2
  +

  u

  ′
  v

  u

  ′
  =

  c

  2

  u
  −
  v

  c

  2
  −
  u
  v

  v
  =

  c

  2

  u
  −

  u

  ′

  c

  2
  −
  u

  u

  ′
  {[c=-sqrt((uu^(')v)/(-u+u^(')+v))","quad c=sqrt((uu^(')v)/(-u+u^(')+v))],[u=(c^(2)(u^(')+v))/(c^(2)+u^(')v)],[u^(')=(c^(2)(u-v))/(c^(2)-uv)],[v=(c^(2)(u-u^(')))/(c^(2)-uu^('))]:}\left\{ \begin{array} {l} \,c = - \sqrt{\frac{u u^{\prime} v}{- u + u^{\prime} + v}}\,,\quad c = \sqrt{\frac{u u^{\prime} v}{- u + u^{\prime} + v}} \\\,
  u = \frac{c^{2} \left(u^{\prime} + v\right)}{c^{2} + u^{\prime} v} \\\,
  u^{\prime} = \frac{c^{2} \left(u - v\right)}{c^{2} - u v} \\\,
  v = \frac{c^{2} \left(u - u^{\prime}\right)}{c^{2} - u u^{\prime}} \end{array} \right.{c=−uu′v−u+u′+v,c=uu′v−u+u′+vu=c2(u′+v)c2+u′vu′=c2(u−v)c2−uvv=c2(u−u′)c2−uu′

  ---

  + Simplification

  u
  =

  c

  2

  (

  u

  ′
  +
  v
  )

  c

  2
  +

  u

  ′
  v
  u
  =

  c

  2

  u

  ′
  +
  v

  c

  2
  +

  u

  ′
  v
  u=(c^(2)(u^(')+v))/(c^(2)+u^(')v)u = \frac{c^{2} \left(u^{\prime} + v\right)}{c^{2} + u^{\prime} v}u=c2(u′+v)c2+u′v

---

* Input

  ∫

  a

  b

  f

  ′
  (
  x
  )
  d
  x
  =
  f
  (
  b
  )
  −
  f
  (
  a
  )

  ∫

  a

  b

   

  f

  ′
  (
  x
  )
  d
  x
  =
  f
  (
  b
  )
  −
  f
  (
  a
  )
  int\_(a)^(b)f^(')(x)dx=f(b)-f(a)\int\_{a}^{b} f^{\prime}(x) d x=f(b)-f(a)∫abf′(x)dx=f(b)−f(a)

  ---

  + Simplification

  True
  True
  "True"\text{True}True

---

* Input

  y

  2
  =

  x

  2
  y
  +

  x

  5

  y

  2
  =

  x

  2
  y
  +

  x

  5
  y^(2)=x^(2)y+x^(5)y^{2}=x^{2} y+x^{5}y2=x2y+x5

  ---

  + Simplification

  y

  2
  =

  x

  2

  (

  x

  3
  +
  y
  )

  y

  2
  =

  x

  2

  x

  3
  +
  y
  y^(2)=x^(2)(x^(3)+y)y^{2} = x^{2} \left(x^{3} + y\right)y2=x2(x3+y)

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/3213b175630c61ca1dbb413da0240936.png)

---

* Input

  x

  3
  =
  10

  x

  3
  =
  10
  x^(3)=10x^{3}=10x3=10

  ---

  + Solution

  x
  ∈

  {

  10
  3
  ,

  −

  10
  3
  2
  −

  10
  3

  3
  i
  2
  ,

  −

  10
  3
  2
  +

  10
  3

  3
  i
  2
  }
  x
  ∈

  10
  3
  ,

  −

  10
  3
  2
  −

  10
  3

  3
  i
  2
  ,

  −

  10
  3
  2
  +

  10
  3

  3
  i
  2
  x in{root(3)(10),-(root(3)(10))/(2)-(root(3)(10)sqrt3i)/(2),-(root(3)(10))/(2)+(root(3)(10)sqrt3i)/(2)}x \in \left\{ \sqrt[3]{10},\, - \frac{\sqrt[3]{10}}{2} - \frac{\sqrt[3]{10} \sqrt{3} i}{2},\, - \frac{\sqrt[3]{10}}{2} + \frac{\sqrt[3]{10} \sqrt{3} i}{2}\right\}x∈{103,−1032−1033i2,−1032+1033i2}

  ---

  + Simplification

  x

  3
  =
  10

  x

  3
  =
  10
  x^(3)=10x^{3} = 10x3=10

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/b0cdca0bfe7e11becdfe2478166d19b6.png)

---

# System of Equations

---

* Input

  4
  x
  −
  2
  y
  +
  2
  z

  =
  30

  3
  x
  −
  2
  y
  −
  2
  z

  =
  −
  13

  x
  −
  y
  +
  2
  z

  =
  22

  4
  x
  −
  2
  y
  +
  2
  z

  =
  30

  3
  x
  −
  2
  y
  −
  2
  z

  =
  −
  13

  x
  −
  y
  +
  2
  z

  =
  22
  {:[4x-2y+2z=30],[3x-2y-2z=-13],[x-y+2z=22]:}\begin{aligned} 4 x-2 y+2 z &=30 \\ 3 x-2 y-2 z &=-13 \\ x-y+2 z &=22 \end{aligned}4x−2y+2z=303x−2y−2z=−13x−y+2z=22

  ---

  + Solution

  {

  x
  =
  3

  y
  =
  1

  z
  =
  10

  x
  =
  3

  y
  =
  1

  z
  =
  10
  {[x=3],[y=1],[z=10]:}\left\{ \begin{array} {l} \,x = 3 \\\,
  y = 1 \\\,
  z = 10 \end{array} \right.{x=3y=1z=10

---

* Input

  {

  0.30
  x
  +
  0.30
  y
  =
  30

  0.60
  x
  +
  0.10
  y
  =
  40

  0.30
  x
  +
  0.30
  y
  =
  30

  0.60
  x
  +
  0.10
  y
  =
  40
  {[0.30 x+0.30 y=30],[0.60 x+0.10 y=40]:}\left\{\begin{array}{l}0.30 x+0.30 y=30 \\ 0.60 x+0.10 y=40\end{array}\right.{0.30x+0.30y=300.60x+0.10y=40

  ---

  + Solution

  {

  x
  =
  60.0

  y
  =
  40.0

  x
  =
  60.0

  y
  =
  40.0
  {[x=60.0],[y=40.0]:}\left\{ \begin{array} {l} \,x = 60.0 \\\,
  y = 40.0 \end{array} \right.{x=60.0y=40.0

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/b5b97dcab9f5b3afd6230c107e30da43.png)

---

* Input

  {

  2
  x
  +
  4
  y
  −
  z
  =
  8

  2
  x
  −
  4
  y
  +
  2
  z
  =
  3

  x
  +
  4
  y
  +
  z
  =
  3

  2
  x
  +
  4
  y
  −
  z
  =
  8

  2
  x
  −
  4
  y
  +
  2
  z
  =
  3

  x
  +
  4
  y
  +
  z
  =
  3
  {[2x+4y-z=8],[2x-4y+2z=3],[x+4y+z=3]:}\left\{\begin{array}{r}2 x+4 y-z=8 \\ 2 x-4 y+2 z=3 \\ x+4 y+z=3\end{array}\right.{2x+4y−z=82x−4y+2z=3x+4y+z=3

  ---

  + Solution

  {

  x
  =
  3

  y
  =

  1
  4

  z
  =
  −
  1

  x
  =
  3

  y
  =

  1
  4

  z
  =
  −
  1
  {[x=3],[y=(1)/(4)],[z=-1]:}\left\{ \begin{array} {l} \,x = 3 \\\,
  y = \frac{1}{4} \\\,
  z = -1 \end{array} \right.{x=3y=14z=−1

---

* Input

  {

  x
  −
  1
  2
  +

  y
  +
  2
  3
  =
  4

  x
  −
  2
  y
  =
  5

  x
  −
  1
  2
  +

  y
  +
  2
  3
  =
  4

  x
  −
  2
  y
  =
  5
  {[(x-1)/(2)+(y+2)/(3)=4],[x-2y=5]:}\left\{\begin{array}{r}\frac{x-1}{2}+\frac{y+2}{3}=4 \\ x-2 y=5\end{array}\right.{x−12+y+23=4x−2y=5

  ---

  + Solution

  {

  x
  =
  7

  y
  =
  1

  x
  =
  7

  y
  =
  1
  {[x=7],[y=1]:}\left\{ \begin{array} {l} \,x = 7 \\\,
  y = 1 \end{array} \right.{x=7y=1

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/7ee7c28b6f40fe175bb367f920dfc24d.png)

---

* Input

  2
  x
  −
  y

  =
  5

  7
  x
  −
  3
  y

  =
  20

  2
  x
  −
  y

  =
  5

  7
  x
  −
  3
  y

  =
  20
  {:[2x-y=5],[7x-3y=20]:}\begin{aligned} 2 x-y &=5 \\ 7 x-3 y &=20 \end{aligned}2x−y=57x−3y=20

  ---

  + Solution

  {

  x
  =
  5

  y
  =
  5

  x
  =
  5

  y
  =
  5
  {[x=5],[y=5]:}\left\{ \begin{array} {l} \,x = 5 \\\,
  y = 5 \end{array} \right.{x=5y=5

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/69e1b0f18243690f4e02bd09f55d6c2a.png)

---

* Input

  x
  +
  5
  y
  =
  20
  ,
  −
  3
  x
  −
  5
  y
  =
  −
  20
  x
  +
  5
  y
  =
  20
  ,
  −
  3
  x
  −
  5
  y
  =
  −
  20
  x+5y=20,-3x-5y=-20x+5 y=20, -3 x-5 y=-20x+5y=20,−3x−5y=−20

  ---

  + Solution

  {

  x
  =
  0

  y
  =
  4

  x
  =
  0

  y
  =
  4
  {[x=0],[y=4]:}\left\{ \begin{array} {l} \,x = 0 \\\,
  y = 4 \end{array} \right.{x=0y=4

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/4b1754ccdc287c3802ece90e118b7708.png)

---

* Input

  2
  x
  +
  y
  +
  7
  z
  =
  4
  ,
  3
  x
  −
  9
  y
  −
  z
  =
  2
  ,
  x
  −
  8
  y
  −
  6
  z
  =
  −
  9
  2
  x
  +
  y
  +
  7
  z
  =
  4
  ,
  3
  x
  −
  9
  y
  −
  z
  =
  2
  ,
  x
  −
  8
  y
  −
  6
  z
  =
  −
  9
  2x+y+7z=4,3x-9y-z=2,x-8y-6z=-92 x+y+7 z=4, 3 x-9 y-z=2, x-8 y-6 z=-92x+y+7z=4,3x−9y−z=2,x−8y−6z=−9

  ---

  + Solution

  {

  x
  =
  −

  237
  2

  y
  =
  −

  177
  4

  z
  =

  163
  4

  x
  =
  −

  237
  2

  y
  =
  −

  177
  4

  z
  =

  163
  4
  {[x=-(237)/(2)],[y=-(177)/(4)],[z=(163)/(4)]:}\left\{ \begin{array} {l} \,x = - \frac{237}{2} \\\,
  y = - \frac{177}{4} \\\,
  z = \frac{163}{4} \end{array} \right.{x=−2372y=−1774z=1634

---

* Input

  x
  +
  y
  −
  z
  =
  −
  7
  ,
  3
  x
  −
  y
  +
  z
  =
  −
  1
  ,
  x
  −
  2
  y
  +
  4
  z
  =
  46
  x
  +
  y
  −
  z
  =
  −
  7
  ,
  3
  x
  −
  y
  +
  z
  =
  −
  1
  ,
  x
  −
  2
  y
  +
  4
  z
  =
  46
  x+y-z=-7,3x-y+z=-1,x-2y+4z=46x+y-z=-7, 3 x-y+z=-1, x-2 y+4 z=46x+y−z=−7,3x−y+z=−1,x−2y+4z=46

  ---

  + Solution

  {

  x
  =
  −
  2

  y
  =
  14

  z
  =
  19

  x
  =
  −
  2

  y
  =
  14

  z
  =
  19
  {[x=-2],[y=14],[z=19]:}\left\{ \begin{array} {l} \,x = -2 \\\,
  y = 14 \\\,
  z = 19 \end{array} \right.{x=−2y=14z=19

---

* Input

  x
  +
  y
  =
  10
  ,

  x
  2
  +
  2
  =
  y
  x
  +
  y
  =
  10
  ,

  x
  2
  +
  2
  =
  y
  x+y=10,x^(2)+2=yx + y = 10, x^2 + 2 = yx+y=10,x2+2=y

  ---

  + Solution

  {

  x
  =
  −

  1
  2
  +

  33
  2

  ,

  y
  =

  21
  2
  −

  33
  2

  x
  =
  −

  33
  2
  −

  1
  2

  ,

  y
  =

  33
  2
  +

  21
  2

  x
  =
  −

  1
  2
  +

  33
  2

  ,

  y
  =

  21
  2
  −

  33
  2

  x
  =
  −

  33
  2
  −

  1
  2

  ,

  y
  =

  33
  2
  +

  21
  2
  {[x=-(1)/(2)+(sqrt33)/(2)","quad y=(21)/(2)-(sqrt33)/(2)],[x=-(sqrt33)/(2)-(1)/(2)","quad y=(sqrt33)/(2)+(21)/(2)]:}\left\{ \begin{array} {l} \,x = - \frac{1}{2} + \frac{\sqrt{33}}{2}\,,\quad y = \frac{21}{2} - \frac{\sqrt{33}}{2} \\\,
  x = - \frac{\sqrt{33}}{2} - \frac{1}{2}\,,\quad y = \frac{\sqrt{33}}{2} + \frac{21}{2} \end{array} \right.{x=−12+332,y=212−332x=−332−12,y=332+212

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/1227fe92a48f0ccc4ffd1a2509b58c2d.png)

---

* Input

  −
  12
  x
  +
  9
  y

  =
  7

  9
  x
  −
  12
  y

  =
  6

  −
  12
  x
  +
  9
  y

  =
  7

  9
  x
  −
  12
  y

  =
  6
  {:[-12 x+9y=7],[9x-12 y=6]:}\begin{aligned}
  -12 x+9 y &=7 \\
  9 x-12 y &=6
  \end{aligned}−12x+9y=79x−12y=6

  ---

  + Solution

  {

  x
  =
  −

  46
  21

  y
  =
  −

  15
  7

  x
  =
  −

  46
  21

  y
  =
  −

  15
  7
  {[x=-(46)/(21)],[y=-(15)/(7)]:}\left\{ \begin{array} {l} \,x = - \frac{46}{21} \\\,
  y = - \frac{15}{7} \end{array} \right.{x=−4621y=−157

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/83971b9328bf4805e9bf9c2fb9633b57.png)

---

* Input

  2
  x
  −
  y
  =
  5

  7
  x
  −
  3
  y
  =
  20

  2
  x
  −
  y
  =
  5

  7
  x
  −
  3
  y
  =
  20
  {:[2x-y=5],[7x-3y=20]:}\begin{array}{c}
  2 x-y=5 \\
  7 x-3 y=20
  \end{array}2x−y=57x−3y=20

  ---

  + Solution

  {

  x
  =
  5

  y
  =
  5

  x
  =
  5

  y
  =
  5
  {[x=5],[y=5]:}\left\{ \begin{array} {l} \,x = 5 \\\,
  y = 5 \end{array} \right.{x=5y=5

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/a096eb26e201caf13b40c8dcd1e2bee8.png)

---

* Input

  {

  2
  x
  +
  5

  x

  2
  +
  2

  2
  x
  +
  5

  x

  2
  +
  2
  {[2x+5],[x^(2)+2]:}\left\{\begin{array}{l}
  2 x+5 \\
  x^{2}+2
  \end{array}\right.{2x+5x2+2

  ---

  + Solution

  ∅
  ∅
  O/\emptyset∅

---

* Input

  {

  x
  3
  =
  y

  x
  2
  +

  y
  2
  =
  10

  y
  =
  2
  x

  x
  3
  =
  y

  x
  2
  +

  y
  2
  =
  10

  y
  =
  2
  x
  {[x^(3)=y],[x^(2)+y^(2)=10],[y=2x]:}\left\{\begin{array}{ccc} x^3 = y \\ x^2 + y^2 = 10 \\ y = 2x \end{array}\right.{x3=yx2+y2=10y=2x

  ---

  + Solution

  {

  x
  =
  −

  2

  ,

  y
  =
  −
  2

  2

  x
  =

  2

  ,

  y
  =
  2

  2

  x
  =
  −

  2

  ,

  y
  =
  −
  2

  2

  x
  =

  2

  ,

  y
  =
  2

  2
  {[x=-sqrt2","quad y=-2sqrt2],[x=sqrt2","quad y=2sqrt2]:}\left\{ \begin{array} {l} \,x = - \sqrt{2}\,,\quad y = - 2 \sqrt{2} \\\,
  x = \sqrt{2}\,,\quad y = 2 \sqrt{2} \end{array} \right.{x=−2,y=−22x=2,y=22

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/0ccf7a10563deac89fb4e83ddd8e864d.png)

---

* Input

  {

  x
  3
  =
  y

  x
  2
  +

  y
  2
  =
  10

  y
  =

  x

  x
  3
  =
  y

  x
  2
  +

  y
  2
  =
  10

  y
  =

  x
  {[x^(3)=y],[x^(2)+y^(2)=10],[y=sqrtx]:}\left\{\begin{array}{ccc} x^3 = y \\ x^2 + y^2 = 10 \\ y = \sqrt{x} \end{array}\right.{x3=yx2+y2=10y=x

  ---

  + Solution

  ∅
  ∅
  O/\emptyset∅

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/536e489359bb32562aa3d99489970c56.png)

---

* Input

  {

  x
  2
  +
  y
  =
  10

  y
  =
  5
  x

  x
  2
  +
  y
  =
  10

  y
  =
  5
  x
  {[x^(2)+y=10],[y=5x]:}\left\{ \begin{array}{ccc} x^2 + y= 10 \\y = 5x\end{array}\right.{x2+y=10y=5x

  ---

  + Solution

  {

  x
  =
  −

  5
  2
  +

  65
  2

  ,

  y
  =
  −

  25
  2
  +

  5

  65
  2

  x
  =
  −

  65
  2
  −

  5
  2

  ,

  y
  =
  −

  5

  65
  2
  −

  25
  2

  x
  =
  −

  5
  2
  +

  65
  2

  ,

  y
  =
  −

  25
  2
  +

  5

  65
  2

  x
  =
  −

  65
  2
  −

  5
  2

  ,

  y
  =
  −

  5

  65
  2
  −

  25
  2
  {[x=-(5)/(2)+(sqrt65)/(2)","quad y=-(25)/(2)+(5sqrt65)/(2)],[x=-(sqrt65)/(2)-(5)/(2)","quad y=-(5sqrt65)/(2)-(25)/(2)]:}\left\{ \begin{array} {l} \,x = - \frac{5}{2} + \frac{\sqrt{65}}{2}\,,\quad y = - \frac{25}{2} + \frac{5 \sqrt{65}}{2} \\\,
  x = - \frac{\sqrt{65}}{2} - \frac{5}{2}\,,\quad y = - \frac{5 \sqrt{65}}{2} - \frac{25}{2} \end{array} \right.{x=−52+652,y=−252+5652x=−652−52,y=−5652−252

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/608620874907d4ae32739dc7e4f2491f.png)

---

# Limits

---

* Input

  lim

  x
  →
  256

  (

  1

  x
  −
  16
  −

  32

  x
  −
  256
  )
  =

  lim

  x
  →
  256

   

  1

  x
  −
  16
  −

  32

  x
  −
  256
  =
  lim\_(x rarr256)((1)/(sqrtx-16)-(32)/(x-256))=\lim \_{x \rightarrow 256}\left(\frac{1}{\sqrt{x}-16}-\frac{32}{x-256}\right)=limx→256(1x−16−32x−256)=

  ---

  + Result

  1
  32

  1
  32
  (1)/(32)\frac{1}{32}132

---

* Input

  lim

  v
  →
  c

  L

  o

  1
  −

  v

  2

  c

  2

  lim

  v
  →
  c

   

  L

  o

  1
  −

  v

  2

  c

  2
  lim\_(v rarr c)L\_(o)sqrt(1-(v^(2))/(c^(2)))\lim \_{v \rightarrow c} L\_{o} \sqrt{1-\frac{v^{2}}{c^{2}}}limv→cLo1−v2c2

  ---

  + Result

  0
  0
  000

---

# Function

---

* Input

  f
  (
  x
  )
  =

  x

  3

  /
  2
  +

  x

  2

  /
  3
  ,
   solve for 

  f

  ′
  (
  1
  )
  f
  (
  x
  )
  =

  x

  3

  /
  2
  +

  x

  2

  /
  3
  ,
   solve for 

  f

  ′
  (
  1
  )
  f(x)=x^(3//2)+x^(2//3)," solve for "f^(')(1)f(x)=x^{3 / 2}+x^{2 / 3}, \text { solve for } f^{\prime}(1)f(x)=x3/2+x2/3, solve for f′(1)

  ---

  + Solution

  d

  d
  x
  f

  (
  x
  )
  |

  x
  =
  1
  =

  13
  6

  d

  d
  x
  f

  x

  x
  =
  1
  =

  13
  6
  (d)/(dx)f((x))|\_({:x=1:})=(13)/(6)\left. \frac{d}{d x} f{\left(x \right)} \right|\_{\substack{ x=1 }} = \frac{13}{6}ddxf(x)|x=1=136

  ---

  + Simplification

  f

  (
  x
  )
  =

  x

  2
  3
  +

  x

  3
  2
  f

  x
  =

  x

  2
  3
  +

  x

  3
  2
  f(x)=x^((2)/(3))+x^((3)/(2))f{\left(x \right)} = x^{\frac{2}{3}} + x^{\frac{3}{2}}f(x)=x23+x32

---

* Input

  f
  (
  x
  )
  =

  x

  2
  −
  x
  −
  1
  ,
   solve for 

  f

  ′
  (
  x
  )
  f
  (
  x
  )
  =

  x

  2
  −
  x
  −
  1
  ,
   solve for 

  f

  ′
  (
  x
  )
  f(x)=x^(2)-x-1," solve for "f^(')(x)f(x)=x^{2}-x-1, \text { solve for } f^{\prime}(x)f(x)=x2−x−1, solve for f′(x)

  ---

  + Solution

  d

  d
  x
  f

  (
  x
  )
  =
  2
  x
  −
  1

  d

  d
  x
  f

  x
  =
  2
  x
  −
  1
  (d)/(dx)f(x)=2x-1\frac{d}{d x} f{\left(x \right)} = 2 x - 1ddxf(x)=2x−1

  ---

  + Simplification

  f

  (
  x
  )
  =

  x

  2
  −
  x
  −
  1
  f

  x
  =

  x

  2
  −
  x
  −
  1
  f(x)=x^(2)-x-1f{\left(x \right)} = x^{2} - x - 1f(x)=x2−x−1

---

# Derivatives

---

* Input

  d

  d
  x

  [

  4

  e

  x
  +
  7

  e

  −
  x
  9
  ]

  d

  d
  x

  4

  e

  x
  +
  7

  e

  −
  x
  9
  (d)/(dx)[(4e^(x)+7e^(-x))/(9)]\frac{d}{d x}\left[\frac{4 e^{x}+7 e^{-x}}{9}\right]ddx[4ex+7e−x9]

  ---

  + Result

  4

  e

  x
  9
  −

  7

  e

  −
  x
  9

  4

  e

  x
  9
  −

  7

  e

  −
  x
  9
  (4e^(x))/(9)-(7e^(-x))/(9)\frac{4 e^{x}}{9} - \frac{7 e^{- x}}{9}4ex9−7e−x9

  ---

  + Simplification

  −

  (

  4

  e

  2
  x
  9
  +

  7
  9
  )

  e

  −
  x
  +

  8

  e

  x
  9
  −

  4

  e

  2
  x
  9
  +

  7
  9

  e

  −
  x
  +

  8

  e

  x
  9
  -((4e^(2x))/(9)+(7)/(9))e^(-x)+(8e^(x))/(9)- \left(\frac{4 e^{2 x}}{9} + \frac{7}{9}\right) e^{- x} + \frac{8 e^{x}}{9}−(4e2x9+79)e−x+8ex9

---

# Elementary

---

* Input

  sin
  ⁡
  (
  x
  )
  sin
  ⁡
  (
  x
  )
  sin(x)\sin(x)sin⁡(x)

  ---

  + Result

  sin
  ⁡

  (
  x
  )
  sin
  ⁡

  x
  sin (x)\sin{\left(x \right)}sin⁡(x)

  ---

  + Alternative Forms

  {

  1

  sec
  ⁡

  (
  x
  −

  π
  2
  )

  1

  csc
  ⁡

  (
  x
  )

  2
  cot
  ⁡

  (

  x
  2
  )

  cot

  2
  ⁡

  (

  x
  2
  )
  +
  1

  2
  tan
  ⁡

  (

  x
  2
  )

  tan

  2
  ⁡

  (

  x
  2
  )
  +
  1

  cos
  ⁡

  (
  x
  −

  π
  2
  )

  1

  sec
  ⁡

  x
  −

  π
  2

  1

  csc
  ⁡

  x

  2
  cot
  ⁡

  x
  2

  cot

  2
  ⁡

  x
  2
  +
  1

  2
  tan
  ⁡

  x
  2

  tan

  2
  ⁡

  x
  2
  +
  1

  cos
  ⁡

  x
  −

  π
  2
  {[(1)/(sec ((x-(pi)/(2))))],[(1)/(csc ((x)))],[(2cot (((x)/(2))))/(cot^(2)(((x)/(2)))+1)],[(2tan (((x)/(2))))/(tan^(2)(((x)/(2)))+1)],[cos (x-(pi)/(2))]:}\left\{ \begin{array} {l} \,\frac{1}{\sec{\left(x - \frac{\pi}{2} \right)}} \\\,
  \frac{1}{\csc{\left(x \right)}} \\\,
  \frac{2 \cot{\left(\frac{x}{2} \right)}}{\cot^{2}{\left(\frac{x}{2} \right)} + 1} \\\,
  \frac{2 \tan{\left(\frac{x}{2} \right)}}{\tan^{2}{\left(\frac{x}{2} \right)} + 1} \\\,
  \cos{\left(x - \frac{\pi}{2} \right)} \end{array} \right.{1sec⁡(x−π2)1csc⁡(x)2cot⁡(x2)cot2⁡(x2)+12tan⁡(x2)tan2⁡(x2)+1cos⁡(x−π2)

  ---

  + Graph  
    ![Plot](https://cdn.mathpix.com/solve/images/6ba7651f803dfc9e410fdb80717481c5.png)

---

# Numericals

---

* Input

  |

  2

  0

  2

  4

  3

  3

  1

  2

  0

  1

  3

  1

  4

  1

  7

  1
  |

  2
      

  0
      

  2
      

  4

  3
      

  3
      

  1
      

  2

  0
      

  1
      

  3
      

  1

  4
      

  1
      

  7
      

  1
  |[2,0,2,4],[3,3,1,2],[0,1,3,1],[4,1,7,1]|\left|\begin{array}{llll}2 & 0 & 2 & 4 \\ 3 & 3 & 1 & 2 \\ 0 & 1 & 3 & 1 \\ 4 & 1 & 7 & 1\end{array}\right||2024331201314171|

  ---

  + Result

  −
  176.0
  −
  176.0
  -176.0-176.0−176.0

---

[<   Tables](/docs/snip/try-examples-tables)

[Compatibility   >](/docs/snip/compatibility)