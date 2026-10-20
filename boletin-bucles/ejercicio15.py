c = "smx2026"
a = "s"
c_a = 0
i = 214
while a == "s":
    c_a = str(input("Contraseña: "))
    if c_a == c:
        print("Acceso concedido")
        break
    elif i == 0:
        print("Cuenta bloqueada")
        break
    else:
        print("Contraseña incorrecta. Te quedan", i, "intentos")
        i -= 1
    
    