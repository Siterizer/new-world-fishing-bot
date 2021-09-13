import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Disable tensorflow warnings
from tensorflow import keras
from utils.global_variables import MODEL_PATH

class_names = ['0', '1', '2', '3']
model = keras.models.load_model(MODEL_PATH)

def get_model_result(screenshot):
    img_array = np.expand_dims(screenshot, 0)
    predictions = model.predict(img_array)
    score = np.exp(predictions[0])/sum(np.exp(predictions[0]))
    return str(class_names[np.argmax(score)])