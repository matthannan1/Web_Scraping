"""
    From https://kazuar.github.io/scraping-tutorial/
    Going after AncestryDNA matches.

"""

import requests
from lxml import html

# Create session object
session_requests = requests.session()

# Login
login_url = "https://www.ancestry.com/account/signin/"
payload = {
    "username": "matthannan1",
    "password": "Calin2012"}

result = session_requests.get(login_url)
print("Login result: ", result)

result = session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)
print(result)
match_url = "https://www.ancestry.com/dna/matches/B0004280\
            -63E9-45B2-9588-1E7AE812CC1D/"
result = session_requests.get(
    match_url,
    headers=dict(referer=match_url)
)
print(result)
tree = html.fromstring(result.text)

print(str(tree))

