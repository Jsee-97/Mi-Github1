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

diccionario = {}
cond = 0

while (cond == 0):
    decision = int(input(f'''
        Quintada
        Presione 1 para ver cesta:
        Presione 2 para agregar frutas
        Presione 3 para salir
'''))

    while (decision not in range (1,4)):
        decision = int(input(f'Ingresó el número {decision}\n'
                           f'Por favor ingrese un valor entre 1-3: '))
    else:
        if decision == 1:
            print("No hay elementos en la lista")


        if decision == 2:
            fruta = int(input('''
                    Menu de frutas:

                    Escoge la fruta que deseas:
                    1: Cambur:
                    2: Patilla:
                    3: Fresa:
            '''))
            if fruta == 1:
                diccionario = {'fruta':'Cambur', 'prueba':'prueba1','prueba2':'prueba4'}
                print(diccionario)
            elif fruta == 2:
                diccionario = {'fruta2':'Patilla'}
            elif fruta == 3:
                diccionario = {'fruta3':'Fresa'}
        
        if decision == 3:
            print(f'Salió al apretar el botón {decision}')
            cond = 1


for chave in diccionario.keys():
    print(f'campo: {chave}:', diccionario[chave])


exit()
