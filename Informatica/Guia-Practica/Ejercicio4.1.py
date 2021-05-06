#Ejercicio 4.1. Definir y documentar : …
    #a) una función denominada “es_par” que, dado un número entero por parámetro,
    #devuelva un valor booleano que indique si es par, o no. Dé un ejemplo de invocación.
    #b) Modificar la solución anterior, para que devuelva como resultado “S” si es par, “N” si
    #es impar o “0” si es cero. Consulte la documentación mediante la función help ().

def es_par(n):
    if n % 2 == 0:
     return True

def main():
    num = int(input("Ingrese un numero: "))
    if es_par(num):
        print("El numero ingresado es Par")
    else:
        print("El numero ingresado es Impar")

        
main()
