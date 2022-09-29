from flask import Flask, request
from service.urlReaderService import *
from module.file import File

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def UrlToJson():
    args = request.args
    return ReadUrl(args["url"]).to_json()