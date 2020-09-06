'''
###############             Ejercicio pag24_03        #########################
Escreva um script em Python que receba dois números e que seja realizado as seguintes
operações:
             • soma dos dois números
             • diferença dos dois números
'''

num1 = int(input("Escriba el primer número : "))
num2 = int(input("Escriba el segundo número: "))

decision = int(input(f'''
                    Presione 1 para sumar 
                    Presione 2 para restar
                    Presione 3 para salir
'''))

while (decision not in range (1,4)):
    decision = int(input(f'Ingresó el número {decision}\n'
                         f'Por favor ingrese un valor entre 1-3: '))
else:
    if decision == 1:
        suma = num1 + num2
        print(f'la suma de los dos números es {suma}')
        
    if decision == 2:
        resta = num1 - num2
        print(f'la resta de los dos números es {resta}')
    
    if decision == 3:
        print(f'Salió al apretar el botón {decision}')
        exit()

exit()
