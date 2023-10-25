# Lista de libs utilizadas no projeto do Pothole e versão do python

## Criando ambiente para execução local

Criado novo environment python 3.9 com conda para instalar as dependencias do tensorflow

`conda create -n tensor_fastai python=3.9`

Instalar pip no ambiente conda

`conda install pip`

Instalar dependencias do requirements.txt

`pip install -r requirements.txt`

Para executar o código localmente

`python src/app.py`

## Buildando imagem docker

Exemplo de Dockerfile

```
FROM registry.procempa.com.br/python:3.9

# Instala as dependências
WORKDIR /app
RUN apt-get update && \
	apt-get install -y libgirepository1.0-dev libjpeg-dev ffmpeg libsm6 libxext6 && \
	apt-get -y autoremove && \
	apt-get -y clean && \
	rm -rf /tmp/*

COPY /requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Cópia da aplicação
COPY /src /app
RUN chmod +x /app

CMD ["python", "/app/app.py"]
```

Buildar a imagem docker

`docker build -t smart_hub_pkl-docker:{version} .`

## Executar o container docker

Para executar a imagem é necessario que as pastas estejam na seguinte disposição:
 
```
.
..
workspace
├── images/
├── model/
├── output/
└── config.yaml
```

**images** - Local onde deve ser adicionado as imagens que será rodado a inferência.

**model** - Pasta onde deve ficar o modelo que sera usado para infêrencia.

**output** - Pasta onde será gerado o resultado das inferências após execução do container.

**config.yaml** - Arquivo que definira modelo a ser utilizado


Para executar o container deve ser executado o comando abaixo:

`docker run -v $PWD/workspace:/app/workspace --rm smart_hub_docker:{version}`

## Criando o arquivo config.yaml

Por padrão o docker utilizará o config.yaml na raiz do workspace
Exemplo de arquivo de configuração config.yaml para modelo em tensorflow

```
model:
  name: pothole_model/*
  img_size: 512 **
  img_mean: 0
  img_std: 255
```


Exemplo de arquivo de configuração config.yaml para modelo em tflite

*Modelo tflite são recomendados para uso mobile, ainda em fase de teste no container*

```
model:
  name: pothole_model.tflite
  img_size: 512 **
  img_mean: 0
  img_std: 255
```


**O img_size é obrigatório para modelos tensorflow ou keras, no pkl mesmo tendo uma prefêrencia de resolução de imagem para inferencia, a primeira camada sempre normaliza a imagem, ja no keras a transformação é feita anteriormente da inferência*

***Para modelos tensorflow é passado o diretório onde encontra-se os weights e arquivos pb para inferencia e podem estar na seguinte disposição:* 
```
.
..
pothole_model
├── assets
├── keras_metadata.pb
├── saved_model.pb
└── variables
    ├── variables.data-00000-of-00001
    └── variables.index

```

Exemplo de arquivo de configuração para modelos fastai

```
model:
  name: skin_cancer.pkl
```
