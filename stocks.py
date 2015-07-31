import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def stocks():
	tickers = ['AAPL','CRM']
	retVal = ''
	for ticker in tickers:
		csvData = requests.get('http://finance.yahoo.com/d/quotes.csv?s=' + ticker + '&f=sap2')
		retVal = retVal + csvData.text + '\n'
	return retVal
