'''
1) Escreva uma função que receba um nome e que tenha como saída uma saudação. O argumento da função deverá ser o nome, e saída deverá ser como a seguir:
chamada da função: saudacao('Lalo')
saída: 'Olá Lalo! Tudo bem com você?'
'''

def saludo(arg):
    print(f'Hola {arg}, todo bien y tú?')


name = input('Ingresa tu nombre: ')

saludo(name)

exit()
