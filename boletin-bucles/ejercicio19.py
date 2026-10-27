while True:
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 0:
        print("¡Hasta pronto!")
        break
    elif opcion in [1, 2, 3, 4]:
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))
        
        if opcion == 1:
            print(f"Resultado: {num1 + num2}")
        elif opcion == 2:
            print(f"Resultado: {num1 - num2}")
        elif opcion == 3:
            print(f"Resultado: {num1 * num2}")
        elif opcion == 4:
            if num2 == 0:
                print("No se puede dividir entre 0")
            else:
                print(f"Resultado: {num1 / num2}")
    else:
        print("Opción no válida")
