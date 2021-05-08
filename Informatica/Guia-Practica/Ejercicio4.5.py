#Ejercicio 4.5. Definir una función denominada “es_bisiesto” que reciba por parámetro un
#número, que representa un año, y devuelva un resultado booleano que indique si es, o no
#es, bisiesto. Pruebe la función para múltiplos de 4, de 100 y de 400. [Nota: un año es
#bisiesto si es un número divisible por 4, pero no es divisible por 100, excepto que
#también sea divisible por 400. Ejemplos: 1984 y 2000 son bisiestos, 1800 no es bisiesto].

def es_bisiesto(n):
    """ reciba por parámetro un número, que representa un año, y devuelva un resultado
        booleano que indique si es, o no es, bisiesto. Pruebe la función para múltiplos
        de 4, de 100 y de 400. [Nota: un año es bisiesto si es un número divisible por 4,
        pero no es divisible por 100, excepto que también sea divisible por 400.
        Ejemplos: 1984 y 2000 son bisiestos, 1800 no es bisiesto]. """
    if n == 0:
        return False
    elif n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 400 == 0:
        return True
    else:
        return False

def main():
    anio = int(input("Ingrese un año para saber si es bisiesto: "))
    if es_bisiesto(anio):
        print("El año",anio,"es bisiesto")
    else:
        print("El año",anio,"no es bisiesto")
main()
        
