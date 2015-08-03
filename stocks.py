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
		price = '{0:.2}'.format(data[1])
		change = '{0:.2}%'.format(float(data[2].strip().strip('\"%')))
		table = table + '<tr><td>' + symbol + '</td><td>' + price + '</td>'
		color = 'rgb(0,186,0)'
		if '-' in change:
			color = 'rgb(255,48,0)'
		table = table + '<td style=\"color:' + color + '\">' + change + '</td></tr>\n'
	return table + '</table>'
	
@app.route('/')
def root():
	return "Hello world!"

if __name__ == '__main__':
    app.run()