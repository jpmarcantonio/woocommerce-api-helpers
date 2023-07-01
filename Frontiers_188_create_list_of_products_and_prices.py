"""
Setup:
Must have a WordPress/Woocommerce website up and running. See the other homework.

Problem Statement:
Use woocommerce API Python library, to make API calls to list all products.
Create a csv file that will have a list of products and their ‘price’ (there are 3 kinds of prices just use the field ‘price’).
So the csv will have two columns ‘name’ and ‘price’.


"""

import requests
from woocommerce import API
import csv

wcapi = API(
    url = "http://localhost:8888/mysite2/",
    consumer_key = "<consumer key>",
    consumer_secret = "<consumer secret>",
    version = "wc/v3"
)

r = wcapi.get("products", params={"per_page": 100})
output_file = "product_list_of_prices_2.csv"
status_code = r.status_code
# assert status_code == 200, f"Expected a status code of 200 but got {status_code}"
if status_code != 200:
    raise Exception(f"Expected status code 200. Got {status_code}")


product_list = []
for product in r.json():
    name = product["name"]
    price = product["price"]
    product_list.append([name, price])


with open (output_file, 'w', newline= '') as csv_f:
    writer = csv.writer(csv_f)
    writer.writerow(["name", "price"])
    writer.writerows(product_list)