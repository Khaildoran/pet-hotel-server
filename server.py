from flask import Flask, request, jsonify
from markupsafe import escape
import json
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("dbname=pets_hotel user=")
cursor = conn.cursor()

@app.route('/api/test', methods=['GET'])
def index():
    if request.method == 'GET':
        print('/api/test GET route has been hit')
        return 'CONNECTED TO SERVER'

# Route for the Pets table
@app.route('/api/pets', methods=['GET'])
def pets_route():
    if request.method == 'GET':
        cursor.execute('SELECT * FROM "pets"')
        data = cursor.fetchall()
        print('data from pets GET:', data)
        return jsonify(data)