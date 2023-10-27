from datetime import datetime
import fastai.vision.all
from fastai.vision.core import PILImage
import fastai.vision.widgets
import fastai
import os
import tensorflow as tf
from keras.preprocessing import image
import numpy as np

from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
caminho_atual = os.getcwd()
PATH_IMAGES = caminho_atual+"/workspace/images/"
PATH_OUTPUT = caminho_atual+"/workspace/output/"
 

def infere_images(model, config):
    # verificar se modelo é um Learner
    if isinstance(model, fastai.vision.all.Learner):
        return infere_images_fastai(model, config)
    if isinstance(model, Sequential):
        return infere_images_keras(model, config)

def save_csv(csv):
    print("Salvando csv")
    # get time as string and add to output.csv to save csv with timestamp
    file_name = "output.csv"+ str(datetime.now()) + ".csv"
    with open(PATH_OUTPUT + file_name, "w") as f: 
        f.writelines(csv)

def infere_images_fastai(model: fastai.vision.all.Learner, config):

    print("Inferindo imagens")
    headerCsv = "filename,prediction,class,probability\n"
    returnCsv = []
    returnCsv.append(headerCsv)

    for filename in os.listdir(PATH_IMAGES):
        if filename.endswith(".jpg"):
            print(f"Processando arquivo {filename}")
            img = PILImage.create(PATH_IMAGES + filename)
            pred, classe, prob = model.predict(img)
            returnCsv.append(f"{filename},{pred},{classe},{prob}\n")
        else:
            print(f"Arquivo {filename} não é um jpg, ignorando")
    save_csv(returnCsv)

def infere_images_keras(model, config):
    img_size = config["model"]["img_size"] if "img_size" in config["model"] else 224
    print("Inferindo imagens")
    headerCsv = "filename,prediction,class,probability\n"
    returnCsv = []
    returnCsv.append(headerCsv)

    for filename in os.listdir(PATH_IMAGES):
        if filename.endswith(".jpg"):
            print(f"Processando arquivo {filename}")
            img = image.load_img(PATH_IMAGES + filename, target_size=(img_size, img_size))
            img_array = image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)
            #normalize tensor to 0-1
            img_array = img_array/255.0
            predictions = model.predict(img_array)
            score = predictions[0] 
            class_names = config["model"]["classes"]
            returnCsv.append(f"{filename},{class_names[np.argmax(score)]},{np.argmax(score)},{100 * np.max(score)}\n")
        else:
            print(f"Arquivo {filename} não é um jpg, ignorando")
    save_csv(returnCsv)

    


   




    

