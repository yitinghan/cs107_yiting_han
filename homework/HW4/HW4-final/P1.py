import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f, h):
    def der(x):
        return (f(x + h) - f(x)) / h
    return der

derivative_h1 = numerical_diff(np.log, 1e-1)
derivative_h2 = numerical_diff(np.log, 1e-7)
derivative_h3 = numerical_diff(np.log, 1e-15)

der_true, der_h1, der_h2, der_h3 = [], [], [], []
x_range = np.linspace(0.2, 0.4, 100)


for x in x_range :
    der_true.append(1/x)
    der_h1.append(derivative_h1(x))
    der_h2.append(derivative_h2(x))
    der_h3.append(derivative_h3(x))


fig, ax = plt.subplots()
ax.plot(x_range, der_h1, label = "1e-1")
ax.plot(x_range, der_h2, label = "1e-7")
ax.plot(x_range, der_h3, label = "1e-15")
ax.plot(x_range, der_true, '--', label = "Analytical") # Overlap with der_h2
ax.set_xlabel("x")
ax.set_ylabel("Derivatives")
ax.legend(frameon = False)

print("Answer to Q-a: h set to 1e-7 most closely approximates the true derivative. \n" 
+"If h is to small, the derivates become too wiggy and there will be roundoff errors. \n"
+"If h is too large, it is not close to the truth.")
print("Answer to Q-b: Automatica differentiation does not take numerical estimates, it just computes derivatives directly.")


plt.show()