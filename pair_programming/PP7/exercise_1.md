"""
Date : Thur Oct 21 2021
Coder : Yiting Han
Listener : Haoming Chen
"""

$f(x,y) = \begin{bmatrix}x^2+y^2\\ exp(x+y) \end{bmatrix}$

## Part 1
$J(1,1)=\begin{bmatrix}2 & 2 \\ exp(2) & exp(2)\end{bmatrix}$

## Part 2
$J_p=\begin{bmatrix}2x-4y\\ -exp(x+y) \end{bmatrix}, P= \begin{bmatrix}1 \\ -2 \end{bmatrix}$
$J_p=\begin{bmatrix}2x+2y \\ 2exp(x+y) \end{bmatrix}, P= \begin{bmatrix}1 \\ 1 \end{bmatrix}$

## Part 3
Trace:

| trace   | elem op.      | value      | elem der.               | $\nabla_{x}$| $\nabla_{y}$ |
| :---:   | :------:      | :------:   | :--------------------:  | :---------: | :----------: |
| $x_1$   | $x$           |     1      |      $\dot{x_1}$        |       1     |       1      |
| $x_2$   | $y$           |     1      |      $\dot{x_2}$        |       -2     |       1      |
| $x_3$   | $x^2_1$       |     1      |      $2 x_1 \dot{x_1}$  |       2     |       2     |
| $x_4$| $x_2^2$| 1| $2x_2\dot{x_2}$| -4|2|
| $x_5$| $x_3+x_4$| 2| $\dot{x_3}+\dot{x_4}$|-2|4|
| $x_6$| $x_1+x_2$| 2| $\dot{x_1}+\dot{x_2}$|-1|2|
| $x_7$| $\exp{(x_6)}$| $\exp{(2)}$ | $\exp{(x_6)}\dot{x_6}$| $-\exp(2)$ |$2\exp(2)$

