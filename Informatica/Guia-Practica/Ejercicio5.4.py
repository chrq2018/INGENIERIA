#Ejercicio 5.4. Definir una función “max_com_div” que, dados por parámetro dos números n
#y m, devuelva como resultado el Máximo Común Divisor entre ambos, implementando el
#algoritmo de Euclides. Se describen a continuación los pasos de ese algoritmo matemático:
#1. Teniendo n y m, se obtiene r, el resto de la división entera de m / n.
#2. Si r es cero, entonces n es el MCD de los valores iniciales.
#3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
#Hacer un seguimiento del algoritmo implementado, para los pares de números: (15,9);
#(9,15); (10,8) y (12,6).

def max_com_div(n, m):
    """ recibe por parámetro dos números n y m, devuelva como resultado el
        Máximo Común Divisor entre ambos, implementando el algoritmo
        de Euclides. Se describen a continuación los pasos de ese algoritmo matemático:
        1. Teniendo n y m, se obtiene r, el resto de la división entera de m / n.
        2. Si r es cero, entonces n es el MCD de los valores iniciales.
        3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
        Hacer un seguimiento del algoritmo implementado, para los pares de números: (15,9);
        (9,15); (10,8) y (12,6). """

    if m > n:
        aux = n
        n = m
        m = aux
          
    while m != 0:   
        r = m
        m = n % m
        n = r
    
    return n

def main():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese un numero: "))
    print("El MCD de",n1,"y",n2,"es",max_com_div(n1, n2))

main()
