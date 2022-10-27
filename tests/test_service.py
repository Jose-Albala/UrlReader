# Import sys and append to sys.path the route to be able to import the service functions.
import sys
sys.path.append('../')
import unittest
from service import *


# Testing CSV cases
class CheckServiceTestCasesCSV(unittest.TestCase):
    def setUp(self):
        self.discover_format_csv = DiscoverFormatCSV

    def test_check_url_csv(self):
        url_sample = "https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv"
        assert self.discover_format_csv(url_sample).check_url() == True

        url = "hola.com"
        assert self.discover_format_csv(url).check_url() == False

    def test_discover_format_csv(self):
        url_sample = "https://cdn-127.anonfiles.com/xdX6N28fy3/9327e425-1666894655/csv-prueba"
        assert self.discover_format_csv(url_sample).discover_format() == True

        url = "https://factionskis.com/pages/photoslurp-product-feed"
        assert self.discover_format_csv(url).discover_format() == False


class CheckServiceTestCasesTSV(unittest.TestCase):
    def setUp(self):
        self.discover_format_tsv = DiscoverFormatTSV

    def test_check_url_tsv(self):
        url_sample = "https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.tsv"
        assert self.discover_format_tsv(url_sample).check_url() == True

        url = "hola.com"
        assert self.discover_format_tsv(url).check_url() == False

    def test_discover_format_tsv(self):
        url_sample = "https://cdn-107.anonfiles.com/34M5Ze94y6/706a5f83-1666895004/prueba-tsv.txt"
        assert self.discover_format_tsv(url_sample).discover_format() == True

        url = "https://factionskis.com/pages/photoslurp-product-feed"
        assert self.discover_format_tsv(url).discover_format() == False


class CheckServiceTestCasesXML(unittest.TestCase):
    def setUp(self):
        self.discover_format_xml = DiscoverFormatXML

    def test_check_url_xml(self):
        url_sample = "https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.xml"
        assert self.discover_format_xml(url_sample).check_url() == True

        url = "hola.com"
        assert self.discover_format_xml(url).check_url() == False

    def test_discover_format_xml(self):
        url_sample = "https://factionskis.com/pages/photoslurp-product-feed"
        assert self.discover_format_xml(url_sample).discover_format() == True

        url = "https://hola.com"
        assert self.discover_format_xml(url).discover_format() == False
