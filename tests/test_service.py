# Import sys and append to sys.path the route to be able to import the service functions.
import sys
sys.path.append('../')
from service import *

# Testing CSV cases
def test_check_csv_positivcase():
    url = "hola.csv"
    assert check_url_csv(url) == True

def test_check_csv_negcase():
    url = "hola.com"
    assert check_url_csv(url) == False

def test_check_csv_nonecase():
    assert check_url_csv(None) == False

# Testing TSV cases

def test_check_tsv_positivcase():
    url = "hola.tsv"
    assert check_url_tsv(url) == True

def test_check_tsv_negcase():
    url = "hola.com"
    assert check_url_tsv(url) == False

def test_check_tsv_nonecase():
    assert check_url_tsv(None) == False

# Testing XML cases

def test_check_xml_positivcase():
    url = "hola.xml"
    assert check_url_xml(url) == True

def test_check_xml_negcase():
    url = "hola.com"
    assert check_url_xml(url) == False

def test_check_xml_nonecase():
    assert check_url_xml(None) == False

# Testing CSV content cases

def test_find_csv_positivecase():
    url = "https://cdn-106.anonfiles.com/xdX6N28fy3/51291ef0-1665659414/csv-prueba"
    assert find_csv(url) == True

def test_find_csv_falsecase():
    url = "https://cdn-117.anonfiles.com/xdX6N28fy3/a6514c43-16232457479/csv-prueba"
    assert find_csv(url) == False

def test_find_csv_nonecase():
    assert find_csv(None) == False

# Testing TSV content cases

def test_find_tsv_positivecase():
    url = "https://cdn-115.anonfiles.com/34M5Ze94y6/c34e29ef-1665659332/prueba-tsv.txt"
    assert find_tsv(url) == True

def test_find_tsv_falsecase():
    url = "https://cdn-103.anonfiles.com/34M5Ze94y6/bc29f570-1665653300/prueba-tsv.txt"
    assert find_tsv(url) == False

def test_find_tsv_nonecase():
    assert find_tsv(None) == False

# Testing XML content cases

def test_find_xml_positivecase():
    url = "https://factionskis.com/pages/photoslurp-product-feed"
    assert find_xml(url) == True

def test_find_xml_falsecase():
    url = "https://factionskis.com"
    assert find_xml(url) == False

def test_find_xml_nonecase():
    assert find_xml(None) == False


