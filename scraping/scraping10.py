"""
    From https://github.com/kennethreitz/requests-html
    Going after AncestryDNA matches.

"""

from requests_html import HTMLSession


# Create session object
session = HTMLSession()

# Login setup
login_url = "https://www.ancestry.com/account/signin/"
payload = {
    "username": "matthannan1",
    "password": "Calin2012"}

r = session.get(login_url)
print("Login setup: ", r)

# Login
r = session.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)
print("Login result: ", r)
print()


# Grab a list of all links on the page, as–is (anchors excluded):
print(r.html.links)
print()

trees = r.html.find('#navTrees', first=True)
# print(trees.text)





match_url = "https://www.ancestry.com/dna/matches/"
result = session.get(
    match_url,
    headers=dict(referer=match_url)
)
print(result)
result.html.render()

