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
lista2 = []
lista3 = []
lista4 = []
x = 0
lista_asc = []
cant = int(input("Cantidad de dígitos: "))
#taman = len(var)

#Imprimir 4 primeros caracteres en Mayúsculas
print('Mayúsculas con función automática: \n', str.upper(string[0:cant]) + string[cant:],'\n')


#identificar equivalentes en ASCII
for c in string:
    asc = ord(c)
    lista.append(asc)
  
#print(f'Lista normal en ASCII \n{lista}\n')

#obtener lista ASCII con las mayúsculas

for c in range(cant):
    asc = str.upper(string[x])
    x += 1
    lista2.append(asc)

string2 = ''.join(lista2)

for c in string2:
    ascc = ord(c)
    lista3.append(ascc)

print(lista)
print(lista3)


#Transformar de ACSII a Carácter
for c in lista:
    ch = chr(c)
    lista_asc.append(ch)

#Sumar o restar ASCII para cambiar valores a Mayúsculas
lista4 = map(sum, (lista, lista3))
print(lista4)


#concatenando la lista
#conc = ''.join(lista_asc)
#print(conc)

#Imprimir cadena en Carácter
#print(lista_asc)

exit()


