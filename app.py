from flask import Flask, render_template, redirect

from Scrapers.scraper import scrape_ai_news
from Scrapers.scraper2 import scrape_ai_magazine
from Scrapers.scraper3 import scrape_techcrunch_ai

import json
from datetime import datetime



DATA_FILE = "articles.json"

def save_articles(articles):
    data = {
        "last_updated": datetime.now().strftime("%d %b %Y %H:%M"),
        "articles": articles
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_articles():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"last_updated": None, "articles": []}




app = Flask(__name__)

@app.route("/")
def home():
    data = load_articles()
    return render_template(
        "index.html",
        articles=data["articles"],
        last_updated=data["last_updated"]
    )

@app.route("/refresh")
def refresh():
    all_articles = (
        scrape_ai_news() +
        scrape_ai_magazine() +
        scrape_techcrunch_ai()
    )
    save_articles(all_articles)
    return redirect("/")



if __name__ == "__main__":
    app.run()
