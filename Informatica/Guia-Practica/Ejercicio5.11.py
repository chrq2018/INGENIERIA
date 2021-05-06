#Ejercicio 5.11. Modificar el programa del enunciado 5.3, para que el usuario pueda dar
#por terminado el juego, ingresando el valor 0.

import random

def leer_numero():
    return input("Ingrese un numero. (terminar con 0): ")

def adivina_numero():
    intentos = 1
    n = random.randrange(1, 100)
    centinela = int(leer_numero())
    if centinela == 0:
        mensaje = print("Finalizado")
        return mensaje
    
    while centinela != n and centinela != 0:
        
        if centinela > n:
            print("Incorrecto, mi numero es menor")
        elif centinela < n:
            print("Incorrecto, mi numero es mayor")
        centinela = int(leer_numero())
        intentos = intentos + 1
    if centinela == 0:
        print("Finalizado")
    else:
        print("El numero correcto es:",centinela,". Y cantidad de intentos fueron: ",intentos)

def main():
    adivina_numero()

main()    
            
    
