# Ejercicio 1.8. Implementar algoritmos que resuelvan los siguientes problemas:
# a) Dado un número natural n, imprimir su tabla de multiplicar desde 0 hasta n.
# b) Dado un número natural n, imprimir la suma total de los naturales de 1 a n.


def tabla_multiplicar(n):
    """
    Dado un número natural n, imprimir su tabla de multiplicar desde 0 hasta n.
    """
    for i in range(0, n+1): "range(n+1) funcuiona igual"
        print(n, "x", i,"=" ,n*i)
    

def acumula(n):
    """
    Dado un número natural n, imprimir la suma total de los naturales de 1 a n.
    """
    suma_total = 0
    for i in range(1, n+1):
        suma_total = suma_total + i
    print("La suma total de los naturales de 1 hasta", n,"es: " ,suma_total)   


def main():
    n = int(input("ingrese un numero entero: "))
    print("Tabla de multiplicar del", n,"hasta",n,"es: ")
    tabla_multiplicar(n)
    print()
    m = int(input("ingrese un numero entero: "))
    acumula(m)

main()    


