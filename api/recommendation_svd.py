import joblib
import pandas as pd
import json

class recommend_svd():
    def __init__(self, master):
        self.model = {}
        self.master = master 
        #for i in range(2):
        #    self.model[i] = joblib.load("../models/SVD_Group"+str(i)+".pkl")

        #self.df_productset = pd.read_csv('../data/Products.csv')
    
    def get_prediction(self, Group: int, User: str):
        if Group not in self.model:
            self.model[Group] = joblib.load("../models/SVD_Group"+str(Group)+".pkl")
        predictions = [self.model[Group].predict(User, item_id) for item_id in list(self.master.Products['Product'])]
        #'a7e8f400-138d-4637-b3ff-1e875052dfab'
        top_n = sorted(predictions, key=lambda x: x.est, reverse=True)[:5]
        recommended_list = []
        for uid, iid, true_r, est, _ in top_n:
            recommended_list.append(iid)
        return json.dumps(recommended_list, ensure_ascii=False)
        