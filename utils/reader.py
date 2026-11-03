import csv
import json

def read_users_csv():
    with open("data/users.csv",newline="") as file:
        reader = csv.DictReader(file)
        return list (reader)
    
#data = read_users_csv()
#print(data)

def read_productos_json():
    with open("data/products.json") as file:
        return json.load(file)


