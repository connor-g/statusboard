import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def stocks():
	tickers = ['AAPL','CRM']
	csvData = requests.get('http://finance.yahoo.com/d/quotes.csv?s=' + '+'.join(tickers) + '&f=nap2')
	return '50%,25%,25%,\n'+csvData.text
