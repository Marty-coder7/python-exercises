texto = input("Texto: ").strip()
buscada = input("Cadena buscada: ").strip()

if texto == "" or buscada == "":
  print("No son válidas: las dos cadenas deben tener un carácter como mínimo.")
else:
  encontrada = -1
  inicio = 0
  while inicio <= len(texto) - len(buscada) and encontrada == -1:
    ind_texto = inicio
    ind_buscada = 0
    coincide = True
    while ind_buscada < len(buscada):
      if texto[ind_texto] != buscada[ind_buscada]:
        coincide = False
      ind_texto += 1
      ind_buscada += 1
    if coincide:
      encontrada = inicio
    inicio += 1
  if encontrada == -1:
    print("{} no aparece en {}.".format(buscada,texto))
  else:
    print("{} empieza en la posición {} de {}.".format(buscada,encontrada,texto))