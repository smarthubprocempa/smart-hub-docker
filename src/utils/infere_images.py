from datetime import datetime
import fastai.vision.all
from fastai.vision.core import PILImage
import fastai.vision.widgets
import fastai
import os

caminho_atual = os.getcwd()
PATH_IMAGES = caminho_atual+"/workspace/images/"
PATH_OUTPUT = caminho_atual+"/workspace/output/"
 

def infere_images(learner: fastai.vision.all.Learner):
    print("Inferindo imagens")
    headerCsv = "filename,prediction,class,probability\n"
    returnCsv = []
    returnCsv.append(headerCsv)

    for filename in os.listdir(caminho_atual + PATH_IMAGES):
        if filename.endswith(".jpg"):
            print(f"Processando arquivo {filename}")
            img = PILImage.create(caminho_atual + PATH_IMAGES + filename)
            pred, classe, prob = learner.predict(img)
            returnCsv.append(f"{filename},{pred},{classe},{prob}\n")
        else:
            print(f"Arquivo {filename} não é um jpg, ignorando")
    save_csv(returnCsv)

def save_csv(csv):
    print("Salvando csv")
    # get time as string and add to output.csv to save csv with timestamp
    file_name = "output.csv"+ str(datetime.now()) + ".csv"
    with open(caminho_atual + PATH_OUTPUT + file_name, "w") as f: 
        f.writelines(csv)
