import pandas as pd
import json
class MasterData():
    def __init__(self): 
        self.Products = pd.read_csv('../data/Products.csv')
        self.Users    = pd.read_csv('../data/UserData.csv')

    def get_products(self, prodset):
        prod = list(self.Products[self.Products['ProductSet']==prodset]['Product'].unique())
        prod.sort()
        keys = list(range(len(prod)))
        return json.dumps(dict.fromkeys(['values'],prod), ensure_ascii=False)

    def get_productset(self):
        prodset = list(self.Products['ProductSet'].unique())
        prodset.sort()
        return json.dumps(dict.fromkeys(['values'],prodset), ensure_ascii=False)
    
    def get_customer_type(self):
        customer_type = list(self.Users['Customer_Type'].unique())
        customer_type.sort()
        return json.dumps(dict.fromkeys(['values'],customer_type), ensure_ascii=False)
    
    def get_gender(self):
        gender = list(self.Users['Gender'].unique())
        gender.sort()
        return json.dumps(dict.fromkeys(['values'],gender), ensure_ascii=False)
    
    def get_user_id(self,CustomerType:str,Gender:str,Age:int):
        user_details = self.Users[(self.Users['Age'] == Age) & (self.Users['Gender'] == Gender) & (self.Users['Customer_Type'] == CustomerType)]
        user_details.reset_index(inplace=True)
        if user_details.shape[0] > 0:
            return user_details.at[0,'guid']
            
    def get_user_details(self,phone:int):
        user_details = self.Users[self.Users['Phone']==phone]
        user_details.reset_index(inplace=True)
        #return (user_details.at[0,'guid'],user_details.at[0,'Customer_Type'],user_details.at[0,'Gender'],user_details.at[0,'Age'])
        if user_details.shape[0] > 0:
            keys = ['guid', 'CustomerType', 'Gender', 'Age']
            values = [user_details.at[0,'guid'],user_details.at[0,'Customer_Type'],user_details.at[0,'Gender'],str(user_details.at[0,'Age'])]
            return dict(zip(keys, values))