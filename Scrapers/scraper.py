import requests
from bs4 import BeautifulSoup

AI_NEWS_URL = "https://huggingface.co/blog"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}


def scrape_ai_news():
    articles = []

    response = requests.get(AI_NEWS_URL, headers=HEADERS)
    if response.status_code != 200:
        return articles

    soup = BeautifulSoup(response.text, "html.parser")

    # Select all article cards directly (no indexing hacks)
    news_cards = soup.select(
        "div.flex.flex-col.gap-6 a"
    )


    for card in news_cards[:3]:
        title_tag = card.select_one("h2")
        link_tag = card
        # p_tags = card.select("span")

        img_src = card.select_one("img")["src"] if card.select_one("img") else None
        if img_src and img_src.startswith("/"):
            img_src = "https://huggingface.co" + img_src


        articles.append({
            "title": title_tag.get_text(strip=True) if title_tag else None,
            "image": img_src,
            "link": AI_NEWS_URL+link_tag["href"] if link_tag and link_tag.get("href") else None,
            # "date": p_tags[0].get_text(strip=True) if len(p_tags) > 1 else None,
            "source": "Hugging Face Blog"
        })

    return articles


if __name__ == "__main__":
    for article in scrape_ai_news():
        print(article)
