# utils/cleaner.py

import csv
import json
import requests
import os
import io
from google.cloud import storage

def clean_data(respuesta_json):
    
    if respuesta_json:
        respuesta_json=respuesta_json
        
        """
        Esta función recibe un JSON, extrae los campos especificados para cada moto
        y devuelve una lista de diccionarios con los campos seleccionados.

        :param data: JSON con la información de las motos.
        :return: Lista de diccionarios con los campos extraídos para cada moto.
         """

        super_highlights = respuesta_json.get("results", {}).get("superHighlights", [])
        
        motos = []
        # Procesar y mostrar los datos relevantes
        for item in super_highlights:
            moto_data = {
                "brand": item.get("brand"),
                "city": item.get("cciudadplaca"),
                "fuel": item.get("ccombustible"),
                "year": item.get("cmodeloint"),
                "color": item.get("color"),
                "type": item.get("ctipo"),
                "status": item.get("ctipoaviso"),
                "transmission": item.get("ctipocaja"),
                "cylinder": item.get("cylindrical"),
                "kilometers": item.get("kilometers"),
                "price": item.get("price"),
            }
            motos.append(moto_data)
        #return motos 
        return "Proceso Ok en Cleaner"
    else:
        return "Error: La solicitud falló y el JSON no se pudo serializar"

    
def save_to_csv(data, filename="motos_data.csv", cloud_bucket_name=None):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    - En local: Guarda el archivo en el sistema de archivos local.
    - En la nube: Guarda el archivo en Google Cloud Storage si `cloud_bucket_name` está definido.
    """
    
    if not data or not isinstance(data, list):
        print("Error: Los datos proporcionados no son válidos.")
        return 
    
    # Crear un archivo CSV en memoria
    headers = data[0].keys()
    csv_buffer = io.StringIO()
    
    try:
        writer = csv.DictWriter(csv_buffer, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        csv_buffer.seek(0)  # Volver al inicio del archivo
        
        # Determinar si guardar en la nube o en local
        if cloud_bucket_name:
            # Guardar en Google Cloud Storage
            client = storage.Client()
            bucket = client.bucket(cloud_bucket_name)
            blob = bucket.blob(filename)
            blob.upload_from_string(csv_buffer.getvalue(), content_type="text/csv")
            return(f"Archivo CSV guardado exitosamente en el bucket '{cloud_bucket_name}' como '{filename}'.")
        else:
            # Guardar localmente
            local_dir = "output"
            os.makedirs(local_dir, exist_ok=True)  # Crear el directorio si no existe
            local_path = os.path.join(local_dir, filename)
            
            with open(local_path, "w", newline="", encoding="utf-8") as file:
                file.write(csv_buffer.getvalue())
            
            return(f"Archivo CSV guardado exitosamente en {local_path}.")
    
    except Exception as e:
        return(f"Error al guardar el archivo CSV: {e}")

    
    
