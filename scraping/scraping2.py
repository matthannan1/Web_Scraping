"""
    From Joel Grus's book, 'Data Science From Scratch'
"""

from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.iana.org/domains/reserved").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')   # or just soup.p
first_paragraph_text = soup.p.text
first_paragraph_words = first_paragraph_text.split()

first_paragraph_id = soup.p['id']   # raise KeyError if no 'id'
first_paragraph_id2 = soup.p.get('id')   # returns None if no 'id'

all_paragraphs = soup.find_all('p')   # or soup.('p') - see above
paragraphs_with_ids = [p for p in all_paragraphs if p.get('id')]

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in all_paragraphs if 'important' in p.get('class', [])]

# DANGER
spans_inside_divs = [span for div in soup('div') for span in div('span')]

