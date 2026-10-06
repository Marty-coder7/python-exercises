'''
Ejercicio 2 - Cuanto cuesta la luz
Autor: Mark Marty
Fecha: 6/10/2026
'''

precio_base = float(5.00)
precio_barata = float(0.10)
precio_caro = float(0.20)
franja_a_usar = 0
precio_a_usar = 0
importe = 0
kwh_gastado = float(input("Cuantos kWh gastaste? "))
hora = int(input("A que hora? "))



if hora >= 0 and hora <= 23 and kwh_gastado > 0:
    if hora < 7:
        precio_a_usar = float(precio_barata)
        franja_a_usar = "Franja barata"
        importe = precio_base +(kwh_gastado*precio_a_usar)
    else:
        Precio_a_usar = float(precio_caro)  
        franja_a_usar = "Franja Cara"
        importe = precio_base +(kwh_gastado*Precio_a_usar)
else:
    print("Error estas fuera de horas o los kWh no pueden ser negativo")

print("kWh consumidos", kwh_gastado)
print("Hora del consumo-(0-23)", hora)
print(franja_a_usar)
print("Importe:", round(importe*1.21, 2),"€ IVA incluido")
