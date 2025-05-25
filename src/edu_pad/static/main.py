from dataweb import DataWebWikipedia
import pandas as pd


def main():
    dataweb = DataWebWikipedia()
    df = dataweb.obtener_datos()

    if not df.empty:
        ruta_archivo = "src/edu_pad/static/csv/ganadoras_premio_nobel.csv"
        df.to_csv(ruta_archivo, index=False, encoding='utf-8')
        print(f"Archivo guardado como '{ruta_archivo}' con {len(df)} registros.")
    else:
        print("No se guardó ningún archivo porque no se obtuvieron datos.")


if __name__ == "__main__":
    main()