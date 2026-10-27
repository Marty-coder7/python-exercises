suma = 0
contador = 0

numero = float(input("Introduce un número: "))

while numero >= 0:
    suma += numero
    contador += 1
    numero = float(input("Introduce otro número: "))

if contador == 0:
    print("No se han introducido datos")
else:
    media = suma / contador
    print("Media:", media)