

````md
# 🤖 ScrapeMind – AI News Aggregator

ScrapeMind is a simple AI news aggregation web application built using **Python, Flask, and BeautifulSoup**.  
It scrapes the latest Artificial Intelligence–related articles from multiple public websites and displays them on a single, clean web page.

This project was built for **learning purposes** to understand web scraping, Flask routing, and frontend rendering with Jinja templates.

---

## 🚀 Features

- Scrapes AI-related news from multiple sources
- Aggregates articles into a single feed
- Displays title, image, source, and date (if available)
- Handles missing data safely (e.g., articles without dates)
- Uses Flask + Jinja for dynamic rendering
- Clean and responsive UI using Bootstrap
- Fresh data fetched on page refresh

---

## 📰 Sources Scraped

- ArtificialIntelligence-News  
- AI Magazine  
- TechCrunch (AI category)

> All data is publicly available and scraped for educational use only.

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **BeautifulSoup (bs4)**
- **Requests**
- **Bootstrap 5**
- HTML + CSS

---

## 📁 Project Structure

```text
ScrapeMind/
│
├── app.py
├── Scrapers/
│   ├── scraper.py          # ArtificialIntelligence-News scraper
│   ├── scraper2.py         # AI Magazine scraper
│   ├── scraper3.py         # TechCrunch AI scraper
│
├── templates/
│   └── index.html
│
├── static/                 # (optional for future CSS/JS)
├── .gitignore
├── README.md
````

---

## ⚙️ How It Works

1. Flask runs a single route (`/`)
2. On each page request:

   * All scraper functions are called
   * Latest articles are fetched
   * Data is combined into a single list
3. Articles are rendered using Jinja templates
4. Page refresh triggers a fresh scrape

---

## ▶️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/vedanttupe005/ScrapeMind.git
cd ScrapeMind
```

2. Create and activate a virtual environment (optional but recommended):

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

---

## ⚠️ Notes & Limitations

* This project scrapes live websites; layout changes may break scrapers.
* Scraping happens on page refresh (no caching yet).
* Not intended for production use.
* No authentication or rate limiting implemented.

---

## 📌 Future Improvements

* Add caching to reduce repeated scraping
* Add source-based filtering
* Sort articles by date
* Add REST API endpoint
* Improve error handling and logging

---

## 📜 Disclaimer

This project is created **strictly for educational purposes**.
All content belongs to its respective owners.

---

## 👨‍💻 Author

**Vedant Tupe**
Learning Flask, Web Scraping, and Backend Development 🚀


