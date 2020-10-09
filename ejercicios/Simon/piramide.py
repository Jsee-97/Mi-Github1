bloques = int(input("Ingrese el número de bloques:"))
modulo = bloques
aux = 0
incremento = 0
contador = 0

while incremento <= bloques:
    modulo -= 1
  
  
    aux = bloques % modulo
    incremento += aux
    
    if incremento > bloques:
        break
    contador+=1
    if aux == 0:
        break
    
print("La altura de la pirámide es:", contador)







