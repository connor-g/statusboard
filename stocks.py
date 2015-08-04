import logging
import os
import requests
import sys
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

@app.route('/stocks/<tickerList>')
def stocks(tickerList):
	tickers = tickerList.split('+')
	table = '<table>\n'
	for ticker in tickers:
		csvData = requests.get('http://finance.yahoo.com/d/quotes.csv?s=' + ticker + '&f=sap2')
		data = csvData.text.split(',')
		symbol = data[0].strip().strip('\"')
		price = float(data[1])
		change = float(data[2].strip().strip('\"%'))
		table = table + '<tr><td>' + symbol + '</td><td>' + '{0:.2f}'.format(price) + '</td>'
		color = 'rgb(0,186,0)'
		if change < 0:
			color = 'rgb(255,48,0)'
		table = table + '<td style=\"color:' + color + '\">' + '{0:.2f}'.format(change) + '%</td></tr>\n'
	return table + '<meta data-refresh-every-n-seconds="60"></table>'
	
@app.route('/')
def root():
	return "Hello world!"

if __name__ == '__main__':
    app.run()