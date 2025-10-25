# Lista principal de cursos (cada curso será un diccionario con nombre y nota)
cursos = []

# Pila donde se guardan los cambios realizados (último en entrar, primero en salir)
historial = []

# Cola de solicitudes de revisión (primero en entrar, primero en salir)
cola = []


# ================== FUNCIÓN: REGISTRAR CURSO ==================
def registrar_curso():
    nombre = input("\nIngrese el nombre del curso: ").strip().lower()

    # Validación: el nombre no puede estar vacío
    if nombre == "":
        print("\n-El nombre no puede estar vacío, escribir de nuevo-\n")
        return


    for curso in cursos:
        if curso['nombre'].lower()==nombre.lower():
            print(f"\n--- El curso: {nombre} ya esta registrado, no se puede repetir---\n")

    try:
        nota = float(input("Ingrese la nota del curso (0-100): "))

        # Validación: nota fuera de rango
        if nota < 0 or nota > 100:
            print("\n-La nota debe estar entre 0 y 100-\n")
            return
    except:
        # Si el usuario escribe texto en vez de número
        print("\n-Nota incorrecta, ingresa un valor numérico-\n")
        return

    # Agregar curso a la lista
    cursos.append({'nombre': nombre, 'nota': nota})

    # Registrar acción en historial (PILA)
    historial.append(f"Curso agregado: {nombre} (nota {nota})")

    print(f"\n-Curso '{nombre}' (Nota: {nota}) registrado con éxito-\n")


# ================== FUNCIÓN: MOSTRAR CURSOS ==================
def mostrar_curso():
    if not cursos:
        print("\n---No hay cursos disponibles---\n")
        return

    print("\n---Lista de cursos---")
    # enumerate da el índice (i) y el curso a la vez
    for i, curso in enumerate(cursos, start=1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")


# ================== FUNCIÓN: PROMEDIO GENERAL ==================
# Formato numérico: f"{promedio:.2f}" imprime el promedio con 2 decimales.

def promedio_general():
    if not cursos:
        print("\n---No hay cursos registrados---\n")
        return
    else:
        promedio = sum(c["nota"] for c in cursos) / len(cursos)
        # .2f → muestra dos cifras decimales (formato flotante)
        print(f"\n-Tu promedio general es: {promedio:.2f}-")


# ================== FUNCIÓN: CONTAR APROBADOS Y REPROBADOS ==================
def cursos_aprobados_reprobados():
    if not cursos:
        print("\n---No hay cursos registrados---\n")
        return

    # Cuenta los cursos con nota >= 60
    aprobados = sum(1 for c in cursos if c["nota"] >= 60)
    reprobados = len(cursos) - aprobados

    print(f"\n---Aprobados: {aprobados}")
    print(f"---Reprobados: {reprobados}\n")

# ================== FUNCIÓN: BÚSQUEDA LINEAL ==================
def buscar_curso():
    if not cursos:
        print("\n---No hay cursos disponibles---\n")
        return

    nombre = input("\nIngrese el nombre del curso a buscar: ").strip().lower()
    encontrado = False

    # Busca uno por uno (búsqueda lineal)
    for curso in cursos:
        if curso["nombre"].lower() == nombre:
            print(f"\n---Curso encontrado: {curso['nombre']}--- Nota: {curso['nota']}---\n")
            encontrado = True
            break

    if not encontrado:
        print("\n---Curso no encontrado---\n")


# ================== FUNCIÓN: ACTUALIZAR NOTA ==================
def actualizar_nota():
    if not cursos:
        print("\n---No hay cursos disponibles---")
        return

    mostrar_curso()
    indice = int(input("\nIngrese el número del curso que quiere actualizar: ")) - 1

    if 0 <= indice < len(cursos):
        nueva_nota = float(input("\nIngrese la nueva nota (0-100): "))

        # Validación de rango de nota
        while nueva_nota < 0 or nueva_nota > 100:
            print("Nota incorrecta, debe estar entre 0 y 100.")
            nueva_nota = float(input("Ingrese nuevamente la nota: "))

        # Guarda el cambio en el historial
        historial.append(f"Nota actualizada: {cursos[indice]['nombre']} {cursos[indice]['nota']} -> {nueva_nota}")
        cursos[indice]["nota"] = nueva_nota

        print("\n---Nota actualizada correctamente---\n")
    else:
        print("---Número de curso inválido---\n")


# ================== FUNCIÓN: ELIMINAR CURSO ==================
def eliminar_curso():
    mostrar_curso()
    if not cursos:
        print("---No hay cursos para eliminar---\n")
        return

    try:
        eliminar = int(input("\nIngrese el número del curso a eliminar: ")) - 1

        if eliminar < 0 or eliminar >= len(cursos):
            print("---Opción inválida---")
            return

        eliminado = cursos.pop(eliminar)
        historial.append(f"Curso eliminado: {eliminado['nombre']}")
        print(f"---Curso '{eliminado['nombre']}' eliminado---\n")
    except:
        print("\n---Error: ingrese un número válido---\n")


# ================== ORDENAMIENTO BURBUJA (por nota) ==================
def ordenar_burbuja():
    if not cursos:
        print("\n---No hay cursos disponibles---")
        return

    n = len(cursos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cursos[j]["nota"] > cursos[j + 1]["nota"]:
                # Intercambio de posiciones
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]

    print("\n---Cursos ordenados por nota (menor a mayor):\n")
    mostrar_curso()


# ================== ORDENAMIENTO POR INSERCIÓN (por nombre) ==================
def ordenar_por_insercion():
    if not cursos:
        print("\n---No hay cursos disponibles---\n")
        return

    for i in range(1, len(cursos)):
        key = cursos[i]
        j = i - 1
        # Compara nombres en minúsculas
        while j >= 0 and cursos[j]["nombre"].lower() > key["nombre"].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key

    print("\n---Cursos ordenados por nombre (inserción)---\n")
    mostrar_curso()


# ================== BÚSQUEDA BINARIA ==================

# Búsqueda binaria
# Asume lista ordenada por nombre.

def busqueda_binaria(nombre):
    ordenar_por_insercion()  # Asegura que estén ordenados antes de buscar
    inicio, fin = 0, len(cursos) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if cursos[medio]["nombre"].lower() == nombre.lower():
            return cursos[medio]
        elif cursos[medio]["nombre"].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return None


def buscar_curso_binario():
    nombre = input("---Ingrese el nombre del curso a buscar: ")
    if not nombre:
        print("\n---Nombre vacío---")
        return

    resultado = busqueda_binaria(nombre)
    if resultado:
        print(f"\n---Encontrado: {resultado['nombre']} - Nota: {resultado['nota']}")
    else:
        print("\n---No se encontró el curso---\n")


# ================== SIMULACIÓN DE COLA DE SOLICITUDES ==================
def simular_cola_revision():
    print("Ingrese curso para revisión (escriba 'fin' para terminar):")



    while True:
        curso = input("> ").strip().lower()  # elimina espacios al inicio y final

        if curso.lower() == "fin":
            break

        if curso == "":
            print("El nombre del curso no puede estar vacío.")
            continue

        cola.append(curso)  # agrega al final de la lista (cola)

    print("\nProcesando solicitudes:")

    # Recorremos la cola en orden de ingreso
    while cola:
        curso_actual = cola.pop(0)  # extrae el primer elemento
        print(f"Revisando: {curso_actual}")


# ================== FUNCIÓN: MOSTRAR HISTORIAL (PILA) ==================
# Historial: 
# Usa append() para registrar acciones y mostrar_historial( ) las escribe en 
# orden inverso con reserved( )


def mostrar_historial():
    if not historial:
        print("\n---El historial está vacío---\n")
    else:
        print("\n---- HISTORIAL DE CAMBIOS ----\n")
        # reversed() → muestra del último al primero
        for h in reversed(historial):
            print(h)



# ================== MENÚ PRINCIPAL ==================
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Registrar curso")
    print("2. Ver cursos")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso (búsqueda lineal)")
    print("6. Actualizar nota")
    print("7. Eliminar curso")
    print("8. Ordenar por nota (burbuja)")
    print("9. Ordenar por nombre (inserción)")
    print("10. Buscar curso (búsqueda binaria)")
    print("11. Simular cola de solicitudes")
    print("12. Mostrar historial (pila)")
    print("13. Salir")

    opcion = input("\n---Ingrese el número de acción a realizar: ")

    # Cada número ejecuta una función diferente
    if opcion == "1":
        registrar_curso()
    elif opcion == "2":
        mostrar_curso()
    elif opcion == "3":
        promedio_general()
    elif opcion == "4":
        cursos_aprobados_reprobados()
    elif opcion == "5":
        buscar_curso()
    elif opcion == "6":
        actualizar_nota()
    elif opcion == "7":
        eliminar_curso()
    elif opcion == "8":
        ordenar_burbuja()
    elif opcion == "9":
        ordenar_por_insercion()
    elif opcion == "10":
        buscar_curso_binario()
    elif opcion == "11":
        simular_cola_revision()
    elif opcion == "12":
        mostrar_historial()
    elif opcion == "13":
        print("Saliendo del programa... ¡Gracias por usar mi proyecto!")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")
