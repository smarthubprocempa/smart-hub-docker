from minio import Minio

# le variaveis de ambiente
import os


def download_file():
    minio_client = Minio(
        os.environ['MINIO_URL'],
        access_key=os.environ['MINIO_ACCESS_KEY'],
        secret_key=os.environ['MINIO_SECRET_KEY'],
        secure=True
    )

# Baixa o arquivo que esta no path do bucket e salva no path local
    minio_client.fget_object(
        os.environ['MINIO_BUCKET'],
        file_path='xresnet50_export.pkl',
        object_name=os.environ['MINIO_MODEL_FILE'],
    )
