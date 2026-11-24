cad1 = input("Cadena: ").strip()
cad2 = input("Posible sufijo: ").strip()

if cad1 == "" or cad2 == "":
    print("No son válidas: las dos cadenas deben tener un carácter como mínimo.")
else:
    es_sufijo = True
    
    if len(cad2) > len(cad1):
        es_sufijo = False
    else:
        i = -1
        while i >= -len(cad2) and es_sufijo:
            if cad1[i] != cad2[i]:
                es_sufijo = False
            i = i - 1
            
    if es_sufijo:
        print("{} es sufijo de {}.".format(cad2, cad1))
    else:
        print("{} no es sufijo de {}.".format(cad2, cad1))
