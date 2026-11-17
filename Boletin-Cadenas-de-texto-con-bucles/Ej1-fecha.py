fecha = input("Fecha (dd/mm/aaaa): ")
partes = fecha.split("/")
nombre_mes = "ninguno"
dia = int(partes[0])
mes = int(partes[1])
año = int(partes[2])
match mes:
    case 1:
        nombre_mes = "enero"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 2:
        nombre_mes = "febrero"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 3:
        nombre_mes = "marzo"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 4:
        nombre_mes = "abril"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 5:
        nombre_mes = "mayo"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 6:
        nombre_mes = "junio"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 7:
        nombre_mes = "julio"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 8:
        nombre_mes = "agosto"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 9:
        nombre_mes = "septiembre"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 10:
        nombre_mes = "octubre"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 11:
        nombre_mes = "noviembre"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case 12:
        nombre_mes = "diciembre"
        print("{0} de {1} de {2}".format(dia, nombre_mes, año))
    case _:
        print("El mes {0} no existe.".format(mes))
        