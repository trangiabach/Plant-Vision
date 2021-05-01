import os
import tensorflow as tf
import numpy as np
from tensorflow import keras
from skimage import io
import pymysql
pymysql.install_as_MySQLdb()
from flask import jsonify
from tensorflow.keras.preprocessing import image
from flask_cors import CORS
from models import db
from models.Models import Disease

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

db_host = "mysql://sql6409422:YQYYXyF9sw@sql6.freemysqlhosting.net/sql6409422" #online hosting
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://bach:bach@localhost/plant_disease"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_PATH'] = 'D:/plant-disease-detector/templates'
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'uploads'

model =tf.keras.models.load_model('D:/plant-disease-detector/detection-model-plant-official-90.h5',compile=False)


def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    show_img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = np.array(x, 'float32')
    x /= 255
    preds = model.predict(x)
    return preds

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #get the file from post request
        f = request.files['file']

        #save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(app.config['UPLOAD_PATH'], secure_filename(f.filename))
        print(file_path)
        f.save(file_path)
        print(basepath)

        #make prediction
        preds = model_predict(file_path, model)
        print(preds[0])

        disease_class = ['Pepper__bell___Bacterial_spot', 'Potato___healthy',
                         'Tomato_Leaf_Mold', 'Tomato__Tomato_YellowLeaf__Curl_Virus',
                         'Tomato_Bacterial_spot', 'Tomato_Septoria_leaf_spot', 'Tomato_healthy',
                         'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato_Early_blight',
                         'Tomato__Target_Spot', 'Pepper__bell___healthy', 'Potato___Late_blight',
                         'Tomato_Late_blight', 'Potato___Early_blight', 'Tomato__Tomato_mosaic_virus']
        a = preds[0]
        ind=np.argmax(a)
        print(ind)
        print('Prediction:', disease_class[ind])
        result=disease_class[ind]
        query = Disease.query.filter_by(name=result).first()
        return jsonify({
            "result": result,
            "image": query.url,
            "symptoms": query.symptoms,
            "causes": query.causes,
            "solutions": query.solutions,
        })
    if request.method == "GET":
        disease_class = ['Pepper__bell___Bacterial_spot', 'Potato___healthy',
                         'Tomato_Leaf_Mold', 'Tomato__Tomato_YellowLeaf__Curl_Virus',
                         'Tomato_Bacterial_spot', 'Tomato_Septoria_leaf_spot', 'Tomato_healthy',
                         'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato_Early_blight',
                         'Tomato__Target_Spot', 'Pepper__bell___healthy', 'Potato___Late_blight',
                         'Tomato_Late_blight', 'Potato___Early_blight', 'Tomato__Tomato_mosaic_virus']
        return jsonify({
            "diseases": ['Pepper__bell___Bacterial_spot', 'Potato___healthy',
                         'Tomato_Leaf_Mold', 'Tomato__Tomato_YellowLeaf__Curl_Virus',
                         'Tomato_Bacterial_spot', 'Tomato_Septoria_leaf_spot', 'Tomato_healthy',
                         'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato_Early_blight',
                         'Tomato__Target_Spot', 'Pepper__bell___healthy', 'Potato___Late_blight',
                         'Tomato_Late_blight', 'Potato___Early_blight', 'Tomato__Tomato_mosaic_virus']
        })
    return None

@app.route('/disease', methods=['POST'])
def get_disease():
    req = request.get_json()
    result = req["name"]
    query = Disease.query.filter_by(name=result).first()
    return jsonify({
        "result": result,
        "image": query.url,
        "symptoms": query.symptoms,
        "causes": query.causes,
        "solutions": query.solutions
    })




if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    app.run()
