from utils import infere_images, model_loader
import sys
import os
# declare main function python
if __name__ == "__main__":
    print("Start application")
    print(sys.argv)
    config_file = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"
    if len(sys.argv) > 1:
        #Seta variavel de ambiente do config3.yaml
        print("chego aqui") 
        os.environ["CONFIG_NAME"] = config_file
    try:
        #learner = model_loader.load_model_keras()
        modelo, config = model_loader.load_model()
    except Exception as e:
        print("Ocorreu um erro ao carregar o modelo, o mesmo pode estar corrompido")
        print(e)
        exit(1)
    print("Modelo carregado corretamente")

    infere_images.infere_images(modelo, config)
