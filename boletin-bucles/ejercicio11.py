n = int(input("¿Cuántos números? "))
i = 1
numero_a_guardar = 0

while i <= n:
    numero = int(input("Número "+str(i)+": "))
    if numero > numero_a_guardar:
        numero_a_guardar = numero
    else:
        numero_a_guardar = numero_a_guardar
    i += 1

print("El mayor es:", numero_a_guardar)

