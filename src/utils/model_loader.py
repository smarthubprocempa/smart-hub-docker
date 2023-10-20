import os
import fastai
import fastai.vision.widgets
import fastai.vision.all
from utils import messages_exceptions

caminho_atual = os.getcwd()
nome_variavel_ambiente = "MODEL_NAME"
version = "0.0.1"
PATH_MODEL = "/workspace/model/"



def check_if_more_than_one_model():
    arquivos_na_pasta = os.listdir(caminho_atual + PATH_MODEL)
    total_de_arquivos = len(arquivos_na_pasta)
    if total_de_arquivos > 1:
        if nome_variavel_ambiente in os.environ:
            valor_variavel_ambiente = os.environ[nome_variavel_ambiente]
            return valor_variavel_ambiente
        raise Exception(messages_exceptions.no_env_value)
    if total_de_arquivos == 0: 
        raise Exception(messages_exceptions.no_model_in_folder)
    print("Apenas um modelo na pasta, tudo certo!")
    return None

def return_model_path():
    nome_modelo = check_if_more_than_one_model()
    if (nome_modelo is None):
        for arquivo in os.listdir(caminho_atual + PATH_MODEL):
            if arquivo.endswith(".pkl"):
                return caminho_atual + PATH_MODEL + arquivo
            else :
                raise Exception(messages_exceptions.no_model_in_folder)
    else:
        return caminho_atual + PATH_MODEL + nome_modelo
    

def load_model() -> fastai.vision.all.Learner:
    path = return_model_path()
    print(f"Carregando modelo {path}")
    return fastai.vision.all.load_learner(path)



