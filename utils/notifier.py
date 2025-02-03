# utils/notifier.py

from twilio.rest import Client
from google.cloud import storage

def download_file_from_gcs(bucket_name, blob_name, destination_file_name):
    """Descarga un archivo desde Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Archivo descargado a {destination_file_name}")
    


def send_whatsapp_message(account_sid, auth_token, from_whatsapp_number, to_whatsapp_number, media_url):
    """Envía un mensaje de WhatsApp con un archivo adjunto."""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="La búsqueda ha sido generada. El archivo se encuentra en el siguiente link: "+media_url,
        from_=f'whatsapp:{from_whatsapp_number}',
        to=f'whatsapp:{to_whatsapp_number}',
        #media_url=[media_url]
    )
    return f"Mensaje enviado con SID: {message.sid}"