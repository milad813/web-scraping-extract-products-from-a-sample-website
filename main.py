import requests
from bs4 import BeautifulSoup
from functions import *

# ************************* CREATE SOUP *************************

with open("sarmayesh_products.csv", "r", encoding="utf-8") as data_file:
    urls = data_file.readlines()

total_urls = len(urls)
# if latest item in data.csv was 125 you have to put 125 as product_id!
product_id = 0
for url in urls[product_id::]:
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find(name="h1").getText()  # ************ CREATE TITLE **************

    category = get_category(soup)  # ************ CREATE category *****************

    guaranty_title, guaranty_text = get_guaranty(soup)  # *********** CREATE GUARANTY *************

    short_desc = get_short_desc(soup)  # ************* CREATE SHORT_DESC ****************

    price = get_price(soup)  # ************* CREATE price *****************

    product_id += 1  # ****************** CREATE image_urls ****************
    image_url = get_images(soup, product_id)

    details = get_details(soup)  # *********** CREATE details ****************

    # content = get_content(soup)  # *********** CREATE content **********

    # # ************************* Fina Step ******************************
    data = f"{product_id}\t{url}\t{title}\t{price}\t{category}\t{image_url}\t" \
           f"\t{short_desc}\t{details}{guaranty_title}\t{guaranty_text}" \
        .replace("\n", "\t").replace("\t\t", "\t")

    with open("cooler/data.csv", "a", encoding="utf-8") as data_file:
        data_file.write(f"{data}\n")
    print(f"{product_id} / {total_urls} created")
