import os
import fastai
import fastai.vision.widgets
import fastai.vision.all
from utils import messages_exceptions
import tensorflow as tf
import keras
import yaml

caminho_atual = os.getcwd()
chave_config_NAME = "CONFIG_NAME"
version = "0.0.2"
print(caminho_atual)
PATH_MODEL = caminho_atual+"/workspace/model/"
PATH_WORKSPACE = caminho_atual+"/workspace/"




def load_config(name_config="config.yaml"):
    # se variavel de ambiente for passada, usar ela, se não usar config.yaml
    path_config = PATH_WORKSPACE + name_config
    with open(path_config) as yaml_file:
        data = yaml.safe_load(yaml_file)
    # validate data has the correct keys model and inside model name
    if "model" not in data:
        raise Exception(messages_exceptions.no_model_in_config)
    if "name" not in data["model"]:
        raise Exception(messages_exceptions.no_name_in_config)

    return data

def get_model_type(nome_modelo):
    if(os.path.isdir(PATH_MODEL+nome_modelo)):
        return "keras"
    if(nome_modelo.endswith(".pkl")):
        return "fastai"
    if(nome_modelo.endswith(".h5")):
        return "keras"
    
    raise Exception(messages_exceptions.invalid_model_type)


def get_model_path(config):
    nome_modelo = config["model"]["name"]
    if (nome_modelo is None):
        raise Exception(messages_exceptions.no_model_in_config)
    return PATH_MODEL + nome_modelo
    
def load_model():
    config_name = os.environ.get(chave_config_NAME,"config.yaml")
    config = load_config(config_name)
    model_type = get_model_type(config["model"]["name"])
    path = get_model_path(config)
    if(model_type == "fastai"):
        return load_model_pkl(path), config
    if(model_type == "keras"):
        return load_model_keras(path), config
    raise Exception(messages_exceptions.invalid_model_type)



def load_model_pkl(path) -> fastai.vision.all.Learner:
    # path = get_model_path()
    
    return fastai.vision.all.load_learner(path)  


def load_model_keras(path):
    return keras.models.load_model(path)
    # TODO: load keras model


