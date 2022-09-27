from module.file import File
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import csv
import requests
import os

def UrlReader(url):
    if url.endswith(".csv"):
        return File("csv", url)
    elif url.endswith(".xml"):
        return File("xml", url)
    elif url.endswith(".tsv"):
        return File("tsv", url)
    else:
        if CheckForXML(url):
            return File("xml", url)
        elif CheckForCSV(url):
            return File("csv", url)
        elif CheckForTSV(url):
            return File("tsv", url)
        else:
            return File("Format File Error", url)

    

def CheckForXML(url):
    # Saving http request in response
    response = urlopen(url)
    # Reading http request
    html_doc = response.read()
    # Parsing data with html.parser
    soup = BS(html_doc,"html.parser")
    # Converting to string
    strhtm = soup.prettify()
    # Search a sub-string (xml) on the first 40 characters 
    if "xml" in strhtm[:40]:
        return True
    else:
        return False

def CheckForCSV(url):
    sniffer = csv.Sniffer()
    file = requests.get(url)
    with open("test2.txt", 'w', encoding="utf-8") as f:
        f.writelines(file.text)
    f.close()
    dialect = sniffer.sniff(file.text)
    if dialect.delimiter == ",":
        mypath= os.getcwd() + "\\test2.txt"
        if os.path.isfile(mypath):
            os.remove(mypath)
            return True
    else:
        return False
    
def CheckForTSV(url):
    sniffer = csv.Sniffer()
    file = requests.get(url)
    with open("test2.txt", 'w', encoding="utf-8") as f:
        f.writelines(file.text)
    f.close()
    dialect = sniffer.sniff(file.text)
    if dialect.delimiter == "\t":
        mypath= os.getcwd() + "\\test2.txt"
        if os.path.isfile(mypath):
            os.remove(mypath)
            return True
    else:
        return False