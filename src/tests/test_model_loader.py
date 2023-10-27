import unittest
import os

from fastai.vision.learner import Learner
from keras.models import Sequential

from src.utils import model_loader

class TestModelLoader(unittest.TestCase):
    
    # primeiro realizar o teste da leitura do config.yaml
    # primeiro testar se o arquivo existe e retorna data esperado
    def test_load_config_exists(self):
        #verificar se o data retorna um campo model e dentro desse campo nome
        assert model_loader.load_config()["model"]["name"] == "xresnet50_export.pkl"
        assert model_loader.load_config("config3.yaml")["model"]["name"] == "pothole_model/"

    def test_load_config_file_not_exists(self):
        self.assertRaises(FileNotFoundError, model_loader.load_config, "config2.yaml")

    def test_load_config_file_but_invalid_format(self):
        self.assertRaises(Exception, model_loader.load_config, "config4.yaml")
        self.assertRaises(Exception, model_loader.load_config, "config5.yaml")

    def test_get_model_type(self):
        config = model_loader.load_config()
        model_name = config["model"]["name"]
        model_type = model_loader.get_model_type(model_name)
        assert model_type == "fastai"
        model_name = model_loader.load_config("config3.yaml")["model"]["name"]
        model_type = model_loader.get_model_type(model_name)
        assert model_type == "keras"
        model_name = "errado.txt"
        self.assertRaises(Exception, model_loader.get_model_type, model_name)

    def test_load_model(self):
        # test without any env variable
        model = model_loader.load_model()
        # test if model is a fastai Learner
        assert isinstance(model, Learner)
        # set environment variable to test CONFIG_NAME
        os.environ["CONFIG_NAME"] = "config3.yaml"
        model = model_loader.load_model()
        #test if model is a keras model
        assert isinstance(model, Sequential)


 



