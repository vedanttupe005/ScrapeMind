from flask import Flask, render_template

from Scrapers.scraper import scrape_ai_news
from Scrapers.scraper2 import scrape_ai_magazine
from Scrapers.scraper3 import scrape_techcrunch_ai



app = Flask(__name__)

@app.route("/")
def home():
    ai_news_articles = scrape_ai_news()
    ai_magazine_articles = scrape_ai_magazine()
    techcrunch_ai_articles = scrape_techcrunch_ai()

    all_articles = (
        ai_news_articles +
        ai_magazine_articles +
        techcrunch_ai_articles
    )

    return render_template("index.html", articles=all_articles)


if __name__ == "__main__":
    app.run(debug=True)
