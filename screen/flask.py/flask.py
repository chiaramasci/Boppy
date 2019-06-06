import os
import webbrowser
from flask import Flask
app = Flask(__name__)

FILE_YELLOW = "/home/pi/Desktop/flask/flask.py/templates/yellow.html"
FILE_BLUE = "/home/pi/Desktop/flask/flask.py/templates/blue.html"
FILE_RED = "/home/pi/Desktop/flask/flask.py/templates/red.html"
FILE_ORANGE= "/home/pi/Desktop/flask/flask.py/templates/orange.html"
FILE_PINK ="/home/pi/Desktop/flask/flask.py/templates/pink.html"
FILE_GREEN = "/home/pi/Desktop/flask/flask.py/templates/green.html"

@app.route('/yellow')
def yellow():
    webbrowser.open(FILE_YELLOW)
    return "yellow"

@app.route('/blue')
def blue():
    webbrowser.open(FILE_BLUE)
    return "blue"

@app.route('/pink')
def pink():
    webbrowser.open(FILE_PINK)
    return "pink"

@app.route('/green')
def green():
    webbrowser.open(FILE_GREEN)
    return "green"

@app.route('/red')
def red():
    webbrowser.open(FILE_RED)
    return "red"

@app.route('/orange')
def orange():
    webbrowser.open(FILE_ORANGE)
    return "orange"


if __name__ == '__main__':
    app.run(host ="0.0.0.0" , port = 5000)
