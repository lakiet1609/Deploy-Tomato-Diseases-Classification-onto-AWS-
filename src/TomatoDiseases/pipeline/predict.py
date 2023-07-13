import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.utils import img_to_array, load_img
import os
from TomatoDiseases import logger

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        model = load_model(r'artifacts\training\model.h5')
        image = img_to_array(load_img(self.filename, target_size=(224,224)))
        image = np.expand_dims(image, axis=0)
        class_names = os.listdir(r'artifacts\data_ingestion\tomato')
        result = np.argmax(model.predict(image), axis=1)
        prediction = class_names[result[0]]
        return [{'image': prediction}]
        
        
        
if __name__ == '__main__':
    try:
        obj = PredictionPipeline(r'artifacts\data_ingestion\tomato\Tomato___Bacterial_spot\00a7c269-3476-4d25-b744-44d6353cd921___GCREC_Bact.Sp 5807.JPG')
        print(obj.predict())
    except Exception as e:
        raise