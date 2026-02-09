import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

script_tag = soup.find("script", id="__NEXT_DATA__")
movies_data = []

if script_tag:
    data = json.loads(script_tag.string)
    edges = data['props']['pageProps']['pageData']['chartTitles']['edges']
    
    for rank, item in enumerate(edges, start=1):
        node = item['node']
        
        title = node['titleText']['text']
        
        year_data = node.get('releaseYear')
        year = year_data.get('year') if year_data else "N/A"
        
        rating_data = node.get('ratingsSummary')
        rating = rating_data.get('aggregateRating') if rating_data else "N/A"
        
        movies_data.append({
            "Rank": rank, 
            "Title": title,
            "Year": year,
            "Rating": rating
        })

df = pd.DataFrame(movies_data)
df.set_index("Rank", inplace=True)
pd.set_option('display.max_rows', None)
df.to_csv("top_movies_all.csv", index_label="Rank")
df.index = df.index + 1
print(f"Total Movies: {len(df)}")
print(df.head(250)) # Show top 250 movies