clase = 0

while True:
    octeto1 = int(input("Octeto 1:"))
    if octeto1 > 255:
        print("Ip no válida: el octeto 1 vale", octeto1)
        break
    octeto2 = int(input("Octeto 2:"))
    if octeto2 > 255:
        print("Ip no válida: el octeto 2 vale", octeto2)
        break
    octeto3 = int(input("Octeto 3:"))
    if octeto3 > 255:
        print("Ip no válida: el octeto 3 vale", octeto3)
        break
    octeto4 = int(input("Octeto 4:"))
    if octeto4 > 255:
        print("Ip no válida: el octeto 4 vale", octeto4)
        break
    if octeto1 <= 126:
        clase = "A"
    elif octeto1 == 127:
        clase = "Loopback (el propio equipo)"
    elif octeto1 >= 128 and octeto1 <= 191:
        clase = "B"
    elif octeto1 >= 192 and octeto1 <= 223:
        clase = "C"
    else:
        clase = "Otra(D,E o reservada)"
    ip = str(octeto1)+"."+str(octeto2)+"."+str(octeto3)+"."+str(octeto4)
    print("IP:",ip,"→ Clase",clase)
    break
