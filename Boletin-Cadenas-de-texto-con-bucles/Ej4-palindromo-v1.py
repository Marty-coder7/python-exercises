texto = input("Texto: ").strip().lower()
limpio = ""
for caracter in texto:
    if caracter != " ":
        limpio = limpio + caracter
print("Texto sin espacios:", limpio)
es_palindromo = True
for i in range(len(limpio)):
    if limpio[i] != limpio[len(limpio) - 1 - i]:
        es_palindromo = False
if es_palindromo:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
