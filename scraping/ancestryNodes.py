import csv
# import pprint
from bs4 import BeautifulSoup as bs


def make_data_file(filename):
    if filename == "nodes.csv" or filename == "protonodes.csv":
        header = ['Label', 'ID', 'URL', 'Confidence',
                  'cMs', 'Segments', 'Notes']
    if filename == "edges.csv":
        header = ['Source', 'Target']
    with open(filename, "w", newline='') as f:
        data_file = csv.writer(f)
        data_file.writerow(header)


def make_soup(filename):
    with open(filename, "r") as html:
        souptml = bs(html, 'html.parser')
    return souptml


def make_ram_soup(html):
    return bs(html, 'html.parser')


def make_matches(souptml):
    # Build the "list" of matches from html a class
    match_soup = souptml.findAll('a', {"class": "textxlrg"})
    return match_soup


def make_nodes(matches):
    with open("protonodes.csv", "a", newline='') as p:
        node_file = csv.writer(p)
        for match in matches:
            name = match.contents[0]
            match_name = str(name)[8:-9]
            # print(match_name)
            id = match.get('href')
            match_id = str(id).split('?')[0].split('/')[3]
            # print(match_id)
            link = 'https://www.ancestry.com/dna/' + id
            node_file.writerow([match_name, match_id, link])


def get_flavor(souptml):
    confidence = ""
    cm = ""
    segs = ""
    # Find Confidence, cMs, Segements, and Notes
    confident_soup = souptml.findAll('span', {"class": "matchPercent"})
    try:
        confidence = str(confident_soup).split(': ')[1].split('\n')[0]
    except IndexError:
        confidence = ""
    # Find cM and Segments
    cm_soup = souptml.findAll('div', {"data-classes": "sharedSegments"})
    cm = str(cm_soup).split('<p>')[1].split('</p>')[0].split(' ')[0]
    segs = str(cm_soup).split('<p>')[1].split('</p>')[0].split(' ')[4]
    # Find Notes
    notes_soup = souptml.findAll('span', {'data-ng-if': "!showShortNote"})
    try:
        note = str(notes_soup).split('>')[1].rstrip('</span>]')
    except IndexError:
        note = ""
    return confidence, cm, segs, note


def get_icw_guid(match_guid, souptml):
    # This is PER MATCH >>>AND<<< PER PAGE of Shared Matches!
    # I am thinking that we need a while loop running,
    # with False being tripped when len(icw_soup_list) < 50.
    # While True, page2, page3, page4, etc
    try:
        icw_soup = souptml.findAll("a", {'class':
                                   "matchesImage matchesInCommonImage"})
    except IndexError:
        return False
    icw_soup_list = list(icw_soup)
    #print("ICW page length: ", len(icw_soup_list))
    for icw in icw_soup_list:
        icw_guid = str(icw).split('?filterBy')[0].split('match/')[1]
        icw_data = [match_guid, icw_guid]
        # Write to edges.csv
        with open("edges.csv", "a", newline='') as e:
            edges = csv.writer(e)
            edges.writerow(icw_data)

