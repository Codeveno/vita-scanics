import pandas as pd
from sklearn.linear_model import LogisticRegression

def check_bias(data):
    """
    Check for bias in the data using a logistic regression model.
    """
    # Example: Logistic Regression model
    model = LogisticRegression()
    X = data.drop(columns=['target'])
    y = data['target']
    model.fit(X, y)

    # Check coefficients for bias
    coefficients = model.coef_
    return coefficients