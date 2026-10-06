'''
Ejercicio 1 - Ecuacion de segundo grado
Autor: Mark Marty
Fecha: 6/10/2026
'''

import math

a = float(input("Dame el valor de a: "))
b = float(input("Ahora el de b: "))
c = float(input("Y el de c: "))

if a == 0:
    print("No es una ecuación de segundo grado.")
    
    if b != 0:
        x = -c / b
        print("Es una ecuación de primer grado.")
        print("Solución: x =", round(x, 2))
    else:
        print("No es una ecuación de primer grado.")

else:
    d = b ** 2 - 4 * a * c
    print("Discriminante =", d)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)

        print("Dos soluciones: x1 =", round(x1, 2), 
              ", x2 =", round(x2, 2))

    elif d == 0:
        x = -b / (2 * a)
        print("Una solución doble: x =", round(x, 2))

    else:
        print("No hay soluciones reales.")
