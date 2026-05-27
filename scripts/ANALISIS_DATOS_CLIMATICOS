
import csv

def importar_csv(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)   # usa la primera fila como claves
            datos = [fila for fila in lector]
        print(f" {len(datos)} registros cargados")
        return datos
    except FileNotFoundError:
        print(f" Archivo no encontrado: {nombre_archivo}")

datos = importar_csv('/content/ANALISIS_DATOS_CLIMATICOS/datos/datos.csv')
