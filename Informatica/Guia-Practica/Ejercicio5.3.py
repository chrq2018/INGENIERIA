#Ejercicio 5.3. Escribir un programa que elija un número al azar, entre 1 y 99, y lo mantenga
#en secreto (utilice la función random.randrange (1,100) del módulo random). El programa
#debe solicitar al usuario que adivine el número. Si el número que ingresa el usuario es
#mayor, el programa debe responder "Incorrecto, mi número es menor"; si el número
#ingresado es menor, el programa debe responder "Incorrecto, mi número es mayor". En
#ambos casos deberá solicitar otro número hasta que el usuario acierte el correcto. Mostrar la
#cantidad de intentos realizados para adivinar.

import random

def leer_numero():
    return input("Ingrese un numero: ")

def adivina_numero():
    intentos = 1
    n = random.randrange(1, 100)
    centinela = int(leer_numero())
    while centinela != n:
        if centinela > n:
            print("Incorrecto, mi numero es menor")
        elif centinela < n:
            print("Incorrecto, mi numero es mayor")
        centinela = int(leer_numero())
        intentos = intentos + 1
    print("El numero correcto es:",centinela,". Y cantidad de intentos fueron: ",intentos)

def main():
    adivina_numero()

main()    
            
    
