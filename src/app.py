from utils import model_loader

# declare main function python
if __name__ == "__main__":
    print("Start application")
    try:
        learner = model_loader.load_model()
    except Exception as e:
        print("Ocorreu um erro ao carregar o modelo, o mesmo pode estar corrompido")
        print(e)
        exit(1)
