from flask import Flask, request
from markupsafe import escape
import json
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("dbname=pets_hotel user=")
cursor = conn.cursor()

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return 'CONNECTED TO SERVER'