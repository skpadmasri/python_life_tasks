import pandas as pd
import requests
from bs4 import BeautifulSoup
response = requests.get("https://quotes.toscrape.com/")
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
quotes = soup.find_all("div", class_="quote")
quote = []
for i in quotes:
    d = i.find("span", class_="text").get_text()
    quote.append(d)
authors = soup.find_all("small", class_="author")
author = []
for i in authors:
    d = i.get_text()
    author.append(d)
tags = soup.find_all("div", class_="tags")
tag = []
for i in tags:
    d = i.get_text(strip=True)
    tag.append(d)
author_links = []
for i in quotes:
    d = i.find("a", href=True).get("href")
    author_links.append("https://quotes.toscrape.com" + d)
tag_count = []
for i in tags:
    d = len(i.find_all("a", class_="tag"))
    tag_count.append(d)
df = pd.DataFrame()
df["quotes"] = quote
df["authors"] = author
df["tags"] = tag
df["author_links"] = author_links
df["tag_count"] = tag_count
print(df)
df.to_csv("quotes.csv", index=False)
