'''
2) Aproveitando o exercício anterior, incremente a sua quitanda para consolidar o valor total de sua cesta de compras. Deverá ser adicionado ao seu menu inicial a opção checkout e esta deverá listar os produtos de sua cesta bem como o valor total:
----------------------------------------------------
Menu:
        1: Ver cesta
2: Adicionar Frutas
3: Checkout
4: Sair
Digite a opção desejada:
---------------------------------------------------
A saída do checkout deverá ser da seguinte maneira:

Total de compras: 15,00
Cesta de compras: Banana, Morango, Melancia

'''
#Condiciones
dic = {}
cond = 0

#Funciones

def cls():
    print('\n' * 100)
    
#While General del menu principal

while (cond == 0):
    decision = int(input(f'''
        Quintanda
        Presione 1 para ver cesta:
        Presione 2 para agregar frutas
        Presione 3 para Chekout
        Presione 4 para salir
'''))


#While descartando que el número esté entre 1 y 4
    while (decision not in range (1,5)):
        cls()
        decision = int(input(f'Ingresó el número {decision}\n'
                           f'Por favor ingrese un valor entre 1-4: '))

#Opciones si el número está entre 1-4
    else:
        

        #Mostrar lista de productos
        if decision == 1:
            cls()
            if len(dic) <= 0:
                print('La cesta está vacía')
            
            else:
                print('\n'* 100)               
                print('Su Cesta tiene los siguientes productos')
                for key in dic:
                    print(f'Producto {key}: {dic[key]}')


        #Agregar productos
        if decision == 2:
            cls()
            fruta = int(input('''
                    Menu de frutas:

                    Escoge la fruta que deseas:
                    1: Cambur:
                    2: Patilla:
                    3: Fresa:
        '''))

            if fruta not in range(1,4):
                cls()
                print('Producto no está en la lista')

            elif fruta == 1:
                cls()
                dic['Cambur'] = 3.5
                print(f'\n\nSe agregó el producto Cambur, preço: {dic["Cambur"]}\n\n')
        
            elif fruta == 2:
                cls()
                dic['Patilla'] = 5
                print(f'\n\nSe agregó el producto Patilla, preço: {dic["Patilla"]}\n\n')

            elif fruta == 3:
                cls()
                dic['Fresa'] = 4
                print(f'\n\nSe agregó el producto Fresa, preço: {dic["Fresa"]}\n\n')
    
        #Opción para Checkout
        if decision == 3:
            cls()
#            suma = sum(dic.values())
            print(f'La suma de sus productos es: {sum(dic.values())}')

        #Opción para Salir
        if decision == 4:
            cls()
            print(f'Salió al apretar el botón {decision}')
            cond = 1 
exit()

