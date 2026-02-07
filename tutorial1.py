from bs4 import BeautifulSoup

with open("index.html", "r") as f: #Open HTML file in read mode
    doc = BeautifulSoup(f, "html.parser") #解析HTML文件
#print(doc.prettify()) #Print out the HTML content in terminal

#tag = doc.title
tag = doc.find_all("p")[0]
#tag.string = "hello world"

print(tag.find_all("b"))