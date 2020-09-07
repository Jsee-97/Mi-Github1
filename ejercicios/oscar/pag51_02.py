'''
###############             Ejercicio pag51_02        #########################
2) Escreva um script em python que represente uma quitanda. O seu programa deverá apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta deverá ser adicionada a uma cesta de compras.
Menu principal:
1: Quitanda:
2: Ver cesta
3: Adicionar frutas
4: Sair
5: Digite a opção desejada:


Menú de Frutas:

Escolha fruta desejada:
1 - Banana
2 - Melancia
3 - Morango

Digite à opção desejada: 2
Melancia adicionada com sucesso!

Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.

Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem Digite uma opção inválida)

O programa deverá ser encerrado apenas se o usuário digitar a opção 3.

2) Aproveitando o exercício anterior, incremente a sua quitanda para consolidar o valor
total de sua cesta de compras. Deverá ser adicionado ao seu menu inicial a opção
checkout e esta deverá listar os produtos de sua cesta bem como o valor total:

Menu:
1: Ver cesta
2: Adicionar Frutas
3: Checkout
4: Sair
Digite a opção desejada:
A saída do checkout deverá ser da seguinte maneira:
1
2
Total de compras: 15,00
Cesta de compras: Banana, Morango, Melancia
Considere os seguintes preços:
Banana: 3.50 Melancia: 7.50 Morango: 5.00
Dica: Você pode armazenar os dados de frutas e seus respectivos preços em um dicionário.
'''
#Condiciones
lista = []
cond = 0

#Funciones

def cls():
    print('\n' * 100)
    
#While General del menu principal

while (cond == 0):
    decision = int(input(f'''
        Quintada
        Presione 1 para ver cesta:
        Presione 2 para agregar frutas
        Presione 3 para salir
'''))


#While descartando que el número esté entre 1 y 3    
    while (decision not in range (1,4)):
        cls()
        decision = int(input(f'Ingresó el número {decision}\n'
                           f'Por favor ingrese un valor entre 1-3: '))

#Opciones si el número está entre 1-3
    else:
        

        #Mostrar lista de productos
        if decision == 1:
            cls()
            if len(lista) <= 0:
                print('La cesta está vacía')
            
            else:
                print('\n'* 100)               
                print('Su Cesta tiene los siguientes productos')
                for index, element in enumerate(lista):
                    print(f'Producto {index + 1}: {element}')


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
                lista.append('Cambur')
                print(f'\n\nSe agregó el producto {lista[-1]}\n\n')
            
                elif fruta == 2:
                cls()
                lista.append('Patilla')
                print(f'\n\nSe agregó el producto {lista[-1]}\n\n')
 
            elif fruta == 3:
                cls()
                lista.append('Fresa')
                print(f'\n\nSe agregó el producto {lista[-1]}\n\n')
        
        #Opción para Salir
        if decision == 3:
            cls()
            print(f'Salió al apretar el botón {decision}')
            cond = 1 
exit()

