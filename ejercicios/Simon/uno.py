nombre = input("Ingresa tu nombre: ")
contador = 0
arreglo = []
for elemento in nombre:
    if contador < 4:
        arreglo.append(elemento.upper())
        contador+=1

        print("La letra '{}'es equivalente en ASCII a '{}'".format(elemento.upper(),ord(elemento))) 
    else:
         break

aux1 = ord(arreglo[0])     
aux2 = ord(arreglo[1])
aux3 = ord(arreglo[2])
aux4 = ord(arreglo[3])

print("\"Mi nombre es:\"",chr(aux1),chr(aux2),chr(aux3),chr(aux4))

