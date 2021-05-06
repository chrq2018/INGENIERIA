#Ejercicio 3.13. Definir una función denominada “suma_n”, que reciba como parámetro
#un número natural n y devuelva como resultado la suma de naturales desde 1 hasta n.

def suma_n(n):
    """ recibe como parámetro un número natural n y devuelva como resultado
        la suma de naturales desde 1 hasta n. """
    suma = 0
    for i in range(n+1):
        suma = suma + i
    return suma

def main():
    num = int(input("Ingrese un nemero natural: "))          
    print("La suma desde 1 hasta ", num,"es: ", suma_n(num))

main()              
