from fastapi import Path, Query, FastAPI, Response
from master_data import MasterData
from recommendation_svd import recommend_svd
from user_cluster import UserCluster
import json

app = FastAPI() 
go_masterdata = MasterData()
go_usercluster = UserCluster()
go_recommender = recommend_svd(go_masterdata)

@app.get('/ProductSet')
def get_productset():
    output = go_masterdata.get_productset()
    return Response(content=output, media_type="application/json")

@app.get('/Products')
def get_products(prodset: str):
    output = go_masterdata.get_products(prodset=prodset)
    return Response(content=output, media_type="application/json")

@app.get('/CustomerType')
def get_customer_type():
    output = go_masterdata.get_customer_type()
    return Response(content=output, media_type="application/json")

@app.get('/Gender')
def get_customer_type():
    output = go_masterdata.get_gender()
    return Response(content=output, media_type="application/json")

@app.get('/UserDetails')
def get_user_details(Phone:int):
    my_dict = go_masterdata.get_user_details(Phone)
    output = json.dumps(my_dict, ensure_ascii=False)
    return Response(content=output, media_type="application/json")

@app.get('/Recommendations')
def get_recommendations(Customer_Type:str,Gender:str,Age:int, Phone:int):
    if Phone > 0:
        user_details = go_masterdata.get_user_details(Phone)
        user_id = user_details['guid']
        Customer_Type = user_details['CustomerType']
        Gender = user_details['Gender']
        Age = user_details['Age']
    else:
        user_id = go_masterdata.get_user_id(CustomerType=Customer_Type, Gender=Gender, Age=Age)
        print(user_id)
    group = go_usercluster.get_cluster(Customer_Type,Gender,Age)
    output = go_recommender.get_prediction(Group=group, User=user_id)
    return Response(content=output, media_type="application/json")