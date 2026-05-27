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

def validar_entrada_menu(opciones_validas):
    while True:
        opcion = input("Seleccione una opción valida: ")
        if opcion in opciones_validas:
            return opcion
        else:
            print("Opción inválida.")

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
while menu:
    print('''\n ANALISIS DE DATOS CLIMATICOS - CATV
    1. ESTADISTICAS PROMEDIO
    2. MAXIMOS Y MINIMOS
    3. SALIR''')
    opcion = validar_entrada_menu(menu)
    match opcion:
        case '1':
            menu_estadisticas = ['1', '2', '3']
            while menu_estadisticas:
                print('''\n ESTADISTICAS PROMEDIO
                1. TEMPERATURA
                2. PRECIPITACIONES
                3. VOLVER AL MENU PRINCIPAL''')
                sub_opcion = validar_entrada_menu(menu_estadisticas)
                match sub_opcion:
                    case '1':
                        print(f"\nPromedio de temperatura anual: {sum(temperatura) / len(temperatura):.2f} C")
                    case '2':
                        print(f"\nPromedio de precipitación anual: {sum(precipitacion) / len(precipitacion):.2f} mm")
                    case '3':
                        print("Volviendo al menú principal...")
                        menu_estadisticas = False
        case '2':
            menu_limites = ['1', '2', '3']
            while menu_limites:
                print('''\n MAXIMOS Y MINIMOS
                1. TEMPERATURA
                2. PRECIPITACIONES
                3. VOLVER AL MENU PRINCIPAL''')
                sub_opcion = validar_entrada_menu(menu_limites)
                match sub_opcion:
                    case '1':
                        print(f"\nTemp. máxima: {max(temperatura):.2f} C — Mes: {meses[temperatura.index(max(temperatura))]}")
                        print(f"Temp. mínima: {min(temperatura):.2f} C — Mes: {meses[temperatura.index(min(temperatura))]}")
                    case '2':
                        print(f"\nPrecip. máxima: {max(precipitacion):.2f} mm — Mes: {meses[precipitacion.index(max(precipitacion))]}")
                        print(f"Precip. mínima: {min(precipitacion):.2f} mm — Mes: {meses[precipitacion.index(min(precipitacion))]}")
                    case '3':
                        print("Volviendo al menú principal...")
                        menu_limites = False
        case '3':
            print("Saliendo del programa...")
            menu = False
