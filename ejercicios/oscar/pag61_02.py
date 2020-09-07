#2) Escreva uma calculadora utilizando funções anônimas


###############33###Funciones
#Limpiar pantalla
def cls():
    print('\n' * 100)

#Anónimas de calculadora
opcoes = {
    '1': lambda x,y: x+y,
    '2': lambda x,y: x-y,
    '3': lambda x,y: x*y,
    '4': lambda x,y: x/y,
    '5': print('Gracias por visita')
}

cond = 0
cls()
while cond == 0:
    n1 = float(input('Introduzca el primer número: '))
    n2 = float(input('Introduzca el segundo número: '))

    op = input('''
        Calculadora:

            Escoge la operación que desea realizar:
            1: Suma:
            2: Resta:
            3: Multiplicación:
            4: División:
    ''')

    if op in opcoes.keys():
        cls()
        print(f'El resultado de su operación es {opcoes[op](n1, n2)}')
    else:
        cls()
        print('opción inválida')

else:
    exit()
