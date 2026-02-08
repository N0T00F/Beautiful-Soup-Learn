from bs4 import BeautifulSoup
import requests
"""Beautiful Soup is a Python library for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping."""
#with open("index.html", "r") as f: #Open HTML file in read mode
    #doc = BeautifulSoup(f, "html.parser") #解析HTML文件
#print(doc.prettify()) #Print out the HTML content in terminal

#tag = doc.title
#tag = doc.find_all("p")[0]
#tag.string = "hello world"

#print(tag.find_all("b"))

url = "https://www.newegg.com/global/hk-en/amd-ryzen-7-9000-series-ryzen-7-9800x3d-granite-ridge-zen-5-socket-am5-desktop-cpu-processor/p/N82E16819113877"
"""
print(result.text)
"""
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)