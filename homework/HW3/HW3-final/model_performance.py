import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import Regression as reg


dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)


alpha_counts = 10
alpha_list = np.logspace(-2.0, 1.0, num = alpha_counts, base= 10.0)

ols_model = reg.LinearRegression()
ols_model_scores, ridge_model_scores = [], []
ols_model.fit(X_train, y_train)
ridge_model= reg.RidgeRegression(alpha = 1) 

print(alpha_list)
for alpha in alpha_list:
    ols_model_scores.append(ols_model.score(X_test, y_test))
    ridge_model.set_params(alpha = alpha)
    ridge_model.fit(X_train, y_train)
    ridge_model_scores.append(ridge_model.score(X_test, y_test))


fig, ax = plt.subplots()
ax.plot(alpha_list, ols_model_scores, label = "Linear Regression")
ax.plot(alpha_list, ridge_model_scores, label = "Ridge Regression")
ax.scatter(alpha_list, ols_model_scores)
ax.scatter(alpha_list, ridge_model_scores)
ax.legend()
ax.set_xlabel("Alphas", fontsize = 14)
ax.set_ylabel("Scores", fontsize = 14)
plt.show()