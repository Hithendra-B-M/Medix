from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io

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

@app.route("/save", methods=["POST"])
def save_image():
    if request.method == "POST":
        file = request.files["image"]

        if file:
            filename = file.filename
            # file.save(os.path.join("uploads", filename))

            return "1"  # Return 1 if the file was uploaded successfully
        else:
            return "0"  # Return 0 if no file was selected

if __name__ == '__main__':
    app.run(debug=True)