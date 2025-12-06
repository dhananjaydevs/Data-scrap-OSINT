import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, url: str):
        self.url = url

    def crawl(self):
        print(f"DEBUG: FETCHING URL = {self.url}")

        try:
            response = requests.get(
                self.url,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                }
            )
        except Exception as e:
            print("ERROR: Could not fetch URL →", e)
            return [], ""          # ALWAYS RETURN A TUPLE

        if response.status_code != 200:
            print("ERROR: HTTP Status =", response.status_code)
            return [], ""          # ALWAYS RETURN A TUPLE

        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # Extract links
        links = []
        for a in soup.find_all("a"):
            href = a.get("href")
            if href:
                links.append(href)

        # Extract text
        text = soup.get_text(separator="\n", strip=True)

        return links, text         # ALWAYS RETURN A TUPLE
