texto = input("Texto: ").strip().lower()
limpio = ""
for caracter in texto:
    if caracter != " ":
        limpio = limpio + caracter
print("Texto sin espacios:", limpio)
invertido = ""
for caracter in limpio:
    invertido = caracter + invertido
if limpio == invertido:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
