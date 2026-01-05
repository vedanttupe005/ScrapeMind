import requests
from bs4 import BeautifulSoup


AI_news2 = "https://aimagazine.com/"

artical2 = []

response2 = requests.get(AI_news2)
html_response2 = response2.text

soup2 = BeautifulSoup(html_response2, "html.parser")


container2 = soup2.find_all("div", class_="GridWrapper_flex__1NgfS GridWrapper_gutter-default__1hMKq")
news2 = container2[1].find_all("div" , recursive=False)

print(news2[0].find("a")["href"])

for i in news2:
    artical2.append({
        "title" : i.find("a").get_text(),
        "image" : i.find("img")["src"],
        "link": "https://aimagazine.com"+i.find("a")["href"],
    })


[print (artical)for artical in artical2]