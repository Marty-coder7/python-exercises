e = 10
while e>0 and e<120:
    e = int(input("Introduce tu edad: "))
    if e>0 and e<120:
        print("Tu edad es ", e)
    else:
        print("Edad no válida")
        break
