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
@app.route('/api/pets', methods=['GET', 'POST'])
def pets_route():
    # handle the GET request
    if request.method == 'GET':
        cursor.execute('SELECT * FROM "pets"')
        data = cursor.fetchall()
        print('data from pets GET:', data)
        return jsonify(data)
    elif request.method == 'POST':
        try:
            data = ['simon2', 'hooman', 'green', True, 2]
            cursor.execute('INSERT INTO "pets" ("name", "breed", "color", "is_checked_in", "owner_id") VALUES(%s, %s, %s, %s, %s)', data)
            conn.commit()
            return "OK"
        except (Exception, psycopg2.Error) as error:
            return 'ERROR!', 500, error