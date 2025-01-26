import requests
import re
from bs4 import BeautifulSoup
import logging
from typing import Optional

class WebsiteScraper:
    @staticmethod
    def scrape_homepage(url):
        cookies: Optional[dict] = None
        headers: Optional[dict] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        
        try:
            response = requests.get(
                url,
                timeout=15,
                headers=headers,
                cookies=cookies if cookies else {},
            )
            # response = requests.get(url, timeout=10)
            # response.raise_for_status()
            parsed = BeautifulSoup(response.text, "html.parser")
            text = parsed.get_text(" ")
            text = re.sub("[ \t]+", " ", text)
            text = re.sub("\\s+\n\\s+", "\n", text)
            return text
        
        except requests.RequestException as e:
            logging.error(f"Scraping error: {e}")
            return None