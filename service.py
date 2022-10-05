import csv
import requests
from os import remove
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS


def CheckExtensionCSV(url):
# Checking the url as string, trying to find file format.
    if url.endswith('.csv'):
        return True

def CheckExtensionTSV(url):

    if url.endswith('.tsv'):
        return True

def CheckExtensionXML(url):
    if url.endswith('.xml'):
        return True


def Find_CSV(url):
# Checking url content, using Sniffer to check if the delimiter of the CSV is the requested.
    sniffer = csv.Sniffer()
    file = requests.get(url)
    try:
        dialect = sniffer.sniff(file.text)
        if dialect.delimiter == ',':
            return True
    except csv.Error:
            return False

def Find_TSV(url):
# Checking url content, using Sniffer to check if the delimiter of the CSV is the requested.
    sniffer = csv.Sniffer()
    file = requests.get(url)
    try:
        dialect = sniffer.sniff(file.text)
        if dialect.delimiter == '\t':
            return True
    except csv.Error:
            return False

def Find_XML(url):
# Checking XML content, trying to find the header of a xml file. <?xml version="1.0" encoding="UTF-8"?>
    response = urlopen(url)
    html_doc = response.read()
    soup = BS(html_doc, features="xml")
    strhtm = soup.prettify()
    if "xml" in strhtm[:40]:
        return True
    else:
        return False
    





