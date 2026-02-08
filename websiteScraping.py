from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.newegg.com/global/hk-en/p/pl?Submit=Pers&ste=84&pmid=C850E5C1-BAE5-4322-8A99-5432E152F2C1&fbid=2&ispreview=1&gid=SingleGroup&nvtc=248326808.0001.bf84bf5a0.1770474579&di=19-113-877%2C20-982-129%2C83-151-690%2C14-137-965&ps=0').text
soup = BeautifulSoup(html_text, 'lxml')
prices = soup.find_all('li', class_ = 'price-current')
for price in prices:
    price_detail = price.find('strong')
    if price_detail:
        print(price_detail.string)