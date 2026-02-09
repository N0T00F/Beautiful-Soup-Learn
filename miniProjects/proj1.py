import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
movies = []
for movie in soup.select(".ipc-metadata-list-summary-item"):
    title_element = movie.select_one("h3.ipc-title__text")
    title = title_element.text.strip() if title_element else "N/A"
    metadata_items = movie.select("span.cli-title-metadata-item")
    if len(metadata_items) >= 1:
        year = metadata_items[0].text.strip()
    else:
        year = "N/A"
    rating_element = movie.select_one("span.ipc-rating-star--rating")
    rating = rating_element.text.strip() if rating_element else "N/A"
    movies.append({"Title": title, "Year": year, "Rating": rating})
df = pd.DataFrame(movies)
df.index = df.index + 1
df.to_csv("top_movies.csv", index_label="Rank")
print(df)

# Note: It only shows the top 25 movies.