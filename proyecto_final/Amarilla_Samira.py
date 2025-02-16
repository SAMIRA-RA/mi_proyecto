import os # importa el modulo para el manejo de archivos
import re # importa para validaciones con expresiones regulares
from datetime import datetime # importa para validar el año

class ArchivoError(Exception): # clase para definir una excepcion personalizada en caso de errores con el archivo de catalogo
    def __init__(self, mensaje="Error con el archivo de catálogo."):
        super().__init__(mensaje)

class Pelicula:
    def __init__(self, nombre, anio, director, codigo):
        self.__codigo = codigo # atributo privado
        self.nombre = nombre
        self.anio = anio
        self.director = director

    def obtener_codigo(self): # getter para acceder al codigo
        return self.__codigo

class CatalogoPelicula: # genera la clase CatalogoPelicula con su atributo
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def agregar(self, pelicula): # metodo para agregar una pelicula
        try:
            with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
                archivo.write(f"{pelicula.nombre},{pelicula.anio},{pelicula.director},{pelicula.obtener_codigo()}\n")
            print("Película agregada correctamente.")
        except Exception as e:
            raise ArchivoError(f"Error al agregar la película: {e}")

    def listar(self): # metodo para listar las peliculas
        try:
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
        except Exception as e:
            raise ArchivoError(f"Error al listar las películas: {e}")

    def eliminar(self): # metodo para eliminar el archivo
        try:
            if os.path.exists(self.ruta_archivo):
                os.remove(self.ruta_archivo)
                print("Catálogo eliminado correctamente.")
            else:
                print("El catálogo no existe.")
        except Exception as e:
            raise ArchivoError(f"Error al eliminar el catálogo: {e}")

    def codigo_existe(self, codigo): # verifica si el codigo de la pelicula ya existe
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(',')
                    if len(datos) == 4 and datos[3] == str(codigo):
                        return True
        except FileNotFoundError:
            return False
        return False

def validar_texto(texto): # verifica que sea un valor valido
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ0-9'’\s]+$", texto))
