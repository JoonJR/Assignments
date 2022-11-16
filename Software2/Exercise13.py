import json
from flask import Flask, Response
import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True
        )
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/prime_number/<number>')
def prime(number):
    global isprime
    try:
        number = int(number)
        if number > 1:
            for i in range(2, int(number/2) + 1):
                if (number % i) == 0:
                    isprime = False
                else:
                    isprime = True
        else:
            isprime = False

        response = {
            "Number": number,
            "isPrime": isprime
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.route('/airport/<icao>')
def get_airport(icao):
    try:
        sql = "SELECT ident, airport.name, municipality FROM airport"
        sql += " WHERE ident='" + icao + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in results:
                icao_code = row[0]
                name = row[1]
                location = row[2]

        response = {
            "ICAO": icao_code,
            "Name": name,
            "Location": location
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)