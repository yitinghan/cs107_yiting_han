# Exercise 2

Coder: Diwei Zhang; Sharer & Listener: Yiting Han, Haoming Chen

| trace   | elem op.    | value      | elem der.               | $\nabla_{x}$.  | $\nabla_{y}$     |
| :---:   | :------:    | :------:   | :--------------------:  | :---------: | :----------: |
| $v_{-1}$   | $x$         |  1  | $\dot{v_{-1}}$             |         1   |      0       |
| $v_0$   | $y$         |  1   | $\dot{v_0}$             |         0   |      1       |
| $v_1$ | $v_{-1}^2$ | 1 | $2v_{-1}\dot{v_{-1}}$ | 2 | 0|
| $v_2$ | $v_0^2$ | 1 | $2v_{0}\dot{v_{0}}$ | 0 | 2|
|$v_3$|$v_1+v_2$|2|$\dot{v_1} + \dot{v_2}$|2|2|
|$v_4$| $v_1 + v_0$ | 2 | $\dot{v_1} + \dot{v_0}$ | 1 | 1 |
|$v_5$|$e^{v_4}$|$e^2$|$\dot{v_4}e^{v_4}$|$e^2$|$e^2$|

$\frac{∂^2f}{∂x∂y}  = \begin{bmatrix}2 & 2 \\ exp(2) & exp(2)\end{bmatrix}$