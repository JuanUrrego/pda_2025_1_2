import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

URL = "https://es.wikipedia.org/wiki/Anexo:Ganadoras_del_Premio_Nobel"

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Buscar todas las tablas de ganadoras
tablas = soup.find_all('table', {'class': 'wikitable'})

datos = []
año_actual = None  # Lo usamos para conservar el año porque está fusionado por rowspan
fecha_scraping = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtener fecha y hora actual

for tabla in tablas:
    filas = tabla.find_all('tr')[1:]  # Saltar encabezado

    for fila in filas:
        columnas = fila.find_all('td')
        if len(columnas) < 5:
            continue  # Fila incompleta

        # Detectar si hay año en la primera columna
        if columnas[0].text.strip().isdigit():
            año_actual = columnas[0].text.strip()

        # Verificar si la segunda columna es una imagen
        contiene_imagen = columnas[1].find('img') is not None

        try:
            if contiene_imagen:
                premiada = columnas[2].get_text(strip=True)
                pais = columnas[3].get_text(strip=True)
                categoria = columnas[4].get_text(strip=True)
                motivacion = columnas[5].get_text(strip=True)
            else:
                premiada = columnas[1].get_text(strip=True)
                pais = columnas[2].get_text(strip=True)
                categoria = columnas[3].get_text(strip=True)
                motivacion = columnas[4].get_text(strip=True)
        except IndexError:
            continue  # Saltar fila malformada

        datos.append({
            'Año': año_actual,
            'Premiada': premiada,
            'País': pais,
            'Categoría': categoria,
            'Motivación': motivacion,
            'Fecha_Scraping': fecha_scraping  # Agregar fecha de scraping
        })

# Convertir a DataFrame
df = pd.DataFrame(datos)

# Guardar en archivo Excel
nombre_archivo = 'ganadoras_premio_nobel.xlsx'
df.to_excel(nombre_archivo, index=False, engine='openpyxl')

print(f"✅ Archivo guardado como '{nombre_archivo}' con {len(df)} registros.")
