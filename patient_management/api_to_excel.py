import requests
import pandas as pd


processed=[]

def fetch_users():
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    data= response.json()
    return data

def process_data(data):
    for user in data:
        processed.append({
            "ID": user['id'],
            "Name": user['name'],
            "Email": user['email'],
            "Phone": user['phone'],
            "City": user['address']['city'],
            "Company": user['company']['name']
        })


def export_to_excel():
    pf= pd.DataFrame(processed)
    pf.to_excel("user.xlsx", index=False)
    return "Exported to users.xlsx"

data=fetch_users()
process_data(data)
print(export_to_excel())