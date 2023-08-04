from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def homepage(): #Function name and the url_for name should be same
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)