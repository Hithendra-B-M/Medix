from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p>Helloworld!</p>'

if __name__ == '__main__':
    app.run(debug=True)