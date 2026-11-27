registro = input("Registro: ")
separacion = registro.strip().split(";")
if len(separacion) != 5:
    print("Tiene {} y debe tener 5 campos".format(len(separacion)))
else:
    nombre = separacion[0].strip().capitalize()
    apellido = separacion[1].strip().capitalize()
    apellido2 = separacion[2].strip().capitalize()
    telefono = separacion[3]
    telefono_correcto = ""
    correo = separacion[4].strip().lower()
    for i in telefono:
        if i != " " and i != "-":  
            telefono_correcto += i
    union = nombre+";"+apellido+","+apellido2+";"+telefono_correcto+";"+correo
print("Registro original: {}".format(registro))
print("Registro normalizado: {}".format(union))