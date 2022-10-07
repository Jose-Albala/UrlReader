import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bS


def check_url_csv(url):
    # Checking the url as string, trying to find file format.
    if url.endswith('.csv'):
        return True


def check_url_tsv(url):
    if url.endswith('.tsv'):
        return True


def check_url_xml(url):
    if url.endswith('.xml'):
        return True


def find_csv(url):
    # Checking url content, using Sniffer to check if the delimiter of the CSV is the requested.
    sniffer = csv.Sniffer()
    file = requests.get(url)
    try:
        dialect = sniffer.sniff(file.text)
        if dialect.delimiter == ',' and dialect.doublequote == 'False':
            return True
    except csv.Error:
        return False


def find_tsv(url):
    # Checking url content, using Sniffer to check if the delimiter of the CSV is the requested.
    sniffer = csv.Sniffer()
    file = requests.get(url)
    try:
        dialect = sniffer.sniff(file.text)
        if dialect.delimiter == '\t' and dialect.doublequote == 'False':
            return True
    except csv.Error:
        return False


def find_xml(url):
    # Checking XML content, trying to find the header of a xml file. <?xml version="1.0" encoding="UTF-8"?>
    response = urlopen(url)
<<<<<<< HEAD
    html_doc = response.read().decode('utf-8')
    str_html = str(html_doc)
=======
    html_doc = response.read()
    soup = bS(html_doc, features="xml")
    str_html = soup.prettify()
>>>>>>> 661c106b3bbaaede476901afc84e524ecf50479a
    if "xml" in str_html[:40]:
        return True
    else:
        return False
