import time
import getpass
import os
import csv
import ancestryNodes as an
from selenium import webdriver
# from bs4 import BeautifulSoup as bs


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
    an.make_node_file("nodes.csv")
    # Get match URL from protonodes.csv file
    # This is PER MATCH, so it is a big loop
    with open("protonodes.csv", "r+", newline='') as p:
        protonodes = csv.reader(p)
        next(protonodes)
        for protonode in protonodes:
            print(protonode[1])
            if os.path.exists("details.txt"):
                os.remove("details.txt")
            node_url = protonode[2].rstrip('\n')
            # Open match page
            browser.get(node_url)
            time.sleep(3)
            # Secret sauce the dynamic HTML
            html = browser.find_element_by_tag_name('html').get_attribute('innerHTML')
            # Collect individual details
            with open("details.txt", "w") as f:
                f.writelines(html)
            # Extract conf, cm, and segs
            soup = an.make_soup("details.txt")
            flavored_soup = an.get_flavor(soup)
            # print(flavored_soup)
            # Combine the original list and the flavor tuple to one list
            flavored_node = protonode + list(flavored_soup)
            # Write to nodes.csv
                # still have node as list, so add items as list items
                # not as easy as it sounds. Either two files or Pandas.
            with open("nodes.csv", "a", newline='') as n:
                nodes = csv.writer(n)
                nodes.writerow(flavored_node)    
                
            # Collect ICW and add to edges.csv


# Set up
delete_old()
uname, pwd = get_credentials()
browser = open_browser(uname, pwd)
collect_nodes(browser)

# Initial match gathering
an.make_node_file("protonodes.csv")
soup = an.make_soup("matches.txt")
match_soup = an.make_matches(soup)
an.make_nodes(match_soup)
print("protonodes.csv file created")

# Going back in for match details
get_details(browser)
