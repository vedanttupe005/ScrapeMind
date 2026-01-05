import requests
from bs4 import BeautifulSoup


AI_news3 = "https://techcrunch.com/category/artificial-intelligence/"

artical3 = []

response3 = requests.get(AI_news3)
html_response3 = response3.text

soup3 = BeautifulSoup(html_response3, "html.parser")

container3 = soup3.find("ul" , class_="wp-block-post-template is-layout-flow wp-block-post-template-is-layout-flow")
news3 = container3.find_all("li", recursive=False)

print(news3[1].find("img")["src"])


for i in range(3):
    artical3.append({
    "title" : news3[i].select_one("h3>a").get_text(),
    "image" : news3[i].find("img")["src"],
    "link": news3[i].select_one("h3>a")["href"],
    "date" : news3[i].find("time").get_text()
    })

[print (artical)for artical in artical3]