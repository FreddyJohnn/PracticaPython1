def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            calificaciones = input("Ingrese las calificaciones separadas por coma (ej. 90,85,78): ")
            calificaciones = [float(x) for x in calificaciones.split(",")]
            estudiantes[nombre] = calificaciones
        except ValueError:
            print("Error: Ingrese solo números separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, notas in estudiantes.items():
        if notas:
            promedio = sum(notas) / len(notas)
        else:
            promedio = 0
        promedios[nombre] = promedio
    return promedios

def encontrar_mejor_estudiante(promedios):
    if not promedios:
        return None, 0
    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]

def guardar_resultados(estudiantes, promedios, mejor_estudiante, promedio_maximo):
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados de los estudiantes:\n\n")
        for nombre in estudiantes:
            archivo.write(nombre + ": Calificaciones = " + str(estudiantes[nombre]) + ", Promedio = " + "{:.2f}".format(promedios[nombre]) + "\n")
        archivo.write("\n")
        archivo.write("Estudiante con el mejor promedio: " + str(mejor_estudiante) + " (" + "{:.2f}".format(promedio_maximo) + ")\n")

def menu():
    estudiantes = {}
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar datos de estudiantes")
        print("2. Calcular promedios")
        print("3. Determinar mejor promedio")
        print("4. Guardar resultados en archivo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiantes = ingresar_datos()
        elif opcion == "2":
            if not estudiantes:
                print("Primero debe ingresar datos.")
            else:
                promedios = calcular_promedios(estudiantes)
                for nombre, promedio in promedios.items():
                    print(nombre + ": " + "{:.2f}".format(promedio))
        elif opcion == "3":
            if not estudiantes:
                print("Primero debe ingresar datos.")
            else:
                promedios = calcular_promedios(estudiantes)
                mejor, promedio_max = encontrar_mejor_estudiante(promedios)
                print("El estudiante con el mejor promedio es " + str(mejor) + " con " + "{:.2f}".format(promedio_max))
        elif opcion == "4":
            if not estudiantes:
                print("Primero debe ingresar datos.")
            else:
                promedios = calcular_promedios(estudiantes)
                mejor, promedio_max = encontrar_mejor_estudiante(promedios)
                guardar_resultados(estudiantes, promedios, mejor, promedio_max)
                print("Resultados guardados en resultados.txt.")
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Abir menu
menu()
