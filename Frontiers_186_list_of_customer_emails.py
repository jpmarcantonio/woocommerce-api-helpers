"""
 Write a py script that will get list of all customer emails for our website
Setup:
You need the ecom website.
You need API credentials.

Problem statement:
Write a script that will get a list of all users for the website.
Your script should output a csv file with list of email addresses.
"""

import requests
from woocommerce import API
import csv

wcapi = API(
    url = "http://localhost:8888/mysite2",
    consumer_key = "<add consumer key>",
    consumer_secret = "<add consumer secret>",
    version = "wc/v3"
)

customers = (wcapi.get("customers"))
output_file = 'list_of_user_email.csv'

email_list = []
for customer in customers.json():
    customer_email = customer["email"]
    email_list.append([customer_email])

with open(output_file, 'w', newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(["User Email Address:"])
    writer.writerows(email_list)