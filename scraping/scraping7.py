"""
    From https://pybit.es/requests-session.html
    Going after AncestryDNA matches.

"""

import requests
# from bs4 import BeautifulSoup

# Create session object
session_requests = requests.session()

# Get to Login Page
login_url = "https://www.ancestry.com/account/signin"
match_url = "https://www.ancestry.com/dna/matches/B0004280-63E9-45B2-9588-1E7AE812CC1D"

payload = {
    "username": "matthannan1",
    "password": "Calin2012"}

with requests.Session() as session:
    post = session.post(login_url, data=payload)
    r = session.get(match_url)
    print(r.text)
