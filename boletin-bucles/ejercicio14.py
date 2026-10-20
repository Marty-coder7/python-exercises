c = "smx2026"
a = "s"
c_a = 0
while a == "s":
    c_a = str(input("Contraseña: "))
    if c_a == c:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta")
    