n = int(input("¿Cuántas notas? "))
i = 1
suma = 0

while i <= n:
    nota = int(input("Nota "+str(i)+": "))
    suma += nota
    i += 1
    

media = suma/n
print("Nota media:", media)