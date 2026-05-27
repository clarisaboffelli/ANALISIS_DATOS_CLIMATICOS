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
def validar_entrada_menu(opciones_validas):
    while True:
        opcion = input("Seleccione una opción valida: ")
        if opcion in opciones_validas:
            return opcion
        else:
            print("Opción inválida.")

while menu:
    print('''\n ANALISIS DE DATOS CLIMATICOS - CATV
    1. ESTADISTICAS PROMEDIO
    2. MAXIMOS Y MINIMOS
    3. SALIR''')
    opcion = validar_entrada_menu(menu)
    match opcion:
      case '1':
            print("Opción 1: ESTADÍSTICAS PROMEDIO")
            # Aquí puedes agregar el código para calcular y mostrar las estadísticas promedio
            menu_estadisticas = True
            menu_estadisticas = ['1', '2', '3']
            while menu_estadisticas:
                print('''\n ESTADISTICAS PROMEDIO
                1. TEMPERATURA
                2. PRECIPITACIONES
                3. VOLVER AL MENU PRINCIPAL''')
                sub_opcion = validar_entrada_menu(menu_estadisticas)
                match sub_opcion:
                    case '1':
                        print(f"\nPromedio de temperatura anual: {sum(temperatura) / len(temperatura)} C")
                        mensual = input("¿Desea ver el promedio mensual? (s/n): ")
                        if mensual.lower() == 's':
                            print(f"\nPromedio de temperatura ENERO: {temperatura[0]} C")
                            print(f"Promedio de temperatura FEBRERO: {temperatura[1]} C")
                            print(f"Promedio de temperatura MARZO: {temperatura[2]} C")
                            print(f"Promedio de temperatura ABRIL: {temperatura[3]} C")
                            print(f"Promedio de temperatura MAYO: {temperatura[4]} C")
                            print(f"Promedio de temperatura JUNIO: {temperatura[5]} C")
                            print(f"Promedio de temperatura JULIO: {temperatura[6]} C")
                            print(f"Promedio de temperatura AGOSTO: {temperatura[7]} C")
                            print(f"Promedio de temperatura SEPTIEMBRE: {temperatura[8]} C")
                            print(f"Promedio de temperatura OCTUBRE: {temperatura[9]} C")
                            print(f"Promedio de temperatura NOVIEMBRE: {temperatura[10]} C")
                            print(f"Promedio de temperatura DICIEMBRE: {temperatura[11]} C")
                        else:
                            print("Volviendo al menú ESTADISTICAS PROMEDIO")
                    case '2':
                        print(f"\nPromedio de precipitación anual: {sum(precipitacion) / len(precipitacion)} mm")
                        mensual = input("¿Desea ver el promedio mensual? (s/n): ")
                        if mensual.lower() == 's':
                            print(f"\nPromedio de precipitación ENERO: {precipitacion[0]} mm")
                            print(f"Promedio de precipitación FEBRERO: {precipitacion[1]} mm")
                            print(f"Promedio de precipitación MARZO: {precipitacion[2]} mm")
                            print(f"Promedio de precipitación ABRIL: {precipitacion[3]} mm")
                            print(f"Promedio de precipitación MAYO: {precipitacion[4]} mm")
                            print(f"Promedio de precipitación JUNIO: {precipitacion[5]} mm")
                            print(f"Promedio de precipitación JULIO: {precipitacion[6]} mm")
                            print(f"Promedio de precipitación AGOSTO: {precipitacion[7]} mm")
                            print(f"Promedio de precipitación SEPTIEMBRE: {precipitacion[8]} mm")
                            print(f"Promedio de precipitación OCTUBRE: {precipitacion[9]} mm")
                            print(f"Promedio de precipitación NOVIEMBRE: {precipitacion[10]} mm")
                            print(f"Promedio de precipitación DICIEMBRE: {precipitacion[11]} mm")
                        else:
                            print("Volviendo al menú ESTADISTICAS PROMEDIO")

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
                        pass
                    case '2':
                        pass
                    case '3':
                        print("Volviendo al menú principal...")
                        menu_limites = False
      case '3':
            print("Saliendo del programa...")
            menu = False
