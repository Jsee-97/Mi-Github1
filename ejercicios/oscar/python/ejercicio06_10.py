'''
Escriba un programa que ponga en mayúscula los primeros cuatro caracteres de una cadena convirtiendo los caracteres a su equivalente ASCII,

Luego agregue la cantidad necesaria para ponerlos en mayúscula y vuelva a convertir los números enteros en caracteres.

Imprime la cadena en mayúscula.

Aquí hay una muestra de cómo ejecutar este programa.
'''


#Variables
lista = []
contenedor = []
lista2 = []
cant_num = []
suma_lista = []
x = 0
lista_ch = []

#Funciones
#Convertir Texto a ASCII
def text_ascii(s,l):
    for i in s:
        asc = ord(i)
        l.append(asc)

#Solicitar cadena de texto y cantidad de dígitos al usuário
string = input("Escriba el texto que será usado: ")
cant = int(input("Cantidad de dígitos: "))


#Imprimir 4 primeros caracteres en Mayúsculas usando función de Python3
print('\nMayúsculas con función automática: \n', str.upper(string[0:cant]) + string[cant:],'\n')


#identificar equivalentes en ASCII
text_ascii(string,lista)
 

#obtener lista ASCII con las mayúsculas
for c in range(cant):
    asc = str.upper(string[x])
    x += 1
    contenedor.append(asc)

string2 = ''.join(contenedor)
text_ascii(string2, lista2)
print(f'\nLista en minúsculas ASCII:\n{lista}\n')


#Calcular cantidad de números entre mayúsculas y minúsculas ASCII
for i in range(cant):
    cant_num.append(lista[i] - lista2[i])

print(f'\nDiferencia entre caracteres:\n {cant_num}\n')

#Calcular lista final en ASCII
for i in range(cant):
    lista[i] = lista[i] - cant_num[i]


print(f'\nLista en Mayúsculas ASCII:\n {lista2}\n')
print(f'\nLista final en ASCII:\n {lista}\n')

#Transformar de ACSII a Carácter
for c in lista:
    ch = chr(c)
    lista_ch.append(ch)

#concatenando la lista
result = ''.join(lista_ch)
print(f'\nLista en Caracteres usando la lista transformada:\n{result}')


exit()
