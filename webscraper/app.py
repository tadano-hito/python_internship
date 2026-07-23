# # from bs4 import BeautifulSoup
# # import requests
 
# # url= "https://www.lush.com/uk/en/c/collaborations?page=3"

# # r_session= requests.session()
# # r=r_session.get(url=url)
# # print(r)
# # soup= BeautifulSoup(r.text, "html parser")
# # product_name_css='div.d-flex div.product-title h3.product-title-name'
# # product_names= soup.select(product_name_css)
# # product_names[1].text.strip()




# import requests
# from bs4 import BeautifulSoup

# url = "https://www.automationexercise.com/product_details/1"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# title = soup.select_one("h2").get_text(strip=True)
# price = soup.select_one(".product-information span span").get_text(strip=True)
# image = soup.select_one(".view-product img")["src"]

# print("Title:", title)
# print("Price:", price)
# print("Image:", image)


from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get("https://www.lush.com/uk/en/c/collaborations")
driver.maximize_window()
time.sleep(3)  # let JS render the product cards

soup = BeautifulSoup(driver.page_source, "html.parser")

# each product card is this container div
cards = soup.select("div.flex.flex-col.gap-1")

products = []

for card in cards:
    try:
        name = card.select_one("h3.text-product-name-plp").get_text(strip=True)
    except AttributeError:
        name = None

    try:
        category = card.select_one("p.text-caption").get_text(strip=True)
    except AttributeError:
        category = None

    try:
        description = card.select_one("p.text-xs").get_text(strip=True)
    except AttributeError:
        description = None

    try:
        image = card.find("img")["src"]
    except (AttributeError, TypeError):
        image = None

    products.append({
        "name": name,
        "category": category,
        "description": description,
        "image": image
    })

for p in products:
    print(p)

driver.quit()