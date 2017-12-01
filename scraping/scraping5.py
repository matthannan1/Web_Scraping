"""
    From Ryan Mitchell's book, 'Web Scraping with Python'
    Chapter 2
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

# find only descendants that are children
print("Descendants that are children")
print()
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)

print()
print("Siblings")
print()
# find the siblings
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)

print()
print("Dealing with parents")
print()
# Dealing with parents
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
