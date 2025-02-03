# utils/cleaner.py

import csv
import json
import requests
import os
import io
from google.cloud import storage

def clean_data2(respuesta_json):
    
    if respuesta_json:
        respuesta_json=respuesta_json
        
        """
        Esta función recibe un JSON, extrae los campos especificados para cada moto
        y devuelve una lista de diccionarios con los campos seleccionados.

        :param data: JSON con la información de las motos.
        :return: Lista de diccionarios con los campos extraídos para cada moto.
         """

         # Los campos que quieres extraer (ajustar según la estructura real)
        fields = ["brand", "cciudadplaca", "ccombustible", "cmodeloint", "color", "ctipo", "ctipoaviso", "ctipocaja", "cylindrical", "kilometers", "price"]

        motos = []

        for entry in respuesta_json:
            super_highlights = entry.get("results", {}).get("superHighlights", [])
            for highlight in super_highlights:
                moto = {}
                for field in fields:
                    moto[field] = highlight.get(field, None)  # Usar None si el campo no existe
                motos.append(moto)
                #print(motos)

        return motos
    else:
        return "Error: La solicitud falló y el JSON no se pudo serializar"


def save_to_csv2(data, filename="motos_data2.csv"):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    Guarda el archivo en el sistema de archivos local.
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
        
        # Guardar localmente
        local_dir = "output"
        os.makedirs(local_dir, exist_ok=True)  # Crear el directorio si no existe
        local_path = os.path.join(local_dir, filename)
        
        with open(local_path, "w", newline="", encoding="utf-8") as file:
            file.write(csv_buffer.getvalue())
        
        print(f"Archivo CSV guardado exitosamente en {local_path}.")
        return local_path
    
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")
        return None
