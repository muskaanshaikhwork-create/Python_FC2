# Project 6: Web Scraping Using Beautiful Soup

# Problem Statement:
# The task is to scrape the list of largest companies in US by revenue from
# Wikipedia using Beautiful Soup in Python. The data required includes the
# rank, name of company, Industry, Revenue, Revenue growth, Headquarters.

# Question:
# What is the process to extract data from the Wikipedia website using
# Beautiful Soup in Python? Specifically, how can we extract the rank,
# name of the company, Industry, Revenue, Revenue growth, Headquarters
# for the top US companies by Revenue?

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="wikitable")

rows = table.find_all("tr")

data = []

for row in rows[1:]:
    cells = row.find_all(["th", "td"])

    if cells:
        row_data = [cell.get_text(strip=True) for cell in cells]
        data.append(row_data)

df = pd.DataFrame(data)

print(df.head())