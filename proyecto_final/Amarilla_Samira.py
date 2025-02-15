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

class Pelicula:
    def __init__(self, nombre, anio, director, codigo):
        self.nombre = nombre
        self.anio = anio
        self.director = director
        self._codigo = codigo


class CatalogoPelicula(Pelicula):
    def __init__(self, nombre, anio, director, codigo, ruta_archivo):
        super().__init__(nombre, anio, director, codigo)
        self.ruta_archivo = ruta_archivo

    def agregar(self):
        with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{self.nombre},{self.anio},{self.director},{self._codigo}\n")
        print("Película agregada correctamente.")

    def listar(self):
        if not os.path.exists(self.ruta_archivo):
            print("No hay películas en el catálogo.")
            return
        
        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            peliculas = archivo.readlines()
        
        if not peliculas:
            print("El catálogo está vacío.")
        else:
            print("\n--- Lista de Películas ---")
            for pelicula in peliculas:
                print(pelicula.strip())

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print("Catálogo eliminado correctamente.")
        else:
            print("El catálogo no existe.")


def opciones():
    """Muestra el menú y gestiona las opciones del usuario."""
    ruta_archivo = "catalogo.txt"
    catalogo = CatalogoPelicula(ruta_archivo)

    while True:
        print("\n--- Catálogo de Películas ---")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo películas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la película: ")
            anio = input("Ingrese el año de estreno: ")
            director = input("Ingrese el director de la película: ")
            codigo = input("Ingrese el código de la película: ")
            pelicula = Pelicula(nombre, anio, director, codigo)
            catalogo.agregar(pelicula)
        elif opcion == "2":
            catalogo.listar()
        elif opcion == "3":
            catalogo.eliminar()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    opciones()