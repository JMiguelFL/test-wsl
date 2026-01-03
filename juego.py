import random

def adivina_numero():
    print("Bienvenido al juego de adivinar el número, estoy pensando en un número del 1 al 100")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    ganaste = False

    historial = []

    while not ganaste:
        try:
            entrada = input("Introduce un número: ")
            numero_usuario = int(entrada)

            historial.append(numero_usuario)

            intentos += 1

            if numero_usuario > numero_secreto:
                print("Más bajo")
            elif numero_usuario < numero_secreto:
                print("Más alto")
            else:
                print(f"Felicidades, has adivinado en {intentos} intentos.")
                ganaste = True
        except ValueError:
            print("Error: Por favor, escribe solo números.")
        
    print("\n--- Resumen de tu partida ---")
    print("Tus intentos fueron: ")

    for numero in historial:
        print(f"- {numero}")

if __name__ == "__main__":
    adivina_numero()