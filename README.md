Este proyecto es un programa interactivo en consola que permite registrar, gestionar y analizar cursos con sus notas.  
Incluye funcionalidades para registrar cursos, calcular promedios, realizar búsquedas, ordenar datos, y simular estructuras de datos como pilas (historial) y colas (solicitudes).

Características principales
Registro de cursos:
Guarda cursos con su nombre y nota (0–100).
Visualización de cursos: 
Muestra todos los cursos registrados con su respectiva nota.
Promedio general:
Calcula el promedio de todas las notas ingresadas.
Conteo de aprobados y reprobados:
Indica cuántos cursos tienen nota >= 60 y cuántos no.
Búsqueda de cursos:  
Búsqueda lineal*: Recorre toda la lista.  
Búsqueda binaria*: Más eficiente, requiere que la lista esté ordenada por nombre.
Ordenamientos implementados: 
Burbuja: Ordena los cursos por nota (menor a mayor).  
Inserción: Ordena los cursos alfabéticamente por nombre.
Actualización y eliminación:  
Permite modificar la nota o eliminar cursos registrados.
Historial (Pila):  
Registra todas las acciones realizadas (último en entrar, primero en salir).
Cola de solicitudes:  
Simula una cola FIFO (primero en entrar, primero en salir) para solicitudes de revisión.


Opción del menú: Descripción 
 1️ Registrar curso: Agrega un curso con su nota 
 2️ Ver cursos: Muestra todos los cursos 
 3️ Calcular promedio: Calcula el promedio general 
 4️ Contar aprobados/reprobados: Indica cuántos cursos pasaron o no 
 5️ Buscar curso (lineal): Busca un curso por nombre 
 6️ Actualizar nota: Modifica la nota de un curso 
 7️ Eliminar curso: Elimina un curso por índice 
 8️ Ordenar por nota (burbuja): Ordena ascendentemente por nota 
 9️ Ordenar por nombre (inserción): Ordena alfabéticamente 
 10 Buscar curso (binario): Busca por nombre usando búsqueda binaria 
 11 Simular cola de solicitudes: Maneja solicitudes tipo cola 
 12 Mostrar historial: Muestra las acciones registradas 
 13 Salir: Cierra el programa 
