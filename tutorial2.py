from bs4 import BeautifulSoup
import re

with open ("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_add(text = re.compile("\$.*"))