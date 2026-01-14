# 🤖 ScrapeMind – AI News Aggregator

ScrapeMind is a Python-based AI news aggregation web application built using **Flask and BeautifulSoup**.  
It collects the latest Artificial Intelligence–related articles from multiple public sources, stores them in a local JSON file, and displays them on a clean, responsive web interface.

This project was built for **learning and demonstration purposes**, focusing on web scraping, backend architecture, and Flask-based rendering.

---

## 🚀 Features

- Scrapes AI-related news from multiple public sources
- Aggregates articles into a single unified feed
- Stores scraped data in a JSON file (persistent storage)
- Overwrites old data on refresh to keep content up to date
- Displays title, image, source, and date (if available)
- Handles missing or optional data safely
- Clean, dark-themed UI using Bootstrap
- Manual refresh route to control scraping frequency
- Fast page loads (scraping decoupled from rendering)

---

## 📰 Sources Scraped

- Hugging Face blog  
- AI Magazine  
- TechCrunch (AI category)

> All data is publicly available and used strictly for educational purposes.

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **BeautifulSoup (bs4)**
- **Requests**
- **Bootstrap 5**
- HTML + CSS
- JSON (for data storage)

---

## 📁 Project Structure

```text
ScrapeMind/
│
├── app.py
├── articles.json            # Stored scraped articles (auto-generated)
│
├── Scrapers/
│   ├── scraper.py           # ArtificialIntelligence-News scraper
│   ├── scraper2.py          # AI Magazine scraper
│   ├── scraper3.py          # TechCrunch AI scraper
│
├── templates/
│   └── index.html
│
├── static/                  # Optional (CSS / assets)
├── .gitignore
├── README.md
```

---

## ⚙️ How It Works

1. Scraper functions collect articles from multiple sources.
2. On calling the `/refresh` route:
   - All scrapers run
   - Latest articles are aggregated
   - Existing `articles.json` file is **overwritten** with fresh data
3. The home route (`/`) reads data from `articles.json`
4. Articles are rendered using Flask + Jinja templates
5. Page refresh **does not trigger scraping**, ensuring better performance and safety

---

## 🔄 Routes

- `/` → Displays articles from the stored JSON file  
- `/refresh` → Re-runs all scrapers and overwrites the JSON data

This separation avoids unnecessary scraping on every page reload.

---

## ▶️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/vedanttupe005/ScrapeMind.git
cd ScrapeMind
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install flask requests beautifulsoup4
```

4. Run the Flask app:

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000/
```

6. To fetch fresh articles, visit:

```
http://127.0.0.1:5000/refresh
```

---

## ⚠️ Notes & Limitations

- This project scrapes live websites; layout changes may break scrapers.
- Scraping is manual to avoid excessive requests.
- No authentication or rate limiting implemented.
- Not intended for production use.

---

## 📌 Future Improvements

- Replace JSON storage with SQLite or PostgreSQL
- Add automatic scheduled scraping
- Add source-based filtering
- Sort articles by date
- Add REST API endpoints
- Improve logging and error handling

---

## 📜 Disclaimer

This project is created **strictly for educational purposes**.  
All content belongs to its respective owners.

---

## 👨‍💻 Author

**Vedant Tupe**  
Final-year diploma student | Project-driven developer  
Learning Flask, Web Scraping, and Backend Development 🚀


