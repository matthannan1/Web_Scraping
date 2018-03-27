from bs4 import BeautifulSoup as bs


def make_soup():
    with open("matches.txt", "r") as html:
        souptml = bs(html, 'html.parser')
    return souptml


def get_tester_name(souptml):
    # Get tester's name
    tester = souptml.findAll('div', {"class": "userCardTitle"})
    tester_name = str(tester).split('>')[1].split('<')[0]
    return tester_name


def make_matches(souptml):
    # Build the "list" of matches from html a class
    match_soup = souptml.findAll('a', {"class": "textxlrg"})
    return match_soup


def make_node_file():
    with open("nodes.csv", "w") as n:
        n.write('ID,Label,URL,Confidence,cMs,Segments,Notes\n')


def make_nodes(matches):
    with open("nodes.csv", "a+") as n:
        for match in matches:
            name = match.contents[0]
            match_name = str(name)[8:-9]
            id = match.get('href')
            match_id = str(id).split('?')[0].split('/')[3]
            link = 'https://www.ancestry.com/dna/' + id
            n.write(match_id+','+match_name+','+link+'\n')


def add_node_details():
    # if ids match, append to nodes.csv line in
    # Confidence,cMs,Segments,Notes\n order
    pass
