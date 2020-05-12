import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/dp/B07JWVNKRL?aaxitk=rcP09C1WVbOxjtPMkPghDg&pd_rd_i=B07JWVNKRL&pf_rd_p=2e3653de-1bdf-402d-9355-0b76590c54fe&hsa_cr_id=3168718750102&sb-ci-n=productDescription&sb-ci-v=Apple%20iPhone%20XR%20(64GB)%20(Product)%20RED&sb-ci-a=B07JWVNKRL'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = price[0:8]
    print(title.strip())
    print(converted_price)


checkPrice()
