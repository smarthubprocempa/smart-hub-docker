# Smart-hub-procempa Docker

## Projeto de criação da imagem docker para inferencias das IAS do Smart Hub Procempa
 
 Para executar o container deve ser executado o comando abaixo:

`docker run -v $PWD/model:/app/model --rm smart_hub_pkl-docker:0.0.1`

Caso a pasta de modelo possua mais de um modelo, deve ser especificado atraves de variavel de ambiente MODEL_NAME qual modelo será utilizado.

`docker run -v $PWD/model:/app/model -e MODEL_NAME=model_exemplo.pkl --rm smart_hub_pkl-docker:0.0.1`
