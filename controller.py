from flask import render_template, request, jsonify
import service
from app import app
from service import *

messages = [{}]


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/create/', methods=['GET'])
def create():
    try:
        form = request.args.get('url')
        print(form)
        if Validation(form).is_valid():
            if DiscoverFormatCSV(form).check_url() or DiscoverFormatCSV(form).discover_format():
                data = {'url': form, 'format': 'csv'}
                return jsonify(data)
            elif DiscoverFormatTSV(form).check_url() or DiscoverFormatTSV(form).discover_format():
                data = {'url': form, 'format': 'tsv'}
                return jsonify(data)
            elif DiscoverFormatXML(form).check_url() or DiscoverFormatXML(form).discover_format():
                data = {'url': form, 'format': 'xml'}
                return jsonify(data)
        else:
            data = {'url': form, 'error': 'File format unknow or not recognizable'}
            return jsonify(data, 400)
    except Exception as exc:
        data = {'url': form, 'error': 'File format unknow or not recognizable'}
        print(exc)
        return jsonify(data, 500)
