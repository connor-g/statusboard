import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def stocks():
	tickers = ['AAPL','CRM']
	for ticker in tickers
	csvData = requests.get('http://finance.yahoo.com/d/quotes.csv?s=' + '+'.join(tickers) + '&f=sap2')
	return '40%,30%,30%,\n'+csvData.text
