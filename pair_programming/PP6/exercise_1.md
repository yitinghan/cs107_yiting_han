# Exercise 1

Coder: Diwei Zhang; Sharer & Listener: Yiting Han, Haoming Chen

| trace   | elem op.    | value      | elem der.               | $\nabla_{x}$  | $\nabla_{y}$     |
| :---:   | :------:    | :------:   | :--------------------:  | :---------: | :----------: |
| $v_{-1}$   | $x$         |  $\pi/2$   | $\dot{v_{-1}}$             |         1   |      0       |
| $v_0$   | $y$         |  $\pi/3$   | $\dot{v_0}$             |         0   |      1       |
| $v_1$ | $sin(v_{-1})$ | 1 | $cos(v_{-1})\dot{v_{-1}}$ | 0 | 0|
| $v_2$ | $cos(v_{0})$ | 0.5 | $-sin(v_{0})\dot{v_{0}}$ | 0 | -$√3 / 2$|
|$v_3$| $v_1 - v_2$ | 0.5 | $\dot{v_1} - \dot{v_2}$ | 0 | $√3 / 2$ |
|$v_4$| $v_3^2$ | 0.25| $2v_3\dot{v_3}$ | 0 | $\sqrt 3/2$ | 
|$v_5$| $-v_4$ | -0.25 | $-\dot{v_4}$ | 0 | -$\sqrt 3/2$ |
|$v_6$| $e^{v_5}$ | $e^{-0.25}$ | $e^{v_5}\dot{v_5}$ | 0 | -$\sqrt 3e^{-0.25} / 2$

$f(\frac{\pi}{2}, \frac{\pi}{3}) = e^{-0.25}$

$\frac{\partial f}{\partial x}(\frac{\pi}{2}, \frac{\pi}{3}) = 0$

$\frac{\partial f}{\partial y}(\frac{\pi}{2}, \frac{\pi}{3}) = -\sqrt 3e^{-0.25} / 2$