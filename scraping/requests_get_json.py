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
import os
import csv
from pprint import pprint


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


def make_data_file(filename):
    if filename == "nodes.csv" or filename == "protonodes.csv":
        header = ['Label', 'ID', 'Starred', 'Confidence',
                  'cMs', 'Segments', 'Notes']
    if filename == "edges.csv":
        header = ['Source', 'Target']
    with open(filename, "w", newline='') as f:
        data_file = csv.writer(f)
        data_file.writerow(header)


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
There are about 50 matches per page. The default sorting lists closer matches
on the earlier pages. That means the more pages scanned, the more false positives
will be brought in. Based on my results, things start getting really sketchy
around page 25 to 30, so I have the default number of pages to capture as 30.
This is 1500 matches, which is more than I will ever be concerned about.
""")
    user_max = input("How many pages of matches would you like to capture? ")
    if user_max == "":
        user_max = "30"
    user_max = int(user_max)    
    print(user_max*50, "matches coming right up!")
    return username, password, user_max


def harvest_matches(matches):
    data = json.loads(matches)
    # c = 0
    #print("Groups:", len(data['matchGroups']))
    for i in range(len(data['matchGroups'])):
        for m in range(len(data['matchGroups'][i]['matches'])):
            # print(data['matchGroups'][i]['matches'][m]['testGuid'])
            # ['Label', 'ID', 'Starred', 'Confidence', 'cMs', 'Segments', 'Notes']
            match_name = data['matchGroups'][i]['matches'][m]['matchTestDisplayName']
            match_guid = data['matchGroups'][i]['matches'][m]['testGuid']
            match_starred = data['matchGroups'][i]['matches'][m]['starred']
            match_confidence = data['matchGroups'][i]['matches'][m]['confidence']
            match_cms = data['matchGroups'][i]['matches'][m]['sharedCentimorgans']
            match_segments = data['matchGroups'][i]['matches'][m]['sharedSegments']
            match_notes = data['matchGroups'][i]['matches'][m]['note']
            match_starred = data['matchGroups'][i]['matches'][m]['starred']
            # c += 1
            match_details = (match_name, match_guid, match_starred, match_confidence, match_cms, match_segments, match_notes)
            with open("nodes.csv", "a", newline='') as n:
                nodes = csv.writer(n)
                nodes.writerow(match_details)
    # print("Matches:", c)


# Create session object
session_requests = requests.session()
# Get to Login Page
login_url = "https://www.ancestry.com/account/signin"
# get_guid_url = "https://www.ancestry.com/dna/insights"
get_guids_url = "https://dnahomeaws.ancestry.com/dna/secure/tests/"
suffix1 = "/matches?filterBy=ALL&sortBy=RELATIONSHIP&page="  # note the no page number
suffix2 = "/matchesInCommon?filterBy=ALL&sortBy=RELATIONSHIP&page=1&matchTestGuid="

# Delete old files
delete_old()
# Create new files
make_data_file("nodes.csv")
make_data_file("edges.csv")

# Login
username, password, max_pages = get_credentials()
payload = {
    "username": username,
    "password": password}

# Start Session
with session_requests as session:
    post = session.post(login_url, data=payload)
    # Get the raw JSON for the tests
    raw = session.get(get_guids_url).text
    # parse it into a dict
    data = json.loads(raw)
    test_guids = get_guids(data)  # get the list of tests available
    print()
    for k, v in test_guids.items():  # Print them out...work on formatting
        print("Test", str(k) + ":", v[0], v[1])
    print()
    test_selection = int(input("Select the Test # that you want to gather matches for: "))
    guid = test_guids[test_selection][1]
    # print(guid)
    # Start to gather match data using number of pages variable
    # suffix1 ends in the "page=1"
    # obviously, this needs to be fixed to capture more than the
    # first page of matches.
    # look at ancestryDNA.py collect_nodes() function.
    print("Gathering match details. Please wait.")
    for page_number in range(1, max_pages+1):
        test_url = get_guids_url + guid + suffix1 + str(page_number)
        matches = session.get(test_url).text
        harvest_matches(matches)
        time.sleep(1)
    # print(matches)
