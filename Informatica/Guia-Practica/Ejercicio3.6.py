#Ejercicio 3.6. Definir (y documentar) con un nombre apropiado, una función que reciba por
#parámetros dos números, cuyos valores representan la base y la altura de un triángulo, y
#devuelva como resultado el área respectiva. Pruebe la función con los pares (2, 4) y (3, 5).

def area_triangulo(b, a):
    """ recibe por parámetros dos números, cuyos valores representan la base y la
        altura de un triángulo, y devuelva como resultado el área respectiva. """

    return (b*a)/2

def main():
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = area_triangulo(base, altura)
    print("El area del triangulo de base",base, "y altura",altura,"es: ",area)

main()
