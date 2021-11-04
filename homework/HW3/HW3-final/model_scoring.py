from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg

dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

alpha = 0.1
model1 = reg.LinearRegression()
model2 = reg.RidgeRegression(alpha=alpha)
models = [model1, model2]

for model in models:
    model.fit(X_train, y_train)

    print(model.score(X_test, y_test))
    print(model.get_params())
    