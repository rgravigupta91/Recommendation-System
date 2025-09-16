import pickle
import joblib
import sys
import os

# Add the path to the other folder
sys.path.append(os.path.abspath('../notebooks'))
from userClusteringPipeline import ColumnSelector
from mytools import ColumnSelector
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
 
    
class UserCluster():
    def __init__(self):
        self.userclustermodel = joblib.load("../models/KMeans_pipeline1.pkl")
    
    def get_cluster(self, Customer_Type:str, Gender:str, Age:int):
        return self.userclustermodel.predict(pd.DataFrame(data=[[Customer_Type, Gender,Age]],columns=['Customer_Type', 'Gender', 'Age']))[0]
     
#user = UserCluster()
#print(user.get_cluster('Homemaker','F',26))
