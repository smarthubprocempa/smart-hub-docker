FROM registry.procempa.com.br/python:3.9

# Instala as dependências
COPY /requirements.txt /tmp/
WORKDIR /app
RUN apt-get update && \
apt-get install -y libgirepository1.0-dev libjpeg-dev ffmpeg libsm6 libxext6 && \
pip install --no-cache-dir -r /tmp/requirements.txt && \
apt-get -y autoremove && \
apt-get -y clean && \
rm -rf /tmp/*

# Cópia da aplicação
COPY /src /app
RUN chmod +x /app

EXPOSE 5000

CMD ["python", "/app/app.py"]

