import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


# PART A

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")
cursor.execute("PRAGMA foreign_keys=1")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER, 
               desc TEXT, 
               param_name TEXT, 
               value REAL)''')

cursor.execute('''CREATE TABLE model_coefs (
          id INTEGER, 
          desc TEXT, 
          feature_name TEXT, 
          value REAL)''')

cursor.execute('''CREATE TABLE model_results (
          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
          desc TEXT, 
          train_score REAL, 
          test_score REAL)''')

db.commit()


# PART B

# 1. Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# 2. Write a function
def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    # Insert model parameters
    params = model.get_params()
    for param_name, value in params.items():
        vals_to_insert = (model_id, model_desc, param_name, value)
        cursor.execute('''INSERT INTO model_params 
                (id, desc, param_name, value)
                VALUES (?, ?, ?, ?)''', vals_to_insert)

    # Insert model coefficients
    coefs = model.coef_[0]
    intercept = model.intercept_[0]
    feature_names = data.feature_names

    # Intercept
    intercept_to_insert = (model_id, model_desc, "intercept", intercept)
    cursor.execute('''INSERT INTO model_coefs 
                (id, desc, feature_name, value)
                VALUES (?, ?, ?, ?)''', intercept_to_insert)
    
    # Other
    for feature_name, value in zip(feature_names, coefs):
            vals_to_insert = (model_id, model_desc, feature_name, value)
            cursor.execute('''INSERT INTO model_coefs 
                    (id, desc, feature_name, value)
                    VALUES (?, ?, ?, ?)''', vals_to_insert)
    

    # Insert model results
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    scores_to_insert = (model_id, model_desc, train_score, test_score)
    cursor.execute('''INSERT INTO model_results 
                (id, desc, train_score, test_score)
                VALUES (?, ?, ?, ?)''', scores_to_insert)

    db.commit()



# 3. Baseline logistic regression model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, "Baseline model", db, baseline_model, X_train, X_test, y_train, y_test)


# 4. Reduced logistic regression model

feature_cols = ['mean radius', 
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2, "Reduced model", db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)


# 5. Logistic regression model with L1 penalty

penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)

save_to_database(3, "L1 penalty model", db, penalized_model, X_train, X_test, y_train, y_test)



# PART C

# 1. 

query = '''SELECT id, test_score
            FROM model_results 
            ORDER BY test_score DESC
            LIMIT 1'''

res = cursor.execute(query).fetchall()[0]
print(f"Best model id: {res[0]}")
print(f"Best validation score: {res[1]:.4f}")
print()


# 2.
query = '''SELECT mc.feature_name, mc.value
            FROM model_coefs mc INNER JOIN model_results mr
            ON mc.id = mr.id
            WHERE mr.test_score = (SELECT test_score
            FROM model_results 
            ORDER BY test_score DESC
            limit 1)'''

res_list = cursor.execute(query).fetchall()
coefs = []

for i in range(len(res_list)):
    res = res_list[i]
    if res[0] == "intercept":
        intercept = res[1]
        continue
    coefs.append(res[1])
    print(f"{res[0]}: {res[1]:.4f}")

print()

# 3. 

test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
test_model.coef_ = np.array([coefs])
test_model.intercept_ = np.array([intercept])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score:.4f}')


db.close()