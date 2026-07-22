from bs4 import BeautifulSoup
import requests
 
url= "https://www.lush.com/uk/en/c/collaborations?page=3"

r_session= requests.session()
r=r_session.get(url=url)
print(r)
soup= BeautifulSoup(r.text, "html parser")
product_name_css='div.d-flex div.product-title h3.product-title-name'
product_names= soup.select(product_name_css)
product_names[1].text.strip()
