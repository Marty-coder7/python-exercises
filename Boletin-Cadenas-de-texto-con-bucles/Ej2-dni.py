cadena = "TRWAGMYFPDXBNJZSQVHLCKE"
dni = input("DNI (8 cifras y una letra): ")
dni = dni.strip().upper()
if len(dni) != 9:
    print(f"No es válido: tiene {len(dni)} caracteres y debe tener 9.")
else:
    numero = int(dni[:8])
    letra_escrita = dni[-1]
    resto = numero % 23
    letra_correcta = cadena[resto]
    print(f"Resto de dividir {numero} entre 23: {resto}")
    if letra_escrita == letra_correcta:
        print(f"El DNI {dni} es correcto.")
    else:
        print(f"El DNI {dni} es incorrecto: la letra debe ser {letra_correcta}.")
