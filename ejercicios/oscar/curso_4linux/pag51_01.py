'''
1) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração a qual a pessoa pertence.
Para definir a qual geração uma pessoa pertence temos a seguinte tabela: 
Geração         -   Intervalo
Baby Boomer     -   Até 1964
Geração X       -   1965 - 1979
Geração Y       -   1980 - 1994
Geração Z       -   1995 - Atual

Para testar se seu script está funcionando, considere os seguintes resultados esperados:
• ano nascimento = 1988: Geração: Y
• ano nascimento = 1958: Geração: Baby Boomer
• ano nascimento = 1996: Geração: Z
'''

ano = int(input("Cual es su año de nacimiento?"))


while (ano not in range (1900,2021)):
    ano = int(input("Por favor ingrese un año entre 1900 y 2020: "))

else:   
    if ano in range(1900,1965):
        print("Estás en la generación Baby Boomer")

    if ano in range(1965,1980):
        print("Estás en la generación X")

    if ano in range(1980,1995):
        print("Estás en la generación Y")

    if ano in range(1995,2021):
        print("Estás en la generación Z")

exit()
