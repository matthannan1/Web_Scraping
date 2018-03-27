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
match_url = "https://www.ancestry.com/dna/matches/my_guid"

payload = {
    "username": "my_username",
    "password": "my_password"}

with requests.Session() as session:
    post = session.post(login_url, data=payload)
    r = session.get(match_url)
    print(r.text)
