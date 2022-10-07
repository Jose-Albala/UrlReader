from flask import Flask

# https://factionskis.com/pages/photoslurp-product-feed
# https://cdn-132.anonfiles.com/34M5Ze94y6/4aa72941-1664793644/prueba-tsv.txt TSV FILE
# https://cdn-128.anonfiles.com/xdX6N28fy3/6099c6c9-1664793677/csv-prueba CSV FILE

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'afa82e24412d6ffa8d2a8e05'

# Import routes
from controler import create, index
