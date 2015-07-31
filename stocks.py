import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def stocks():
	return 'Hello stocks!'
