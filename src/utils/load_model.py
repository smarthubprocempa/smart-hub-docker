import os

def check_if_model_in_folder() -> bool:
    if os.path.isfile('models/*.pkl'):
        print("Model found")
        return True
    return False


def load_model():
    if check_if_model_in_folder():
        print("Load model")
    else:
        print("Modelo não encontrado na pasta de modelos, lembre-se de adicionar o volume ao executar a imagem do docker")
        print("docker run -v /path/to/models:/app/models -p 5000:5000 -d smart_hub_pkl:latest")
        
    
