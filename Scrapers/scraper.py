import requests
from bs4 import BeautifulSoup

AI_NEWS_URL = "https://www.artificialintelligence-news.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_ai_news():
    articles = []

    response = requests.get(AI_NEWS_URL, headers=HEADERS)
    if response.status_code != 200:
        return articles

    soup = BeautifulSoup(response.text, "html.parser")

    # Select all article cards directly (no indexing hacks)
    news_cards = soup.select(
        "div.elementor-loop-container[role='list'] > div"
    )

    for card in news_cards[:3]:
        title_tag = card.select_one("h1")
        img_tag = card.select_one("img")
        link_tag = card.select_one("a")
        p_tags = card.select("p")

        articles.append({
            "title": title_tag.get_text(strip=True) if title_tag else None,
            "image": img_tag["src"] if img_tag and img_tag.get("src") else None,
            "link": link_tag["href"] if link_tag and link_tag.get("href") else None,
            "date": p_tags[1].get_text(strip=True) if len(p_tags) > 1 else None,
            "source": "Artificial Intelligence News"
        })

    return articles


if __name__ == "__main__":
    for article in scrape_ai_news():
        print(article)
