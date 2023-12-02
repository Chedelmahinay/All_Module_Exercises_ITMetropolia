from flask import Flask, Response
import mysql.connector
import json

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='airport',
    user='root',
    password='123',
    autocommit=True)

app = Flask(__name__)


@app.route('/<icao_code>')
def airport_name_town(icao):
    sql = 'SELECT name, municipality from airport where ident =' + f'"{icao}"' + ";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            response = {
                "icao": icao,
                "Name": result[0][0],
                "Location": result[0][1]
            }
            return response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint - Add '/icao_code' in URL to get info",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
