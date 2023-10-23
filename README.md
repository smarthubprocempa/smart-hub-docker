# Smart-hub-procempa Docker

## Projeto de criação da imagem docker para inferencias das IAS do Smart Hub Procempa

Para executar a imagem é necessario que as pastas estejam na seguinte disposição:
 
```
.
..
workspace
├── images
├── model
└── output
```

**images** - Local onde deve ser adicionado as imagens que será rodado a inferência.

**model** - Pasta onde deve ficar o modelo que sera usado para infêrencia.

**output** - Pasta onde será gerado o resultado das inferências após execução do container.


Para executar o container deve ser executado o comando abaixo:

`docker run -v $PWD/workspace:/app/workspace --rm smart_hub_pkl-docker:0.0.1`

Caso a pasta de modelo possua mais de um modelo, deve ser especificado atraves de variavel de ambiente MODEL_NAME qual modelo será utilizado.

`docker run -v $PWD/workspace:/app/workspace -e MODEL_NAME=model_exemplo.pkl --rm smart_hub_pkl-docker:0.0.1`

