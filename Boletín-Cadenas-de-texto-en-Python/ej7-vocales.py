vocales = "aeiouáéíóú"
cantidad = int(input("¿Cuantas palabras vas a introducir? "))
vocales_halladas = ""
for i in range(cantidad):
    palabra = input("Palabra {}: ".format(i+1)).strip().lower()
    for u in palabra:
        print()