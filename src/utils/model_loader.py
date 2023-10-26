import os
import fastai
import fastai.vision.widgets
import fastai.vision.all
from utils import messages_exceptions
import tensorflow as tf
import keras
import yaml

caminho_atual = os.getcwd()
nome_variavel_ambiente = "MODEL_NAME"
version = "0.0.2"
print(caminho_atual)
PATH_MODEL = caminho_atual+"/workspace/model/"
PATH_CONFIG = caminho_atual+"/workspace/config.yaml"


def read_config():
    with open(PATH_CONFIG) as yaml_file:
        data = yaml.safe_load(yaml_file)
    print(data)
    return data

def get_model_type():
    if(os.path.isdir(PATH_MODEL+nome_modelo)):
        return "keras"
    elif(nome_modelo.endswith(".pkl")):
        return "fastai"
    elif(nome_modelo.endswith(".h5")):
        return "keras"
    else:
        raise Exception(messages_exceptions.invalid_model_type)


def check_if_more_than_one_model():
    arquivos_na_pasta = os.listdir(PATH_MODEL)
    total_de_arquivos = len(arquivos_na_pasta)
    print(arquivos_na_pasta)
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
        for arquivo in os.listdir(PATH_MODEL):
            if arquivo.endswith(".pkl"):
                return PATH_MODEL + arquivo
            else :
                raise Exception(messages_exceptions.no_model_in_folder)
    else:
        return PATH_MODEL + nome_modelo
    
def load_model():
    print("Carregando modelo")


def load_model_pkl():
    # path = return_model_path()
     print(f"Carregando modelo")
    # return fastai.vision.all.load_learner(path)  


def load_model_keras():
    return keras.models.load_model(PATH_MODEL+"")
    # TODO: load keras model


