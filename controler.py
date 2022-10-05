from http.client import InvalidURL
from msilib import schema
from flask import render_template, request, jsonify, flash
from app import app
from service import * 

messages = [{}]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=['POST' , 'GET'])
def create():
    try:
        if request.method == 'POST':
            url = request.form['url']
            # Check URL as strings
            if CheckExtensionCSV(url) == True:
                data = {'url' : url, 'type' : 'csv'}
                return jsonify(data)
            elif CheckExtensionTSV(url) == True:
                data = {'url' : url, 'type' : 'tsv'}
                return jsonify(data)
            elif CheckExtensionXML(url) == True:
                data = {'url' : url, 'type' : 'xml'}
                return jsonify(data)

            # Checking URL Content
            elif Find_CSV(url) == True:
                data = {'url' : url, 'type' : 'csv'}
                return jsonify(data)
            elif Find_TSV(url) == True:
                data = {'url' : url, 'type' : 'tsv'}
                return jsonify(data)
            elif Find_XML(url) == True:
                data = {'url' : url, 'type' : 'xml'}
                return jsonify(data)
        
        else:
            return render_template('create.html')
    except:
            flash("Invalid URL,perhaps you meant http://...?")
            return render_template('create.html')
            


