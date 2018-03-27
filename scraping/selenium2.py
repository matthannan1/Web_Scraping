"""
    From http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php
    Going after AncestryDNA.

    Requests is failing to capture the innerHTML stuff that is being created by JS.
"""

import time
import getpass
from bs4 import BeautifulSoup as soup
from selenium import webdriver

# Username and password should be provided by user via input
username = input("Ancestry username: ")
# This should be masked
password = getpass.getpass(prompt='Ancestry Password: ', stream=None)

# Open login page
browser = webdriver.Chrome()
login_url = 'https://www.ancestry.com/account/signin'
browser.get(login_url)

# Login
username_element = browser.find_element_by_id("username")
password_elememt = browser.find_element_by_id("password")
username_element.send_keys(username)
password_elememt.send_keys(password)
submitButton = browser.find_element_by_id("loginButton")
submitButton.click()
# wait for home page to load
time.sleep(7)

# grab the home page. Looking for that user ID string
browser.get('https://www.ancestry.com/dna/insights')
time.sleep(3)
# We can get our guid now!
guid = browser.current_url.split("/")[-1]

# Assume it has some js that needs to run
dna_html_page = browser.find_element_by_tag_name('html').get_attribute('innerHTML')
dna_soup = soup(dna_html_page, "html5lib")


# Move on to match page
suffix = '?filterBy=ALL&sortBy=RELATIONSHIP&page='
prefix = 'https://www.ancestry.com/dna/matches/'
match_url = prefix + guid + suffix
# More data can be collected by looping through and changing the "page=1" type stuff
for i in range(1, 11, 1):
    browser.get(match_url + str(i))
    time.sleep(7)

    # this line is the secret sauce that grabs the FULL html AFTER the js runs
    html = browser.find_element_by_tag_name('html').get_attribute('innerHTML')
    with open("matches.txt", "w+") as f:
        f.writelines(html)


# Now extract the results of the JS inner HTML
# innerHTML = browser.execute_script("return document.body.innerHTML")
# print(len(innerHTML))
# base_url = 'https://www.ancestry.com'
# browser.get(base_url)
# browser.find_element_by_link_text("DNA").click()
# html = browser.page_source

# soup = BeautifulSoup(innerHTML, "lxml")

# for tag in soup.find_all('title'):
#    print(tag.text)
