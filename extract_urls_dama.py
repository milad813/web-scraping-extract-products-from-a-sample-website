import requests
from bs4 import BeautifulSoup

for url in range(102):
    response = requests.get(
        f"https://damatajhiz.com/categories/714/%D8%AA%D8%A3%D8%B3%DB%8C%D8%B3%D8%A7%D8%AA-%DA%AF%D8%B1%D9%85%D8%A7%DB%8C%D8%B4%DB%8C-%D8%B3%D8%A7%D8%AE%D8%AA%D9%85%D8%A7%D9%86-%D9%88-%D9%85%D9%88%D8%AA%D9%88%D8%B1%D8%AE%D8%A7%D9%86%D9%87?p={url+1}")
    soup = BeautifulSoup(response.content, "html.parser")
    page_urls = soup.find_all(name="a", class_="product-name")
    for product in page_urls:
        with open("sarmayesh_products.csv", "a") as data_file:
            data_file.write(f"{product.get('href')}\n")
    print(f"page {url} completed")
