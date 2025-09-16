from sklearn.base import BaseEstimator, TransformerMixin

def colmnSelector(df):
    return df[["Customer_Type", "Gender", "Age"]]

class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns  # Can be list of names or indices
 
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.columns]