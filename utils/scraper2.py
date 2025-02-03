import requests
import json

def scrape_data2():
    
    """Extrae información de múltiples páginas de un sitio web."""
    
    URL = "https://carroya-habilitadora-api.avaldigitallabs.com/find-filters"
    total_paginas = 11  # Número total de páginas a extraer
    resultados = []  # Lista para almacenar los datos extraídos
    
    for pagina in range(1, total_paginas + 1):
        peticion = {
            "seoArray": [],
            "params": {
                "page": str(pagina),
                "category": "Motos",
                "status": "usado",
                "kilometers": "0-25000",
                "location": "MEDELLIN",
                "modelRange": "2019-2026",
                "fuel": "Gasolina"
            },
            "isReqForRedirect": False
        }
        
        try:
            response = requests.post(URL, json=peticion)
            
            if response.status_code == 200:
                response_body = response.json()
                resultados.append(response_body)  # Almacena los datos de la página
                print(f"Página {pagina} extraída con éxito.")
            else:
                print(f"Error: La solicitud para la página {pagina} falló con el código {response.status_code}")
        
        except Exception as e:
            print(f"Error al extraer datos de la página {pagina}: {e}")
    
    return resultados

"""
# Ejecutar la función y almacenar los datos
datos_extraidos = scrape_data2()

# Guardar los datos en un archivo JSON
with open("datos_motos3.json", "w", encoding="utf-8") as f:
    json.dump(datos_extraidos, f, ensure_ascii=False, indent=4)

print("Extracción completada y datos guardados en 'datos_motos.json'.")
"""
