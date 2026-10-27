bisiestos = 0

while True:
    año_inicial = int(input("Año inicial: "))
    año_final = int(input("Año final: "))
    if año_inicial > año_final:
        print("El año inicial no puede ser mayor que el final")
    else:
        for i in range(año_inicial,año_final+1):
            if (i%4 == 0 and i%100 != 0) or (i%400 == 0):
                print(i)
                bisiestos += 1
        print("Hay", bisiestos, "años bisiestos")
        break