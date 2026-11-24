cadena = ""
campos = 0
registros = 0
inicio = True

while inicio ==True:
    nombre = input("Nombre: ")
    if nombre == "FIN":
        print("Registros constituidos: {}".format(registros))
        break
    else:
        campos +=1
    
    primero = input("Primer apellido: ")
    if primero == "FIN":
        print("Registro incompleto descartado: tenia {} campos de 5.".format(campos))
        print("Registros constituidos: {}".format(registros))
        break
    else:
        campos +=1

    segundo = input("Segundo apellido:")
    if segundo == "FIN":
        print("Registro incompleto descartado: tenia {} campos de 5.".format(campos))
        print("Registros constituidos: {}".format(registros))
        break
    else:
        campos +=1

    telefono = input("Telefono: ")
    if telefono == "FIN":
        print("Registro incompleto descartado: tenia {} campos de 5.".format(campos))
        print("Registros constituidos: {}".format(registros))
        break
    else:
        campos +=1
    
    correo = input("Correo:")
    if correo == "FIN":
        print("Registro incompleto descartado: tenia {} campos de 5.".format(campos))
        print("Registros constituidos: {}".format(registros))
        break
    else:
        campos +=1

    cadena = nombre+";"+primero+";"+segundo+";"+telefono+";"+correo
    print("Registro constituido: {}".format(cadena))
    registros += 1
    campos = 0            
