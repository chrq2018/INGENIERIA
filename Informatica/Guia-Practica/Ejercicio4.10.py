#Ejercicio 4.10. Definir una función denominada “es_primo”, que reciba un número
#entero por parámetro y devuelva un resultado booleano que indique si es primo, o no.
#[Un número natural es primo, si solamente es divisible por sí mismo y por 1].

def es_primo(n):
    """ reciba por parametro un número entero por parámetro y devuelva
        un resultado booleano que indique si es primo, o no.
        [Un número natural es primo, si solamente es divisible
        por sí mismo y por 1]. """
   
    for i in range (2, n):
        if n % i == 0 :
            return False
    return True

def main():
    num = int(input("Ingrese un numero entero: "))
    if es_primo(num):
        print(num,"es Primo")
    else:
        print(num,"no es Primo")

main()

