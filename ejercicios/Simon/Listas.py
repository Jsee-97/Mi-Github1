from random import sample



lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
#Algoritmo de Arreglo le paso el parametro args(en args lo que importa es el *),que me permite pasar multiple cantidad de parametros
def inserta_lista(*args):
    #Genero n° aleatorios en rango de 0 a 20, y los almaceno en 2 listas
    lista_random = range(0,20)
    lista1 = sample(lista_random,10)
    lista2 = sample(lista_random,10)
    print('Esta es mi lista 1:',lista1,'\nEsta es mi lista 2: ',lista2)
    #Con Enumerate almaceno la llave de cada valor;asigno un numero al indice del elemento 
    for key,value in enumerate(lista1):
   
       if key % 2 == 0:
         lista3.append(value)
       else:
         lista6.append(value)
    #Con Enumerate almaceno la llave de cada valor;asigno un numero al indice del elemento
    for key,value in enumerate(lista2):
       if key % 2 != 0:
        lista4.append(value)
       else:
        lista6.append(value)
    #Con zip puedo evaluar dos o mas listas de forma simultanea    
    for i,e in zip(lista3,lista4):
        lista5.append(i)
        lista5.append(e)
    #El remanente de mi lista lo ordeno de forma ascendente con la funcion sorted    
    resto = sorted(lista6)
    

    #print(lista5) 
    #Concateno mis dos listas    
    lista_total = lista5 + resto 
    print('Esta es mi lista organizada: ',lista_total)
#Llamo a la funcion y le remito los parametros       
inserta_lista(lista1,lista2,lista3,lista4,lista5,lista6)               

