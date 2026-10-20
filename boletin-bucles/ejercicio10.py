n = int(input("¿Cuántas notas? "))
i = 1
suma = 0
aprobados = 0
suspensos = 0
while i <= n:
    nota = int(input("Nota "+str(i)+": "))
    suma += nota
    if nota < 5:
        suspensos += 1
    else:
        aprobados += 1
    i += 1
    

media = suma/n
print("Nota media:",round(media, 2))
print("Aprobados:",aprobados)
print("Suspensos:",suspensos)