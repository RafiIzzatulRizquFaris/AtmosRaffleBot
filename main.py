import pandas as pd
import re
from requests import Session
from bs4 import BeautifulSoup as bs


def login_func(email, password, id_card, gender, name, phone, ig):
    with Session() as s:
        login_data = {"customer[email]": email, "customer[password]": password}
        s.post("https://atmos.co.id/account/login", login_data)
        product_page = s.get("PRODUCT PAGE URL")
        bs_content = bs(product_page.content, "html.parser")
        pattern = re.compile("var\s+id_customer\s+=\s+'(.*?)';")
        print (bs_content)
        print (pattern.findall(product_page.content)[0])
        submit_data = {
            "emailna": email,
            "id_customer": pattern.findall(product_page.content)[0],
            "id_raffle": bs_content.find("input", {"name": "raffle_id"})["value"],
            "id_product": bs_content.find("input", {"name": "product_id"})["value"],
            "id_submission": "0",
            "id_card": id_card,
            "gender": gender,
            "customer_name": name,
            "phone": "0"+str(phone),
            "customer_instagram": "@"+ig,
            "variantna": "YOUR VARIANT",
            "delivery_opt": "Delivery",
            "accept_terms": "on"
        }
        s.post("https://atmos.devbdd.com/front/submit_raffle", submit_data)


df = pd.read_excel(r'YOUR XLS DATA', sheet_name='Sheet1')

for x in df.values:
    login_func(x["YOUR COLUMN"], "YOUR COLUMN", x["YOUR COLUMN"], x["YOUR COLUMN"], x["YOUR COLUMN"], x["YOUR COLUMN"], x["YOUR COLUMN"])
