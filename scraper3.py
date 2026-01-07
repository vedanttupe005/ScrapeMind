import requests
from bs4 import BeautifulSoup

TECHCRUNCH_AI_URL = "https://techcrunch.com/category/artificial-intelligence/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_techcrunch_ai():
    articles = []

    response = requests.get(TECHCRUNCH_AI_URL, headers=HEADERS)
    if response.status_code != 200:
        return articles

    soup = BeautifulSoup(response.text, "html.parser")

    # Select article list items directly
    news_cards = soup.select(
        "ul.wp-block-post-template > li"
    )

    for card in news_cards[:3]:
        title_link = card.select_one("h3 a")
        time_tag = card.select_one("time")
        img_tag = card.select_one("img")

        image_url = None
        if img_tag:
            image_url = (
                img_tag.get("src")
                or img_tag.get("data-src")
                or img_tag.get("srcset", "").split(" ")[0]
            )

        articles.append({
            "title": title_link.get_text(strip=True) if title_link else None,
            "image": image_url,
            "link": title_link["href"] if title_link and title_link.get("href") else None,
            "date": time_tag.get_text(strip=True) if time_tag else None,
            "source": "TechCrunch"
        })

    return articles


if __name__ == "__main__":
    for article in scrape_techcrunch_ai():
        print(article)
