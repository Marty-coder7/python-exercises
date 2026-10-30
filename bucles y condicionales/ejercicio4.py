articulo = "Zapatillas"
precio = 35
billetes_validos = [5, 10, 20, 50]
print(f"Artículo: {articulo}")
print(f"Precio: {precio} €")
falta_por_pagar = precio
while falta_por_pagar > 0:
    billete = int(input("Introduce un billete: "))  
    if billete in billetes_validos:
        falta_por_pagar -= billete        
        if falta_por_pagar > 0:
            print(f"Faltan {falta_por_pagar} €")
    else:
        print("Billete no válido")


cambio = abs(falta_por_pagar)
print(f"Cambio: {cambio} €")
