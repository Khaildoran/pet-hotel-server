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
    # handle the GET request
    if request.method == 'GET':
        cursor.execute('SELECT * FROM "pets"')
        data = cursor.fetchall()
        print('data from pets GET:', data)
        return jsonify(data)

# Route for the Owners table
@app.route('/api/owners', methods=['POST'])
def owners_route():
    # handle the POST request
    if request.method == 'POST':
        try:
            req = request.get_json()
            SQL = 'INSERT INTO "owners" ("first_name", "last_name") VALUES (%s, %s);'
            data = [req['first_name'], req['last_name']]
            cursor.execute(SQL, data)
            conn.commit()
            print('in owners POST')
            return 'OK'
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)