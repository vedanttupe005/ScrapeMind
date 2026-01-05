# AI News Scraper (Work in Progress)

An automated **AI news scraping project** built using Python and BeautifulSoup.  
The goal of this project is to collect the latest Artificial Intelligence–related news from multiple reliable websites and present them in a clean, structured format.

This project is currently **under development** and will eventually be extended into a **Flask-based web application**.

---

## Project Status

🚧 **Incomplete / In Progress**

- ✅ 3 individual news scrapers implemented  
- ❌ Unified architecture pending  
- ❌ Error handling and logging pending  
- ❌ Flask web interface not yet implemented  

---

## Current Features

- Scrapes AI-related news articles from **multiple websites**
- Extracts:
  - Article title
  - Image URL
  - Article link
  - Published date
- Stores scraped data in Python data structures (lists of dictionaries)

---

## Technologies Used

- **Python**
- **Requests** – for HTTP requests
- **BeautifulSoup (bs4)** – for HTML parsing and scraping
- *(Planned)* **Flask** – for web interface
- *(Planned)* **Jinja2** – for HTML templating

---

## Example Scraper (One of Three)

Below is an example of one scraper used in this project:

```python
import requests
from bs4 import BeautifulSoup

AI_news1 = "https://www.artificialintelligence-news.com/"
articles1 = []

response = requests.get(AI_news1)
soup = BeautifulSoup(response.text, "html.parser")

container = soup.find_all(
    "div",
    class_="elementor-loop-container elementor-grid",
    role="list"
)

news_cards = container[3].find_all("div", recursive=False)

for i in range(3):
    articles1.append({
        "title": news_cards[i].find("h1").get_text(),
        "image": news_cards[i].find("img")["src"],
        "link": news_cards[i].find("a")["href"],
        "date": news_cards[i].find_all("p")[1].get_text()
    })

for article in articles1:
    print(article)
