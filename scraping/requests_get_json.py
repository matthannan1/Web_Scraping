"""
Based on this web site:
https://ianlondon.github.io/blog/web-scraping-discovering-hidden-apis/

I used his method and found match data here:
https://dnahomeaws.ancestry.com/dna/secure/tests/B0004280-63E9-45B2-9588-1E7AE812CC1D/matches?filterBy=ALL&sortBy=RELATIONSHIP&page=1
and Shared Match data here:
https://dnahomeaws.ancestry.com/dna/secure/tests/B0004280-63E9-45B2-9588-1E7AE812CC1D/matchesInCommon?filterBy=ALL&sortBy=RELATIONSHIP&page=1&matchTestGuid=861ABA15-2DEE-495B-A843-42166C59F80C

First trick will be logging in without a browser.

"""

import requests
import json
import getpass
import time
from pprint import pprint


def get_guids(raw_data):
    tests = {}
    for i in range(len(raw_data['data']['completeTests'])):
        guid = (raw_data['data']['completeTests'][i]['guid'])
        # print("Test {}: {} {}".format(num, id['testSubject']['displayName'], id['guid']))
        tester = (raw_data['data']['completeTests'][i]['testSubject']['givenNames']
                  + " " + raw_data['data']['completeTests'][i]['testSubject']['surname'])
        tests[i+1] = tester, guid
    # for k, v in tests.items():
        # print("Test", str(k) + ":", v[0], v[1])
    return tests


def get_credentials():
    # Username and password should be provided by user via input
    username = input("Ancestry username: ")
    # This should be masked
    password = getpass.getpass(prompt='Ancestry Password: ', stream=None)
    # Get max number of pages to scrape.
    print("""
There are 48 matches per page. The default sorting lists closer matches on the
earlier pages. That means the more pages scanned, the more false positives will
be brought in. Based on my results, things start getting really sketchy around
page 25 to 30, so I have the default number of pages to capture as 30. This is
1440 matches, which is more than I will ever be concerned about.
""")
    user_max = input("How many pages of matches would you like to capture? ")
    user_max = int(user_max)
    if user_max == "":
        user_max = 30
    print(user_max*48, "matches coming right up!")
    return username, password, user_max


# Create session object
session_requests = requests.session()
# Get to Login Page
login_url = "https://www.ancestry.com/account/signin"
# get_guid_url = "https://www.ancestry.com/dna/insights"
get_guids_url = "https://dnahomeaws.ancestry.com/dna/secure/tests/"
suffix1 = "/matches?filterBy=ALL&sortBy=RELATIONSHIP&page=1"
suffix2 = "/matchesInCommon?filterBy=ALL&sortBy=RELATIONSHIP&page=1&matchTestGuid="


username, password, max_pages = get_credentials()
payload = {
    "username": username,
    "password": password}

with session_requests as session:
    post = session.post(login_url, data=payload)
    # Get the raw JSON for the tests
    raw = session.get(get_guids_url).text
    # parse it into a dict
    data = json.loads(raw)
    test_guids = get_guids(data) # get the list of tests available
    print()
    for k, v in test_guids.items(): # Print them out...work on formatting
        print("Test", str(k) + ":", v[0], v[1])
    print()
    test_selection = int(input("Select the test that you want to gather matches for: "))
    guid = test_guids[test_selection][1]
    # print(guid)
    # Start to gather match data using number of pages variable
    test_url = get_guids_url + guid + suffix1
    matches = session.get(test_url).text
    print(matches)

