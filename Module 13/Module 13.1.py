from flask import Flask

app = Flask(__name__)


@app.route('/check/<number>')
def prime_num(number):
    number = int(number)
    for x in range(2, number):
        if number % x == 0:
            response = {"Number": number, "Prime": "No"}

            return response

    else:
        response = {"Number": number, "Prime": "Yes"}

        return response


if __name__ == '__main__':
    app.run()
