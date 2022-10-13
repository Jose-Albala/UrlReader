import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bS
from flask import jsonify


def check_url_csv(url):
    # Checking the url as a string to find the format file, we control if url is a NONE object and if it returns False.
    if url is not None and url.endswith('.csv'):
        return True
    return False


def check_url_tsv(url):
    if url is not None and url.endswith('.tsv'):
        return True
    return False


def check_url_xml(url):
    if url is not None and url.endswith('.xml'):
        return True
    return False


def find_csv(url):
    # Checking url content, using Sniffer to check if the delimiter of the CSV is the requested.
    if url is not None:
        sniffer = csv.Sniffer()
        file = requests.get(url)
        try:
            dialect = sniffer.sniff(file.text)
            if dialect.delimiter == ',' and dialect.doublequote == False:
                return True
            else:
                return False
        except csv.Error:
            return False
    else:
        return False


def find_tsv(url):
    # Checking url content, using Sniffer to check if the delimiter of the TSV is the requested.
    if url is not None:
        sniffer = csv.Sniffer()
        file = requests.get(url)
        try:
            dialect = sniffer.sniff(file.text)
            if dialect.delimiter == '\t':
                return True
            else:
                return False
        except csv.Error:
            return False
    else:
        return False


def find_xml(url):
    # Checking XML content, trying to find the header of a xml file. <?xml version="1.0" encoding="UTF-8"?>
    if url is not None:
        response = urlopen(url)
        html_doc = response.read().decode('utf-8')
        str_html = str(html_doc)
        if "xml" in str_html[:40]:
            return True
        else:
            return False
    else:
        return False

