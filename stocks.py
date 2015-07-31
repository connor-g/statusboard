import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/stocks/<ticker>')
def stocks():
	#tickers = tickerlist.split('+')
	#retVal = ''
	#for ticker in tickers:
	csvData = requests.get('http://finance.yahoo.com/d/quotes.csv?s=' + ticker + '&f=sap2')
	#retVal = retVal + csvData.text + '\n'
	#return retVal
	return csvData.text
	
@app.route('/')
def root():
	return "Hello world!"

if __name__ == '__main__':
    app.run()