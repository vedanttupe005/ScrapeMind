import requests
from bs4 import BeautifulSoup

AI_MAGAZINE_URL = "https://aimagazine.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_ai_magazine():
    articles = []

    response = requests.get(AI_MAGAZINE_URL, headers=HEADERS)
    if response.status_code != 200:
        return articles

    soup = BeautifulSoup(response.text, "html.parser")

    # Select article cards directly
    news_cards = soup.select(
        "div.GridWrapper_flex__1NgfS > div"
    )

    for card in news_cards[:3]:
        link_tag = card.select_one("a")
        img_tag = card.select_one("img")

        articles.append({
            "title": link_tag.get_text(strip=True) if link_tag else None,
            "image": img_tag["src"] if img_tag and img_tag.get("src") else None,
            "link": (
                AI_MAGAZINE_URL + link_tag["href"]
                if link_tag and link_tag.get("href")
                else None
            ),
            "source": "AI Magazine"
        })

    return articles


if __name__ == "__main__":
    for article in scrape_ai_magazine():
        print(article)
