from flask import render_template, request, jsonify
import service
from app import app
from service import *

messages = [{}]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=['POST', 'GET'])
def create():
    try:
        if request.method == 'POST':
            url = request.form['url']
            # Check URL as strings
            # Want to clean this controler, just let the function calls and the jsonify(data)
            if check_url_csv(url):
                data = {'url': url, 'format': 'csv'}
                return jsonify(data)
            elif check_url_tsv(url):
                data = {'url': url, 'format': 'tsv'}
                return jsonify(data)
            elif check_url_xml(url):
                data = {'url': url, 'format': 'xml'}
                return jsonify(data)

            # Checking URL Content
            elif find_csv(url) is True:
                data = {'url': url, 'format': 'csv'}
                return jsonify(data)
            elif find_tsv(url):
                data = {'url': url, 'format': 'tsv'}
                return jsonify(data)
            elif find_xml(url):
                data = {'url': url, 'format': 'xml'}
                return jsonify(data)

            else:
                return {'url':url, 'error': 'File format unknown or not recognizable'}
        else:
            return render_template('create.html')
    except:
            data = {'url':url, 'error' : 'File format unknow or not recognizable'}
            return jsonify(data)  