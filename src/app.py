from flask import Flask, request, Response, jsonify
from fastai.vision.widgets import *
from fastai.vision.all import *
import pandas as pd
import fastai
from PIL import Image
import cv2
import numpy as np
import os
from utils import minio_conector

# Initialize the Flask application

app = Flask(__name__)
print("[INFO] Initializing API ...")
print("[INFO] loading skin cancer detection model...")

diretorio_atual = os.getcwd()

# check if caminho_arquivo exists
if not os.path.exists(os.path.join(diretorio_atual, 'xresnet50_export.pkl')):
    print("[INFO] Downloading model from Minio...")
    minio_conector.download_file()
    print("[INFO] Done...")
caminho_arquivo = os.path.join(diretorio_atual, 'xresnet50_export.pkl')
learn_inf = load_learner(caminho_arquivo)
caminho_images = os.path.join(diretorio_atual, 'test_data')
print("[INFO] Done...")
print("[INFO] API ready to receive requests!")

# route http get to this method


@app.route('/skincancer/api/alive', methods=['GET'])
def alive():
    return Response(response="Ok", status=200, mimetype="application/text")
# route http to test prediction


@app.route('/skincancer/api/test', methods=['GET'])
def test():
    # read every image in caminho_images
    returnJson = []

    for filename in os.listdir(caminho_images):

        # img = cv2.imread(os.path.join(caminho_images, filename))
        img = PILImage.create(os.path.join(caminho_images, filename))
        # prediction
        pred, classe, prob = infere_imagem(img)
        print(type(pred))
        print(type(classe))
        print(type(prob))

        returnJson.append({"filename": filename, "prediction": pred, "class": np.array(
            classe).tolist(), "probability": np.array(prob).tolist()})

    returnJson = jsonify(returnJson)
    return returnJson
# route http posts to this method


@app.route('/skincancer/api/check', methods=['POST'])
def check():
    # request data
    r = request
    
    print("[INFO] Request received...")
    returnJson = []

    file = r.files['file']
    # check if file is a image
    if not file.content_type.startswith('image/'):
        return Response(response="File is not a image", status=400, mimetype="application/text")
    # read file with PILLOw
    img = PILImage.create(file)

    # prediction
    pred, classe, prob = infere_imagem(img)

    returnJson.append({"prediction": pred, "class": np.array(
        classe).tolist(), "probability": np.array(prob).tolist()})

    returnJson = jsonify(returnJson)
    return returnJson


def infere_imagem(imagem):
    predicao, classe, prob = learn_inf.predict(imagem)
    print(predicao)
    return predicao, classe, prob


# start flask app
app.run(host="0.0.0.0", port=5000)
