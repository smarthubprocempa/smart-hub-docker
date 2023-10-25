version = "0.0.1"

no_env_value = f"""Mais de um modelo encontrado na pasta de modelos, para identificar qual o modelo de uso, passe a variavel de ambiente MODEL_NAME substituindo model_exemplo pelo nome do modelo em extenso
docker run -v /path/to/models:/app/models -e MODEL_NAME=model_exemplo.pkl -p 5000:5000 -d smart_hub_pkl:{version}
"""

no_model_in_folder = f"""Nenhum modelo encontrado na pasta de modelos, lembre-se de adicionar o volume ao executar a imagem do docker
docker run -v /path/to/models:/app/models -p 5000:5000 -d smart_hub_pkl:{version}"""

invalid_model_type = "Tipo de modelo inválido, o modelo deve ser .pkl, h5, ou pasta com modelo keras e seus weights"
