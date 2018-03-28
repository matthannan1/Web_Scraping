# import time
# import getpass
# import os
import csv
import ancestryNodes as an
# from selenium import webdriver
from bs4 import BeautifulSoup as bs


# Going back in for match details
# get_details(browser)
soup = an.make_soup("details.txt")
flavored_soup = an.get_flavor(soup)
