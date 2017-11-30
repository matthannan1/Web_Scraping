"""
    From Joel Grus's book, 'Data Science From Scratch'
"""

from bs4 import BeautifulSoup
import requests

url = "https://www.barnesandnoble.com/s/data?Ns=P_Publication_Date%7C0"
soup = BeautifulSoup(requests.get(url).text, "html5lib")

tds = soup('td', 'thumbtext')
print(len(tds))
