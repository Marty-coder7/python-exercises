'''
Ejericio 3 - Formar un triangulo
Autor: Mark Marty
Fecha: 6/10/2026
'''
tipo_triangulo = "nada"

a = float(input("Dame un lado: "))
b = float(input("Dame otro lado: "))
c = float(input("Dame el ultimo lado: "))


if a > 0 and b > 0 and c > 0:
    if a + b < c:
        print("No forman un triangulo")
        tipo_triangulo = "inexistente"
    elif a + b == c:
        print("No forman un triangulo, se queda plano")
        tipo_triangulo = "inexistente"
    else:
        if a == b == c:
            tipo_triangulo = "equilatero"
        elif a == b or b == c:
            tipo_triangulo = "isosceles"
        else:
            tipo_triangulo = "escaleno"
else:
    print("Todos los lados tiene que ser mayores que cero")
    tipo_triangulo = "inexistente"


print("Lado a: ", a)
print("Lado b: ", b)
print("Lado c: ", c)
print("Forman un triangulo", tipo_triangulo)




