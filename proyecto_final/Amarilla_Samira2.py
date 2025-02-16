from Amarilla_Samira import Pelicula, CatalogoPelicula, validar_texto, ArchivoError
from datetime import datetime

def opciones(): # establece las opciones del menu
    ruta_archivo = "catalogo.txt"
    catalogo = CatalogoPelicula(ruta_archivo)

    while True:
        print("\n--- Catálogo de Películas ---")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo de películas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":  # opcion para agregar una pelicula
                while True:
                    try:
                        codigo = int(input("Ingrese el código de la película: "))
                        if catalogo.codigo_existe(codigo):
                            print("El código ya está registrado. Ingrese otro.")
                        else:
                            break
                    except ValueError:
                        print("El código debe ser un número entero válido.")

                while True:
                    nombre = input("Ingrese el nombre de la película: ").strip()
                    if not validar_texto(nombre):
                        print("El nombre contiene caracteres no permitidos.")
                    else:
                        break

                while True:
                    try:
                        anio = int(input("Ingrese el año de estreno: "))
                        anio_actual = datetime.now().year
                        if anio <= 0 or anio > anio_actual: # revisa que sea menor al año actual
                            print(f"Por favor, ingrese un año válido (entre 1 y {anio_actual}).")
                        else:
                            break
                    except ValueError:
                        print("El año debe ser un número entero válido.")

                while True:
                    director = input("Ingrese el director de la película: ").strip()
                    if not validar_texto(director): # revisa el formato de lo ingresado
                        print("El director contiene caracteres no permitidos.")
                    else:
                        break

                pelicula = Pelicula(nombre, anio, director, codigo)
                catalogo.agregar(pelicula) # agrega la nueva pelicula 


            elif opcion == "2": # ejecuta el metodo que lista
                catalogo.listar()

            elif opcion == "3": # ejecuta el metodo que elimina
                catalogo.eliminar()

            elif opcion == "4":
                print("Saliendo del programa...")
                break # sale del programa


            else:
                print("Opción no válida. Intente de nuevo.") # en caso de que ingrese un valor invalido


        except ArchivoError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    opciones()
