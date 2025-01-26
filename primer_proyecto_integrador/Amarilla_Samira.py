import random # uso este modulo para poder seleccionar una palabra aleatoriamente

def seleccionar_palabra(): # defino la funcion para selecciona la plabra
    palabras = ['cielo', 'avenida', 'juego', 'asteroide', 'planta'] # hago el listado de palabras
    return random.choice(palabras) # elijo la palabra aleatoriamente

def mostrar_palabra(palabra, letras_adivinadas): # defino la funcion que va a mostrar la palabra con guiones, en caso de ser adivinada coloca la letra
    return ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)

def juego(): # defino la funcion del juego
    palabra = seleccionar_palabra() # almaceno la palabra que se va a tener que adivinar
    letras_adivinadas = set() # almaceno las letras que ha acertado
    vidas = 7  # establezco la cantidad de vidas
    letras_incorrectas = [] # almaceno las letras incorrectas

    print("¡Bienvenido al juego de adivinar la palabra!") # mensaje inicial
    print("Tienes", vidas, "vidas.") # condiciones del juego
    
    while vidas > 0: # uso el while para que se siga ejecutando mientras se cumpla que le queden vidas
        print("\nPalabra a adivinar:", mostrar_palabra(palabra, letras_adivinadas)) # muestro la palabra a adivinar
        print("Letras incorrectas:", ' '.join(letras_incorrectas)) # muestro el listado de las palabras incorrectas
        letra = input("Ingresa una letra: ").lower() # le pido que ingrese la palabra

        if not letra.isalpha() or len(letra) != 1: # se verifica que ingreso una letra
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas: # se verifica que no es una letra ingresada previamente
            print("Ya has adivinado esa letra. Intenta otra.") 
            continue

        if letra in palabra: # se verifica que la letra conforme la palabra a adivinar
            letras_adivinadas.add(letra) # se añade al listado de letras acertadas
            print("¡Correcto!")
        else:
            vidas -= 1 # si es incorrecta se resta 1 vida
            letras_incorrectas.append(letra) # se añade al listado de letras incorrectas
            print("Incorrecto. Te quedan", vidas, "vidas.") # se muestra el estado en el juego

        if all(letra in letras_adivinadas for letra in palabra): # se verifica si acerto la palabra
            print("\n¡Felicidades! Has adivinado la palabra:", palabra) # mensaje cuando gana
            break
    else:
        print("\nPerdiste. La palabra era:", palabra) # mensaje cuando pierde

juego()