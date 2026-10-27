suma = 0
contador = 0
min = 1
max = 1


numero = float(input("Introduce un número: "))
if numero >= max:
    max == numero
else:
    min == numero

while numero >= 0:
    if numero >= max:
        max = numero
    else:
        min = numero
    
    suma += numero
    contador += 1
    numero = float(input("Introduce otro número: "))
   

if contador == 0:
    print("No se han introducido datos")
else:
    media = suma / contador
    print("Media:", media)
    print("Mínimo:", min)
    print("Máximo:", max)