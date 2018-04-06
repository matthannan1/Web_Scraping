import time
import getpass
import os
import csv
import ancestryNodes as an
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def make_html(browser):
    # this line is the secret sauce that grabs the
    # FULL html AFTER the js runs
    return browser.find_element_by_tag_name('html').\
            get_attribute('innerHTML')


def delete_old():
    # Delete old files
    print("Deleting old files")
    if os.path.exists("matches.txt"):
        os.remove("matches.txt")
    if os.path.exists("protonodes.csv"):
        os.remove("protonodes.csv")
    if os.path.exists("edges.csv"):
        try:
            os.remove("edges.csv")
        except PermissionError:
            print("edges.csv is open.")
            input("Press any key after you close the file.")
    if os.path.exists("nodes.csv"):
        try:
            os.remove("nodes.csv")
        except PermissionError:
            print("nodes.csv is open.")
            input("Press any key after you close the file.")


def get_credentials():
    # Username and password should be provided by user via input
    username = input("Ancestry username: ")
    # This should be masked
    password = getpass.getpass(prompt='Ancestry Password: ', stream=None)
    # Get max number of pages to scrape.
    print("""
There are 49 matches per page. The default sorting lists closer matches on the
earlier pages. That means the more pages scanned, the more false positives will
be brought in. Based on my results, things start getting really sketchy around
page 25 to 30, so I have the default number of pages to capture as 30. This is
1470 matches, which is more than I will ever be concerned about.
""")
    user_max = input("How many pages of matches would you like to capture? ")
    if user_max == "":
        user_max = 30
    print(int(user_max)*49, "matches coming right up!")
    return username, password, user_max


def open_browser(username, password):
    print("Logging in")
    # Setting some webdriver options
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    # Open login page
    browser = webdriver.Firefox()
    # browser = webdriver.Chrome(chrome_options=chrome_options)
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
    time.sleep(1)
    return browser


def collect_nodes(user_max, browser):
    print("Collecting list of matches.")
    # grab the home page. Looking for the user ID string
    browser.get('https://www.ancestry.com/dna/insights')
    time.sleep(1)
    # We can get our guid now!
    guid = browser.current_url.split("/")[-1]
    # Move on to match page
    prefix = 'https://www.ancestry.com/dna/matches/'
    suffix = '?filterBy=ALL&sortBy=RELATIONSHIP&page='
    match_url = prefix + guid + suffix
    # More data can be collected by looping through and
    # changing the "page=1" stuff
    max = int(user_max) + 1
    for i in range(1, max, 1):
        print("Collecting match page", i)
        browser.get(match_url + str(i))
        time.sleep(1)
        # this line is the secret sauce that grabs the
        # FULL html AFTER the js runs
        html = make_html(browser)
        with open("matches.txt", "a+") as f:
            f.writelines(html)


def get_match_details(browser):
    print("Gathering match details and Shared Matches (ICW).")
    print("This is going to take a while, so go do some traditional genealogy!")
    an.make_data_file("nodes.csv")
    an.make_data_file("edges.csv")
    # Get match URL from protonodes.csv file
    # protonode[0]  protonode[1]    protonode[2]
    # Label         ID              URL
    # This is PER MATCH, so it is a big loop
    with open("protonodes.csv", "r+", newline='') as p:
        protonodes = csv.reader(p)
        total_matches = len(protonodes) - 1
        next(protonodes)
        match = 1
        for protonode in protonodes:
            # Get match guid, will be used in edges.csv
            match_guid = protonode[1]
            # Get the match URL
            node_url = protonode[2].rstrip('\n')
            # Open match page
            browser.get(node_url)
            time.sleep(1)
            # Secret sauce the dynamic HTML
            html = make_html(browser)
            soup = an.make_ram_soup(html)
            # Extract Confidence, cMs, and # of Segments
            flavored_soup = an.get_flavor(soup)
            # Combine the original list and the flavor tuple to one list
            flavored_node = protonode + list(flavored_soup)
            # Write flavored_node list to nodes.csv
            # This gives us all of the basic match details in nodes.csv file
            with open("nodes.csv", "a", newline='') as n:
                nodes = csv.writer(n)
                nodes.writerow(flavored_node)
            # Now it starts getting tricky.
            # Collect ICW and add to edges.csv
            print("Collecting Shared Matches (ICW) from match", match, "of", total_matches +".")
            #page = 1
            # Click the Shared Matches button
            browser.find_element_by_css_selector('.ancBtnM').click()
            time.sleep(1)
            # print("Page #: ", page)
            while True:
                # Secret sauce the dynamic HTML
                html = make_html(browser)
                soup = an.make_ram_soup(html)
                # Get the ICW guids from each page of the MATCH
                matches = an.get_icw_guid(match_guid, soup)
                if matches is False:
                    break
                # else click the "Next" arrow and send the soup to
                # get_icw_guid again.
                else:
                    browser.find_element_by_css_selector('div.matchesPagination:nth-child(2) > div:nth-child(1) > a:nth-child(3)').click()
                    time.sleep(1)
                # Increment the page count number
                # page += 1
            match += 1


# Set up
delete_old()
uname, pwd, max = get_credentials()
browser = open_browser(uname, pwd)
collect_nodes(max, browser)

# Initial match gathering
an.make_data_file("protonodes.csv")
soup = an.make_soup("matches.txt")
match_soup = an.make_matches(soup)
an.make_nodes(match_soup)
print("Basic Match capture completed.")
# print("    protonodes.csv file created")

# Going back in for match details
get_match_details(browser)
browser.close()
print("Complete.")
