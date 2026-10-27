total_sin_iva = 0.0
total_iva = 0.0

while True:
  nombre = input("Producto: ")
  if nombre.lower() == "fin":
    break

  precio = float(input("Precio: "))

  while True:
    tipo = input("Tipo (a/o): ").lower()
    if tipo == "a":
      porcentaje = 4
      break
    elif tipo == "o":
      porcentaje = 21
      break
    else:
      print("Tipo no válido")


  iva_producto = precio * porcentaje / 100
  total_sin_iva += precio
  total_iva += iva_producto

total_a_pagar = total_sin_iva + total_iva

print(f"Total sin IVA: {total_sin_iva:.2f} €")
print(f"IVA: {total_iva:.2f} €")
print(f"Total a pagar: {total_a_pagar:.2f} €")
