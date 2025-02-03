# main.py

from flask import Flask, render_template, jsonify
from flask import Flask
from utils.scraper import scrape_data
from utils.scraper2 import scrape_data2
from utils.cleaner import clean_data, save_to_csv
from utils.cleaner2 import clean_data2, save_to_csv2
from utils.notifier import download_file_from_gcs,  send_whatsapp_message
from twilio.rest import Client
from google.cloud import storage
from config.settings import URL, OUTPUT_FILE, PHONE_NUMBER
import os
import csv
import io
from google.cloud import storage

app = Flask(__name__)

@app.route('/')

def index():
    """Carga la página principal"""
    return render_template('index.html')


@app.route('/tarea', methods=['GET'])


def home():
    # 1. Extraer datos
    print("Extrayendo datos de la página web...")
    raw_data = scrape_data()

    
    # 2. Limpiar datos
    print("Limpiando datos...")
    clean_data_result = clean_data(raw_data)
    


    
    # 3. Guardar datos en un archivo
    print(f"Guardando datos en {OUTPUT_FILE}...")
    # Configuración: Detectar el entorno (local o nube)
    #cloud_mode = os.getenv("CLOUD_MODE", "false").lower() == "true"  # Detecta si está en modo nube
    #bucket_name = os.getenv("mi-bucket-motos")
    cloud_mode=True
    bucket_name="mi-bucket-motos"
    #print(f"CLOUD_MODE: {cloud_mode}")
    #print(f"BUCKET_NAME: {bucket_name}")
    if cloud_mode and bucket_name:
        save_file=save_to_csv(clean_data_result, filename="motos_data.csv", cloud_bucket_name=bucket_name)
        #return save_file
    else:
        save_file=save_to_csv(clean_data_result, filename="motos_data.csv")
        #return save_file
    


    # 4. Enviar archivo por WhatsApp
    # Configuración
    """
    bucket_name = 'mi-bucket-motos'
    blob_name = 'motos_data.csv'
    destination_file_name = 'output/out_motos_data.csv'
    download_file_from_gcs(bucket_name, blob_name, destination_file_name)
    """
    
    
    
    print("Enviando archivo por WhatsApp...")
    account_sid = 'ACCOUNT SID DE TWILIO'
    auth_token = 'AUTH TOKEN DE TWILIO'
    from_whatsapp_number = '+14155238886'
    to_whatsapp_number = '+57315XXXXXXX'
    media_url = 'https://storage.cloud.google.com/mi-bucket-motos/motos_data.csv'  # URL accesible públicamente del archivo
    send_wp=send_whatsapp_message(account_sid, auth_token, from_whatsapp_number, to_whatsapp_number, media_url)
    
    return jsonify({"message": send_wp})
    
   
    

if __name__ == "__main__":
    app.run(debug=True)