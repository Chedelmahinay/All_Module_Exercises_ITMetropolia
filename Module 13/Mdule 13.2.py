from flask import Flask, Response
import mysql.connector
import json
2
# Connection to Database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='root',
    password='yoyo@123',
    autocommit=True)

# Endpoint route
app = Flask(__name__)


@app.route('/<icao_code>')
def airport_name_town(icao_code):
    sql = 'SELECT name, municipality from airport where ident =' + f'"{icao_code}"' + ";"  # Extracting ICAO info
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            # response = json.dumps(row)
            # print(f" Airport name: {result[0][0]}, Town: {result[0][1]}")
            response = {
                "ICAO": icao_code,
                "Name": result[0][0],
                "Location": result[0][1]
            }
            return response


@app.errorhandler(404)  # Error manager
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint - Add '/ICAO-CODE' in URL to get info",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


# Launching Backend to Browser
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
