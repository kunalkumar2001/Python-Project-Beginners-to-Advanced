import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv


class Scraper:
    def __init__(self,site):
        self.site = site
        
    def scrape(self):
        headers = {"User-Agent":"Mozilla/5.0"}
        request = urllib.request.Request(self.site, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read()
        soup = BeautifulSoup(html,"html.parser")
        links = set()
        
        
        
        for tag in soup.find_all("a", href = True):
            url = tag["href"]
            
            
            if url.startswith("./"):
                full_url = urljoin(self.site,url)
                links.add(full_url)
        return list(links)        
                
news = "https://news.google.com/"
scraper = Scraper(news)

article_links = scraper.scrape()

with open("news_articles.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Article_URL"])  # header

    for link in article_links:
        writer.writerow([link])

print(f"✅ Saved {len(article_links)} links to news_articles.csv")