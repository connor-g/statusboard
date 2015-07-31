import logging
import os
import requests
from flask import Flask

app = Flask(__name__)
app.debug = True

app.logger.setLevel(logging.DEBUG)
del app.logger.handlers[:]

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
handler.formatter = logging.Formatter(
    fmt=u"%(asctime)s level=%(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
app.logger.addHandler(handler)

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