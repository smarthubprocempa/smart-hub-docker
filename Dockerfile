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

EXPOSE 5000

CMD ["python", "/app/app.py"]

