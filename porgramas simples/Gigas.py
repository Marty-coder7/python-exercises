'''
Version 1.0

'''

gigas_usados = float(input("Cuantos gigas usaste:"))
precio_gigas = 3.0
calculo_final = precio_gigas

if gigas_usados <= 5:
    print("La factura asciede a:", precio_gigas)
elif gigas_usados <= 10:
    calculo_final += (gigas_usados-5)*1.5
    print("La factura asciende a:", calculo_final)
else:
    calculo_final += 5*1.5 + (gigas_usados-10)*1
    print("la factura asciede a:", calculo_final )

