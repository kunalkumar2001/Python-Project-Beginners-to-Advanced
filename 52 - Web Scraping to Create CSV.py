import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser") 
articles = []

for item in soup.find_all("h2"):
    title = item.get_text(strip=True)
    if title:
        articles.append(title)
        
df = pd.DataFrame(articles, columns=["Headline"])
df.to_csv("bbc_news.csv", index=False)

print("News Headline saved to bbc_news.csv")