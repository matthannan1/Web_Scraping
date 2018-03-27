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
    "username": "my_username",
    "password": "my_password"}

result = session_requests.get(login_url)
print("Login result: ", result)

result = session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)
print(result)
match_url = "https://www.ancestry.com/dna/matches/my_guid/"
result = session_requests.get(
    match_url,
    headers=dict(referer=match_url)
)
print(result)
tree = html.fromstring(result.text)

print(str(tree))

