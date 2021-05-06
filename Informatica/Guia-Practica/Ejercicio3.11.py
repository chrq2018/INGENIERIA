#Ejercicio 3.11. Definir una función denominada “pinta_cuadro”, que reciba como
#parámetro un número natural n y dibuje con el carácter ‘x’ un cuadrado relleno, de
#lado igual al parámetro. Ejemplo: pinta_cuadro (3)
#  xxx
#  xxx
#  xxx

def pinta_cuadro(n):
    """ reciba como parámetro un número natural n y dibuje con
        el carácter ‘x’ un cuadrado relleno, de lado igual al parámetro """
    for i in range(n):
        print('X'*n)

def main():
    num = int(input("ingrese un número entero: "))
    pinta_cuadro(num)

main()
