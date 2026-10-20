
compra = float(input("Introduce el importe de la compra: "))
zona = input("Introduce la zona de envío (A/B/C): ").upper()
socio = input("¿Eres socio (S/N)? ").upper()

if compra <= 150:
    if socio == "S":
        envio = 19
    else:
        envio = 25
elif compra <= 750:
    if socio == "S":
        envio = 49
    else:
        envio = 60
elif compra <= 1500:
    if socio == "S":
        envio = 89
    else:
        envio = 120
else:
    if socio == "S":
        envio = compra * 0.06
    else:
        envio = compra * 0.08

if zona == "B":
    envio = envio + 30
elif zona == "C":
    envio = envio + 69

print(f"Gastos de envío: {envio:.2f} euros")
