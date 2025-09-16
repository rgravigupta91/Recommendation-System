from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.pd = pd
        self.np = np
        self.columns = columns  # Can be list of names or indices

    def fit(self, X, y=None): 
        return self

    def transform(self, X):
        return X[self.columns]