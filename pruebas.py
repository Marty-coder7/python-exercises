cad1=input("cadena 1:")
cad2=input("cadena 2:")
esSufijo = True
for i in range(-1,-1*len(cad2),-1):
    if cad1[i] != cad2[2]:
        esSufijo = False
        break
if esSufijo:
    print("Es sufij")
else:
    print("No es sufijo")