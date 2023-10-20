import fastai.vision.all
import fastai.vision.widgets
import fastai
import os

caminho_atual = os.getcwd()
PATH_FILES = "/workspace/files/"
 

def infer_images(learner: fastai.vision.all.Learner):
    print("Inferindo imagens")
    headerCsv = "filename,prediction,class,probability\n"
    returnCsv = []
    returnCsv.append(headerCsv)

    for filename in os.listdir(caminho_atual + PATH_FILES):
        if filename.endswith(".jpg"):
            print(f"Processando arquivo {filename}")
            img = fastai.vision.widgets.PILImage.create(os.path.join(caminho_atual + PATH_FILES, filename))
            pred, pred_idx, probs = learner.predict(img)
        else:
            print(f"Arquivo {filename} não é um jpg, ignorando")


    
