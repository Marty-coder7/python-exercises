
kwh = float(input("Introduce la cantidad de kWh: "))

if kwh <= 100:
    importe = kwh * 0.05
elif kwh <= 250:
    importe = 100 * 0.05 + (kwh - 100) * 0.07
else:
    importe = 100 * 0.05 + 150 * 0.07 + (kwh - 250) * 0.10

print(f"Importe: {importe:.2f} euros")
