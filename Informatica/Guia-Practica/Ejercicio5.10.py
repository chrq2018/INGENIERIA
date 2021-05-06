#Ejercicio 5.10. Definir una función que reciba como parámetro un número natural e
#imprima todos los números primos que hay hasta ese número.


def es_primo(n):
    """ reciba por parametro un número entero por parámetro y devuelva
        un resultado booleano que indique si es primo, o no.
        [Un número natural es primo, si solamente es divisible
        por sí mismo y por 1]. """
    if n == 2 or n == 3 or n == 5:
        return True
    for i in range (2, n):
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 :
            return True
        else:
            return False


def todos_los_numeros_primos(n):
    """ recibe como parámetro un número natural e imprima
        todos los números primos que hay hasta ese número. """

    for i in range(1,n+1):
        if es_primo(i) == True:
            print(i)

def main():
    num = int(input("Ingrese un numero: "))
    todos_los_numeros_primos(num)

main()    
