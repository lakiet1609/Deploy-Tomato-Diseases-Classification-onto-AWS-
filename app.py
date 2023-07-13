from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS
from TomatoDiseases.utils.common import decodeImage
from TomatoDiseases.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = 'inputimage.jpg'
        self.classifier = PredictionPipeline(self.filename)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/train', methods = ['GET', 'POST'])
def training_route():
    os.system('dvc repro')
    return 'Training done successfully'

@app.route('/predict', methods = ['POST'])
def predicting_route():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0',  port=8080)

