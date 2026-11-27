registro = input("Registro: ").strip()
campos = registro.split(";")
if len(campos) != 5:
    print("No es válido: tiene {} campos y debe tener 5".format(len(campos)))
else:
    invertido = ""
    for i in campos:
        if invertido == "":
            invertido = i
        else:
            invertido = i + ";" + invertido
    print("Registro original: {}".format(registro))
    print("Registro invertido: {}".format(invertido))
