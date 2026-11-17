nombre = input("Nombre del fichero: ")
nombre = nombre.strip().lower()
if len(nombre) < 5:
    print("No es válido: tiene {} caracteres y debe tener 5 o más.".format(len(nombre)))
else:
    sufijo = ""
    for i in range(-1, -5, -1):
        sufijo = nombre[i] + sufijo
    match sufijo:
        case ".jpg" | ".png" | ".gif":
            tipo = "imagen"
        case ".pdf" | ".odt" | ".txt":
            tipo = "documento"
        case ".mp3" | ".wav" | ".ogg":
            tipo = "audio"
        case _:
            tipo = "desconocido"
    print("Sufijo: {}".format(sufijo))
    print("Tipo de fichero: {}".format(tipo))
