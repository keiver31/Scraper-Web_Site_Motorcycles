# utils/scraper.py

import requests
import json

def scrape_data():
    """Extrae información de una página web."""
    
    #Datos de la Peticion
    URL = "https://carroya-habilitadora-api.avaldigitallabs.com/find-filters"
    peticion = {"seoArray":[],"params":{"page":"2","category":"Motos","status":"usado","kilometers":"0-25000","location":"MEDELLIN","modelRange":"2019-2026","fuel":"Gasolina"},"isReqForRedirect":False}
    
    try:
        response = requests.post(URL, json=peticion)
        
        if response.status_code == 200:
            response_body = response.json()  # Convierte la respuesta a JSON
            return response_body
        
        else:
            print(f"Error: La solicitud falló con el código de estado {response.status_code}")
            return []
        
    except Exception as e:
        print(f"Error al extraer datos: {e}")
        return []