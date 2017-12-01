"""
    From Ryan Mitchell's book, 'Web Scraping with Python'
    Chapter 2
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup

# Grab the whole page
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")

# Grab the text formatted in green (proper nouns)
nameList = bsObj.findAll("span", {"class" : "green"})
for name in nameList:
    print(name.get_text())

# Do a count
print()
princeList = bsObj.findAll(text="the prince")
print("\"the prince\" shows", len(princeList), "times.")

# keyword attribute example
print()
allText = bsObj.findAll(id='text')
print(allText[0].get_text())


