import time
import getpass
import os
import ancestryNodes as an
from selenium import webdriver


def delete_old():
    # Delete old files
    if os.path.exists("matches.txt"):
        os.remove("matches.txt")
    if os.path.exists("*.csv"):
        os.remove("*.csv")


def get_credentials():
    # Username and password should be provided by user via input
    username = input("Ancestry username: ")
    # This should be masked
    password = getpass.getpass(prompt='Ancestry Password: ', stream=None)
    return username, password


def collect_nodes(username, password):
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
    # Move on to match page
    prefix = 'https://www.ancestry.com/dna/matches/'
    suffix = '?filterBy=ALL&sortBy=RELATIONSHIP&page='
    match_url = prefix + guid + suffix
    # More data can be collected by looping through and changing the "page=1" stuff
    for i in range(1, 2, 1):
        browser.get(match_url + str(i))
        time.sleep(7)
        # this line is the secret sauce that grabs the FULL html AFTER the js runs
        html = browser.find_element_by_tag_name('html').get_attribute('innerHTML')
        with open("matches.txt", "a+") as f:
            f.writelines(html)


# def get_details():
    # Get match URL from nodes.csv file
    # Create new browser object in Selenium
    # Collect individual details and append to nodes.csv
    # Collect ICW and add to edges.csv


delete_old()
uname, pwd = get_credentials()
collect_nodes(uname, pwd)
an.make_node_file()
soup = an.make_soup()
tester = an.get_tester_name(soup)
print("AncestryDNA results for: ", tester)
match_soup = an.make_matches(soup)
an.make_nodes(match_soup)
print("nodes.csv file created")
