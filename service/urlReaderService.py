from module.file import *
import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

# Check the URL to find the file format, if not, call PruebaLocal function.
def ReadUrl(url):
    if url.endswith(".csv"):
        return File("csv", url)
    elif url.endswith(".tsv"):
        return File("tsv", url)
    elif url.endswith(".xml"):
        return File("xml", url)
    else:
        return FormatFinder(url)

    # Checking the content of the url to find the format
def FormatFinder(url):
    if (IsXml(url)):
        return File("xml", url)
    sniffer = csv.Sniffer()
    file = requests.get(url)
    with open('test2.txt', 'w', encoding='utf-8') as f:
        f.writelines(file.text)
    f.close()
    dialect = sniffer.sniff(file.text)
    if dialect.delimiter == "\t":
    #     # Send JSON object
        return File("tsv", url)
    elif dialect.delimiter == ",":
        return File("csv", url)
    return File("File format unknow or not recognizable.", url)

def IsXml(url):
    response = urlopen(url)
    html_doc = response.read()
        # print(html_doc)
        # Parsing data
    soup = BS(html_doc, features="xml")
        # We parse to str
    strhtm = soup.prettify()
        # printing lines of html
        # print(strhtm[:39])
        # Search a sub-string (xml) on the first 40 characters
    if "xml" in strhtm[:40]:
        return True
    else:
        return False