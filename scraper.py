import requests
from bs4 import BeautifulSoup


AI_news = "https://www.artificialintelligence-news.com/"

artical1 = []

response1 = requests.get(AI_news)
html1 = response1.text

soup1 = BeautifulSoup(html1, "html.parser")

container1 = soup1.find_all("div", class_="elementor-loop-container elementor-grid",role="list")
news1 = container1[3].find_all("div", recursive=False)

print(news1[2].get_text())


for i in range(0,3):
    artical1.append({
    "title" : news1[i].find("h1").get_text(),
    "image" : news1[i].find("img")["src"],
    "link": news1[i].find("a")["href"],
    "date" : news1[i].find_all("p")[1].get_text()
    })

[print (artical)for artical in artical1]

