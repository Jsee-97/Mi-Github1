"""
1.-Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
2.-Si es par, evalúa un nuevo c0 como c0 ÷ 2.
3.-De lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1.
Si c0 ≠ 1, salta al punto 2.
"""








c0 = int(input("Ingresa un numero natural: "))
contador = 0
def Collatz (c0,contador):
    while c0 > 0:
        if c0 == 1:
            break
        elif c0 % 2 == 0:
           c0 = int(c0 / 2)
        elif c0 % 2 != 0:
            c0 = (3*c0)+1
        contador+=1
        print(c0)
    print("Los paso empleados fueron:",contador)          
Collatz(c0,contador) 
