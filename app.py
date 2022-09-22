from urllib import request
from flask import Flask,request
from service.urlReaderService import *
from module.file import File

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def UrlFormatReader():
    args = request.args
    url = args["url"]
    return UrlReader(url).to_json()