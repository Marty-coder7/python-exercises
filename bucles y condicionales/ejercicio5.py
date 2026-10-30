cambio_a_devolver = int(input("Cambio a devolver: "))
if cambio_a_devolver%5 != 0 and cambio_a_devolver > 0:
    print("La cantidad a devolver debe ser multiplo de 5 o mayor que 0")
else:
    while cambio_a_devolver != 0:
        if cambio_a_devolver >= 50:
            cambio_a_devolver -= 50
            print("Billete de 50")
        elif cambio_a_devolver >= 20:
            cambio_a_devolver -= 20
            print("Billete de 20")
        elif cambio_a_devolver >= 10:
            cambio_a_devolver -= 10
            print("Billete de 10")
        else:
            cambio_a_devolver -= 5
            print("Billete de 5")
        if cambio_a_devolver == 0:
            break
            