import csv
import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup as bS
from flask import jsonify


class DiscoverFormat(object):
    def __init__(self, url):
        self.url = url

    def check_url(self):
        pass

    def check_format(self):
        pass


class Validation(DiscoverFormat):
    def is_valid(self):
        url_validate = re.search(r'^https*:\/\/.*\..*', self.url)
        return True if url_validate else False


class DiscoverFormatCSV(DiscoverFormat):

    def check_url(self):
        # Checking the end url
        return True if self.url and self.url.endswith('.csv') else False

    def discover_format(self):
        if self.url:
            sniffer = csv.Sniffer()
            file = requests.get(self.url)
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


class DiscoverFormatTSV(DiscoverFormat):

    def check_url(self):
        return True if self.url and self.url.endswith('.tsv') else False

    def discover_format(self):
        if self.url:
            sniffer = csv.Sniffer()
            file = requests.get(self.url)
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


class DiscoverFormatXML(DiscoverFormat):

    def check_url(self):
        return True if self.url and self.url.endswith('.xml') else False

    def discover_format(self):
        if self.url:
            response = urlopen(self.url)
            html_doc = response.read().decode('utf-8')
            str_html = str(html_doc)
            if "xml" in str_html[:40]:
                return True
            else:
                return False
        else:
            return False
