"""
El objetivo consiste en desarrollar un programa quo permita llevar un registro
de películas aplicando conceptos de programación orientada a objetos.
El funcionamiento esperado es el siguiente:
• Al ejecutar el programa se solicita ingresar el nombre del catálogo de películas:
• Si el catálogo de películas no existe se creará uno nuevo. Este se va a
guardar en un archivo txt donde posteriormente se guardarán las peliculas. Si el
catálogo existe se podrá seguir modificando el archivo.
• Se debe mostrar un menú de opciones, que permita realizar las siguientes
operaciones:
l- Agregar Película
2- Listar Películas
3. Eliminar catálogo películas
4. Salir

Funcionamiento de las opciones:
• Agregar Película: se va a solicitar el nombre de la película y esta película se va a guardar en
el archivo txt.
• Listar Peliculas: va a mostrar todas las peliculas del catalogo y guardadas en el archivo txt.
• Eliminar catálogo: elimina el archivo txt que corresponde al catálogo de películas.
• Salir. debe finalizar el programa mostrando un mensaje al usuario.
Implementación POO:
El programa implementar programación orientada a objetos.
Se solicita:
• Clase Pelicula.
* uno de sus atributos debe ser privado.
• Clase CatalogoPelicula.
* atributo nombre
* atributo ruta_archivo
* métodos: agregar, listar, eliminar
"""
import os

ruta_archivo = r'C:\Users\Usuario\Desktop\1_proyecto\proyecto_final\catalogo.txt'

class Pelicula:
    def __init__(self, nombre, año, director, codigo):
        self.nombre = nombre
        self.año = año
        self.director = director
        self._codigo = codigo

class CatalogoPelicula (Pelicula):
    def __init__(self, nombre, ruta_archivo, codigo):
        super().__init__(nombre)
        super().__init__(codigo)
        self.ruta_archivo = ruta_archivo

    def agregar(self,codigo):



def opciones():
    """Muestra el menú y gestiona las opciones del usuario."""
    catalogo = "catalogo.csv"

    while True:
        print("\n--- Catálogo de Películas ---")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo películas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar(catalogo)
        elif opcion == "2":
            listar(catalogo)
        elif opcion == "3":
            eliminar(catalogo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
if __name__ == "__main__":
    opciones()