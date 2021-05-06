#Ejercicio 4.10. Definir una función denominada “es_primo”, que reciba un número
#entero por parámetro y devuelva un resultado booleano que indique si es primo, o no.
#[Un número natural es primo, si solamente es divisible por sí mismo y por 1].

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

def main():
    num = int(input("Ingrese un numero entero: "))
    if es_primo(num):
        print(num,"es Primo")
    else:
        print(num,"no es Primo")

main()

