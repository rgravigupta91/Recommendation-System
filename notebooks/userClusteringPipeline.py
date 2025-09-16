from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from mytools import ColumnSelector
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans

df_cust = pd.read_csv('../data/UserData.csv')
  
# ------------------------------
# ✅ Pipeline Components

# Step 1: Select only 3 columns
column_selector = ColumnSelector(columns=["Customer_Type", "Gender", "Age"])

# Step 2: Define column-wise transformers
preprocessor = ColumnTransformer(transformers=[
    ("num", StandardScaler(), ["Age"]),
    ("cat", OneHotEncoder(drop="first"), ["Customer_Type", "Gender"])
])

# Step 3: KMeans Clustering
kmeans = KMeans(n_clusters=16, random_state=42)

# Step 4: Full Pipeline
pipeline = Pipeline(steps=[
    ("select_columns", column_selector),
    ("preprocessing", preprocessor),
    ("clustering", kmeans)
])

# ------------------------------
# 🔍 Fit pipeline to data
pipeline.fit(df_cust)

# Write Pipeline
joblib.dump(pipeline,'../models/KMeans_pipeline1.pkl')