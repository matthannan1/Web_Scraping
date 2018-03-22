"""
    From https://www.youtube.com/watch?v=bhYulVzYRng
    and https://www.youtube.com/watch?v=--vqRAkcWoM
    Going after AncestryDNA matches.

"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
chrome_path = r"C:\Users\matth\GitRepos\Web_Scraping\scraping\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

# Get to Login Page
login_url = "https://www.ancestry.com/account/signin/"
driver.get(login_url)

usernameID = "username"
passwordID = "password"
loginButtonID = "loginButton"

result = session_requests.get(login_url)
print("Get to Login page: ", result)

# Login
login_result = session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)
print("Login result: ", login_result)

# Selenium
driver.get("https://www.ancestry.com/dna/insights/")
driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[1]/div[4]/div/article/div[2]/div[1]/div[2]/div/div[2]/div[1]/ul/li[3]""").click()
matches = driver.find_elements_by_class_name("matchesName noTopSpacing")
for match in matches:
    print(match)









"""

# Create session object
session_requests = requests.session()

# Get to Login Page
login_url = "https://www.ancestry.com/account/signin/"
payload = {
    "username": "matthannan1",
    "password": "Calin2012"}

result = session_requests.get(login_url)
print("Get to Login page: ", result)

# Login
login_result = session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)
print("Login result: ", login_result)

# Get to match page
match_url = "https://www.ancestry.com/dna/matches/B0004280-63E9-45B2-9588-1E7AE812CC1D?filterBy=ALL&sortBy=RELATIONSHIP&page=1"
match_result = session_requests.get(match_url, headers=dict(referer=match_url))

matches_page = BeautifulSoup(match_result.text, 'html.parser')
with open("matches.txt", "w") as out_file:
    out_file.writelines(str(matches_page))
print("Done.")
"""
