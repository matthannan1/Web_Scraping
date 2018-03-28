import time
import getpass
import os
import csv
import ancestryNodes as an
from selenium import webdriver
from bs4 import BeautifulSoup as bs


def delete_old():
    # Delete old files
    print("Deleting old files")
    if os.path.exists("*.txt"):
        os.remove("*.txt")
    if os.path.exists("*.csv"):
        os.remove("*.csv")


def get_credentials():
    # Username and password should be provided by user via input
    username = input("Ancestry username: ")
    # This should be masked
    password = getpass.getpass(prompt='Ancestry Password: ', stream=None)
    return username, password


def open_browser(username, password):
    print("Logging in")
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
    return browser


def collect_nodes(browser):
    print("Collecting list of matches.")
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


def get_details(browser):
    print("Gathering match details.")
    # Get match URL from nodes.csv file
    with open("nodes.csv", "r+") as n:
        nodes = csv.reader(n)
        next(nodes)
        for node in nodes:
            node_url = node[2].rstrip('\n')
            print(node_url)
            # Create new browser object in Selenium
            # Maybe not, otherwise all that login stuff needs to run again.
            # See about passing browser object
            browser.get(node_url)
            time.sleep(3)
            html = browser.find_element_by_tag_name('html').get_attribute('innerHTML')
            # Collect individual details
            # temp write to file to exlore structure
            with open("details.txt", "a+") as f:
                f.writelines(html)
            # Append to nodes.csv
                # still have node as list, so add items as list items
            # Collect ICW and add to edges.csv

# Set up
delete_old()
uname, pwd = get_credentials()
browser = open_browser(uname, pwd)
collect_nodes(browser)

# Initial match gathering
an.make_node_file()
soup = an.make_soup("matches.txt")
# tester = an.get_tester_name(soup)
# print("AncestryDNA results for: ", tester)
match_soup = an.make_matches(soup)
an.make_nodes(match_soup)
print("Initial nodes.csv file created")

# Going back in for match details
get_details(browser)
soup = an.make_soup("details.txt")


