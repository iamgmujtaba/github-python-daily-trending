#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def debug_title_extraction():
    url = "https://github.com/trending/python?since=daily"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    
    repos = soup.find_all("article", class_="Box-row")
    first_repo = repos[0]
    
    print("H2 element:")
    h2 = first_repo.find("h2")
    print(h2.prettify())
    
    print("\nH2 text extraction methods:")
    print(f"get_text(): '{h2.get_text()}'")
    print(f"get_text(strip=True): '{h2.get_text(strip=True)}'")
    
    # Try to find the actual repo link
    h2_link = h2.find("a")
    if h2_link:
        href = h2_link.get("href", "")
        print(f"Link href: '{href}'")
        title = href.strip("/")
        print(f"Title from href: '{title}'")

if __name__ == "__main__":
    debug_title_extraction()
