
import csv

def importar_csv(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = [fila for fila in lector]
        print(f"{len(datos)} registros cargados")
        return datos
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")

datos = importar_csv('/content/ANALISIS_DATOS_CLIMATICOS/datos/datos.csv')

meses         = []
temperatura   = []
precipitacion = []



for registro in datos:
    if registro["Variable"] == "Temperatura (°C)":
        meses.append(registro["Mes"])
        temperatura.append(float(registro["Valor"]))
    elif registro["Variable"] == "Precipitación (mm)":
        precipitacion.append(float(registro["Valor"]))

menu = ['1', '2', '3']

def validar_entrada_menu():
    while True:
        opcion = input("Seleccione una opción valida: ")
        if opcion in menu:
            return opcion
        else:
            print("Opción inválida.")

while menu:
    print('''\n ANALISIS DE DATOS CLIMATICOS
    1. ESTADISTICAS PROMEDIO
    2. MAXIMOS Y MINIMOS
    3. SALIR''')
    opcion = validar_entrada_menu()
    match opcion:
        case '1':
            print("Opción 1: ESTADÍSTICAS PROMEDIO")
        case '2':
            print("Opción 2: MAXIMOS Y MINIMOS")
        case '3':
            print("Saliendo del programa...")
            menu = False
