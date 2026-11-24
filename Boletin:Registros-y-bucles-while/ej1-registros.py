registros_leidos = 0
registros_validos = 0
registros_descartados = 0
inicio = True
while inicio == True:
    registro = input("Registro (o FIN para terminar) ")
    if registro == "FIN":
        print("Registros leidos: {0}".format(registros_leidos))
        print("Registros validos: {0}".format(registros_validos))
        print("Registros descartados: {0}".format(registros_descartados))
        inicio = False
    else:
        registros_leidos += 1
        registro = registro.split(";")
        campos = len(registro)
        for i in registro:
            if i == "":
                vacio = 1
                break
            else:
                vacio = 0
        if campos != 5:
            print("Registro descartado: tiene {0} campos y debe tener 5.".format(campos))
            registros_descartados += 1
        elif vacio == 1:
            print("Registro descartado: tiene algún campo vacio")
            registros_descartados += 1
        else:
            registros_validos += 1
            print("Nombre: {}".format(registro[0]))
            print("Primer apellido: {}".format(registro[1]))
            print("Segundo apellido: {}".format(registro[2]))
            print("Telefono: {}".format(registro[3]))
            print("Correo: {}".format(registro[4]))