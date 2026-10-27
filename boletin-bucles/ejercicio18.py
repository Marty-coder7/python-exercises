i = 0
intentos = 0
import random
numero = random.randint(1,10)
while i < 1:
    numero_puesto = int(input("Adivina el número (1-10): "))
    if numero_puesto != numero:
        if numero_puesto < numero:
            print("El numero es mayor")
            intentos += 1
        else:
            print("El número es menor")
            intentos += 1
    else:
        print("¡Correcto! Lo has adivinado en", intentos, "intentos")
        break

