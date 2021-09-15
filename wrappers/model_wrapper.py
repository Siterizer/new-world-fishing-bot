from os import environ
from numpy import expand_dims, exp, argmax
environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Disable tensorflow warnings
from tensorflow.keras.models import load_model
from utils.global_variables import MODEL_PATH

class_names = ['0', '1', '2', '3']
model = load_model(MODEL_PATH)

def get_model_result(screenshot):
    img_array = expand_dims(screenshot, 0)
    predictions = model.predict(img_array)
    score = exp(predictions[0])/sum(exp(predictions[0]))
    return str(class_names[argmax(score)])
