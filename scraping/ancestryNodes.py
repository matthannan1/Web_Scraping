import csv
from bs4 import BeautifulSoup as bs


def make_soup(filename):
    with open(filename, "r") as html:
        souptml = bs(html, 'html.parser')
    return souptml


def make_matches(souptml):
    # Build the "list" of matches from html a class
    match_soup = souptml.findAll('a', {"class": "textxlrg"})
    return match_soup


def make_node_file():
    with open("nodes.csv", "w", newline = '') as n:
        node_file = csv.writer(n)
        node_file.writerow(['ID', 'Label', 'URL', 'Confidence', 'cMs', 'Segments', 'Notes'])


def make_nodes(matches):
    with open("nodes.csv", "w") as n:
        node_file = csv.writer(n)
        for match in matches:
            name = match.contents[0]
            match_name = str(name)[8:-9]
            id = match.get('href')
            match_id = str(id).split('?')[0].split('/')[3]
            link = 'https://www.ancestry.com/dna/' + id
            node_file.writerow([match_id, match_name, link])


def get_flavor(souptml):
    # return the Confidence, cMs and segements
    confident_soup = souptml.findAll('span', {"class": "matchPercent"})
    # print(confident_soup)
    confidence = str(confident_soup).split(': ')[1].split('\n')[0]
    # print(confidence)
    cm_soup = souptml.findAll('div', {"data-classes": "sharedSegments"})
    cm = str(cm_soup).split('<p>')[1].split('</p>')[0].split(' ')[0]
    segs = str(cm_soup).split('<p>')[1].split('</p>')[0].split(' ')[4]
    # print(cm)
    # print(segs)
    return confidence, cm, segs

    





"""
def add_node_details():
    # if ids match, append to nodes.csv line in

    # Confidence,cMs,Segments,Notes\n order
    pass
 

def get_node_url():
    with open("nodes.csv", "r+") as n:
    nodes = n.readlines()
    for node in nodes:
        node_line = node.split(',')
        node_url = node_line[2].rstrip('\n')
        return node_url
        """
