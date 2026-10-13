a = float(input("Introduce el número a: "))
b = float(input("Introduce el número b: "))
c = float(input("Introduce el número c: "))


if a > 0 and b > 0 and c > 0:
    if a + b < c:
        print("No es un triangulo")
    elif a + b == c:
        print("No es un triangulo")
    else:
        print("Es un triangulo")
else:
    print("No es un triangulo")
    