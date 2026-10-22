# Listas globales en memoria RAM (Arreglos paralelos)
codigos = []
nombres = []
dnis = []
asuntos = []
fechas = []

def cargar_datos_desde_archivo():
    try:
        with open("expedientes.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 5:
                    codigos.append(datos[0])
                    nombres.append(datos[1])
                    dnis.append(datos[2])
                    asuntos.append(datos[3])
                    fechas.append(datos[4])
    except FileNotFoundError:
        pass

def guardar_datos_en_archivo():
    with open("expedientes.txt", "w") as archivo:
        for i in range(len(codigos)):
            archivo.write(f"{codigos[i]},{nombres[i]},{dnis[i]},{asuntos[i]},{fechas[i]}\n")

def validar_datos(codigo, dni):
    if len(dni) != 8 or not dni.isdigit():
        print("\n[ERROR] El DNI debe tener exactamente 8 números.")
        return False
    if codigo in codigos:
        print(f"\n[ERROR] El código de expediente '{codigo}' ya existe.")
        return False
    return True

def registrar_datos_expediente():
    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")
    codigo = input("Código de expediente: ").strip().upper()
    nombre = input("Nombre del ciudadano: ").strip()
    dni = input("Número de DNI: ").strip()
    asunto = input("Asunto del trámite: ").strip()
    fecha = input("Fecha de recepción (DD/MM/AAAA): ").strip()

    if codigo == "" or nombre == "" or dni == "" or asunto == "" or fecha == "":
        print("\n[ERROR] No se permiten campos vacíos.")
        return

    if validar_datos(codigo, dni):
        codigos.append(codigo)
        nombres.append(nombre)
        dnis.append(dni)
        asuntos.append(asunto)
        fechas.append(fecha)
        print("\n[ÉXITO] Expediente registrado de forma digital.")

def buscar_expediente(codigo_buscar):
    print("\n--- CONSULTA DE EXPEDIENTE ---")
    encontrado = False
    for i in range(len(codigos)):
        if codigos[i] == codigo_buscar.upper():
            print(f"\n[Localizado] Código: {codigos[i]} | Ciudadano: {nombres[i]} | DNI: {dnis[i]} | Asunto: {asuntos[i]} | Fecha: {fechas[i]}")
            encontrado = True
            break
    if not encontrado:
        print(f"\n[AVISO] El expediente con código '{codigo_buscar}' no existe.")

def ordenar_expedientes_por_codigo():
    n = len(codigos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if codigos[j] > codigos[j + 1]:
                codigos[j], codigos[j+1] = codigos[j+1], codigos[j]
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
                dnis[j], dnis[j+1] = dnis[j+1], dnis[j]
                asuntos[j], asuntos[j+1] = asuntos[j+1], asuntos[j]
                fechas[j], fechas[j+1] = fechas[j+1], fechas[j]

def mostrar_resultados_expedientes():
    print("\n--- LISTADO GENERAL DE EXPEDIENTES ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados en el sistema.")
        return
    for i in range(len(codigos)):
        print(f"{codigos[i]} | {dnis[i]} | {nombres[i]} | {fechas[i]} | {asuntos[i]}")

def menu_principal():
    cargar_datos_desde_archivo()
    while True:
        print("\n==================================================")
        print("     MUNICIPALIDAD DISTRITAL - MESA DE PARTES     ")
        print("==================================================")
        print("1. Registrar Expediente")
        print("2. Consultar Expediente por Código")
        print("3. Mostrar todos los Expedientes Ordenados")
        print("4. Guardar y Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            registrar_datos_expediente()
        elif opcion == "2":
            cod = input("\nIngrese el código del expediente a buscar: ").strip()
            buscar_expediente(cod)
        elif opcion == "3":
            ordenar_expedientes_por_codigo()
            mostrar_resultados_expedientes()
        elif opcion == "4":
            guardar_datos_en_archivo()
            print("\n[INFO] Datos guardados en 'expedientes.txt'. ¡Hasta luego!")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente del 1 al 4.")

if __name__ == "__main__":
    menu_principal()
