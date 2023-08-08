from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io

app = Flask(__name__)

model = load_model("Voidex.h5")

class_labels = [
    "Atelectasis", "Brain_Tumor", "Cardiomegaly", "Consolidation", "Edema", "Effusion",
    "Emphysema", "Fibrosis", "Hernia", "Infiltration", "Mass", "No_Brain_Finding",
    "No_Lung_Finding", "Nodule", "Pleural", "Pneumonia", "Pneumothorax", "Tuberculosis"
]

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
        image_file = request.files["image"]
        img = image.load_img(io.BytesIO(image_file.read()), target_size=(150, 150))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0

        predictions = model.predict(img)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = class_labels[predicted_class_index]
        
        print(img)

        return predicted_class


@app.route("/classify", methods=["POST"])
def classify():
    image_file = request.files["image"]
    img = image.load_img(io.BytesIO(image_file.read()), target_size=(150, 150))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    predictions = model.predict(img)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_labels[predicted_class_index]
    print(img)

    return predicted_class

if __name__ == '__main__':
    app.run(debug=True)