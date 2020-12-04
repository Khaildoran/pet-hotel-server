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

# Route for the Pets table with paramater for pet id
@app.route('/api/pets/<int:pet_id>', methods=['PUT'])
def pet_byId_route(pet_id):
    try:
        if request.method == 'PUT':
            req = request.get_json()
            if req['checkDirection'] == 'OUT':
                sql = 'UPDATE "pets" SET "is_checked_in" = false WHERE "id" = %s'
            elif req['checkDirection'] == 'IN':
                sql = 'UPDATE "pets" SET "is_checked_in" = true WHERE "id" = %s'
            else:
                return 'Something has gone wrong', 501
            
            cursor.execute(sql, (pet_id,))
            conn.commit()
            return 'Request OK', 200

    except(Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database", error)
        return 'Bad Request %s' % error, 500