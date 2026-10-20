
usos = int(input("¿Cuántas veces prevés utilizar el gimnasio? "))

tarjeta = 50
num_bonos = usos // 10
precio_bonos = num_bonos * 20
entradas = usos % 10
precio_mixto = num_bonos * 20 + entradas * 3

print(f"Con tarjeta: {tarjeta} euros.")
print(f"Con bonos ({(usos + 9) // 10}): {((usos + 9) // 10) * 20} euros.")
print(f"Con bonos ({num_bonos}) y entradas ({entradas}): {precio_mixto} euros.")

if tarjeta <= precio_bonos and tarjeta <= precio_mixto:
    print("Recomendación: tarjeta.")
elif precio_bonos <= tarjeta and precio_bonos <= precio_mixto:
    print("Recomendación: bonos.")
else:
    print("Recomendación: bonos y entradas.")
