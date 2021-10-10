import numpy as np

class Regression(object):

    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        pass
        
    def fit(self, X, y):
        pass

    def predict(self, X):
        return X.dot(self.params["beta"]) + self.params["intercept"]

    def score(self, X, y):
        ss_t = np.sum((y - np.mean(y)) ** 2)
        ss_e = np.sum((y - self.predict(X)) ** 2)
        r2 = 1 - ss_e / ss_t
        return r2


class LinearRegression(Regression):
    def __init__(self):
        super().__init__()

    def fit(self, X, y):
        X_new = np.concatenate([np.ones(len(y)).reshape(-1, 1), X], axis = 1)
        coefs = np.linalg.inv(X_new.T.dot(X_new)).dot(X_new.T).dot(y)
        self.params["beta"] = coefs[1:]
        self.params["intercept"] = coefs[0]


class RidgeRegression(LinearRegression):
    def __init__(self, alpha):
        super().__init__()
        self.alpha = alpha

    def set_params(self, **kwargs):
        self.alpha = kwargs['alpha']

    def fit(self, X, y):
        X_new = np.concatenate([np.ones(len(y)).reshape(-1, 1), X], axis = 1)
        gamma = self.alpha * np.eye(X_new.shape[1])
        coefs = np.linalg.inv(X_new.T.dot(X_new) + gamma.T.dot(gamma)).dot(X_new.T).dot(y)
        self.params["beta"] = coefs[1:]
        self.params["intercept"] = coefs[0]


