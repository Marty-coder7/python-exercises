'''
Autor: Mark Marty
Version: 1.0
'''
import random
#Da contexto al jugador
print("=== BIENVENIDO AL RETO DEL GUARDIAN ===")
print("Para cruzar el puente, debes adivinar un número del 1 al 10.")

#Da el resultado
x = random.randint(1,10)

#Se define el numero a adivinar y se define como un numero
y = int(input("Ingresa tu número: "))

#El primer if es para comprovar si es mayor que 10
if y <= 10:
    #El segundo if es para comprovar si es menor que 1
    if y >= 1:
        #Y el tercer y ultimo if es para comprovar si se ha adivinado el numero
        if x == y:
            print("¡Correcto! Has superado el reto y puedes cruzar el puente.")
        else:
            print("¡Incorrecto!", "Era", x)
    else:
        print("Recurda que es del 1 al 10, intentalo de nuevo.")
else:
    print("Recurda que es del 1 al 10, intentalo de nuevo.")
