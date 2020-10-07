'''
Escriba un programa que ponga en mayúscula los primeros cuatro caracteres de una cadena convirtiendo los caracteres a su equivalente ASCII,

Luego agregue la cantidad necesaria para ponerlos en mayúscula y vuelva a convertir los números enteros en caracteres.

Imprime la cadena en mayúscula.

Aquí hay una muestra de cómo ejecutar este programa.
'''

#Crear lista

#Solicitar cadena de texto
string = input("Escriba el texto que será usado: ")
lista = []
lista_asc = []
cant = int(input("Cantidad de dígitos: "))
#taman = len(var)

#Imprimir 4 primeros caracteres en Mayúsculas
print(str.upper(string[0:cant]) + string[cant:])

#identificar equivalentes en ASCII
for c in string:
    asc = ord(c)
    lista.append(asc)
  
print(lista)

#Identificar y guardar ASCII en la lista
for c in lista:
    ch = chr(c)
    lista_asc.append(ch)

#Sumar o restar ASCII para cambiar valores a Mayúsculas


#Imprimir cadena en Carácter
print(lista_asc)

exit()


