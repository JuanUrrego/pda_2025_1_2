import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


class DataWebWikipedia:
    def __init__(self):
        self.url = "https://es.wikipedia.org/wiki/Anexo:Ganadoras_del_Premio_Nobel"

    def obtener_datos(self):
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, 'html.parser')

            tablas = soup.find_all('table', {'class': 'wikitable'})

            datos = []
            año_actual = None
            fecha_scraping = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for tabla in tablas:
                filas = tabla.find_all('tr')[1:]  # Omitir encabezado
                for fila in filas:
                    columnas = fila.find_all('td')
                    if len(columnas) < 5:
                        continue

                    if columnas[0].text.strip().isdigit():
                        año_actual = columnas[0].text.strip()

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
                        continue

                    datos.append({
                        'Año': año_actual,
                        'Premiada': premiada,
                        'País': pais,
                        'Categoría': categoria,
                        'Motivación': motivacion,
                        'Fecha_Scraping': fecha_scraping
                    })

            df = pd.DataFrame(datos)
            print("✅ Datos extraídos con éxito.")
            print(df.head())
            return df

        except Exception as e:
            print("❌ Error al obtener los datos:", e)
            return pd.DataFrame()