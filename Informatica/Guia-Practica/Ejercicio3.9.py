#Ejercicio 3.9. Definir (y documentar) una función denominada “factorial”, que reciba un
#número natural por parámetro y devuelva como resultado su factorial (cuya definición
#matemática es: n ! = 1 x 2 x 3 x … x (n-1) x n ).

def factorial(n):
    """ que reciba un número natural por parámetro y
        devuelva como resultado su factorial (cuya definición
        matemática es: n ! = 1 x 2 x 3 x … x (n-1) x n ). """
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

def main():
    num = int(input("ingrese un num: "))
    resultado = factorial(num)
    print("El factorial de",num,"es: ",resultado)

main()
    
