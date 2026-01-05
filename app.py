import requests
from bs4 import BeautifulSoup

AI_news = "https://www.artificialintelligence-news.com/"

response1 = requests.get(AI_news)
html1 = response1.text

soup1 = BeautifulSoup(html1, "html.parser")

container1 = soup1.find_all("div", class_="elementor-loop-container elementor-grid",role="list")
news1 = container1[3].find_all("div")

print(news1[0].find("h1").get_text())



news1[0].find("h1").get_text()
image=news1[0].find("img")["src"]
link=news1[0].find("a")["href"]
news1[0].find_all("p")[1].get_text()



