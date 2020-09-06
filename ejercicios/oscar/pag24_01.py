"""
###############             Ejercicio pag24_01          #########################
Em muitos programas, nos é solicitado o preenchimento de algumas informações como
nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:
"""

nombre = input("Escriba su nombre: ")
cpf = input("Escriba su número de CPF: ")
edad = input("Escriba su edad: ")

print(f'''
        Su nombre es: {nombre}\n
        Su CPF es: {cpf}\n
        Su edad es: {edad}\n\n
        Gracias por usar nuestro sistema!
        ''')
exit()
