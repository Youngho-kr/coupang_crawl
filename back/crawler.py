import os
import sys
from urllib.parse import urlparse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")

import django
django.setup()

from post.models import Post
import requests
from bs4 import BeautifulSoup

url_bases = ["https://www.coupang.com/np/categories/194276", "https://www.coupang.com/np/categories/497135"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
}

def crawling():
    result = []
    for url_base in url_bases:
        res = requests.get(url_base, headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")

        items = soup.find_all("li", "baby-product renew-badge")

        for item in items:
            # 품절된 상품은 수집 X
            sold_out = item.find("div", "out-of-stock")
            if sold_out != None:
                continue
            # 세일하지 않는 상품은 수집 X
            discount_percent = item.find("span", "discount-percentage")
            if discount_percent == None:
                continue
            
            name = item.find("div", "name")
            old_price = item.find("del", "base-price")
            new_price = item.find("strong", "price-value")
            link = item.find("a", "baby-product-link")
            link = link.get("href")
            link = "http://www.coupang.com" + link
            
            # print(link)
            
            tmp = {
                "name": name.text.replace("\n", "")[4:],
                "discount_percent": discount_percent.text,
                "old_price": old_price.text.replace("\n", "").replace(" ",""),
                "new_price": new_price.text,
                "link": link
            }
            
            for r in result:
                if r["name"] == tmp["name"]:
                    continue

            result.append(tmp)     
    return result
    
if __name__ == "__main__": 
    crawl_result = crawling()
    for item in crawl_result:
        Post(name = item["name"], discount_percent = item["discount_percent"], old_price = item["old_price"], new_price = item["new_price"], link = item["link"]).save()
        