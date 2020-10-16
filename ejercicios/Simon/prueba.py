"""Curso Python/cisco/pildo"""

#Generadores en python, con la función yield

def numeros_pares(args):
    while args < 10:
        args+=1    
        if args%2==0:
            print(args,sep="-")
        
        elif args%2!=0:
            continue
        
        
numeros_pares(args=1)        



#Ejemplo Funcion map
#Ejemplo Funcion Enumerate
#Ejemplo Funcion Zip


    




