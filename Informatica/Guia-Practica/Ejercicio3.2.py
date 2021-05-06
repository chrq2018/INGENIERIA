#Ejercicio 3.2. Definir (y documentar) con un nombre apropiado, una función:
#a) Que calcule e imprima el valor de cualquier número n elevado al cubo.
#b) Modificar la solución anterior, para que la función calcule cualquier potencia dada, de
#cualquier número dado y devuelva el resultado al programa principal. Pruebe la
#función con valores: 2 0, 2 1, 2 2, 2 3 y 36 0.5 . Consultar la documentación mediante la
#función help( ) provista por Python y verificar: ¿todavía describe adecuadamente lo
#que hace la función? ¿el nombre de la función sigue siendo apropiado?

def potencia_cubo(b):

    """ Calcula e imprime el valor de cualquier numero n
        elevado al cubo  """

    return b**3


def potencia(b, e):

    """ Calcula e imprime el valor de cualquier numero n
        elevado a cualquier potencia """

    return b**e

def main():
    base = int(input("ingrese la base: "))
    exp = int(input("ingrese el exponente: "))
    resultado = potencia(base,exp)
    print(base, "elevado al",exp, "es igual a: ",resultado)
    print()
    resultado = potencia_cubo(base)
    print(base, "elevado al cubo es igual a: ",resultado)
    print()
    help(potencia)
    help(potencia_cubo)

    for i in range(4):
        print("el valor de 2 elevado a la",i,"es",potencia(2,i))

main()    
