#Ejercicio 5.2. Escribir un programa:
#a) que contenga una contraseña de 4 caracteres inventada, que le pregunte al usuario
#   la contraseña y no le permita continuar hasta que la haya ingresado correctamente.
#b) Modificar el programa anterior para que solamente permita una cantidad fija de
#   intentos. Al finalizar, deberá imprimir en pantalla “Eureka” si acertó la clave o, en
#caso contrario, “Clave incorrecta” y la cantidad de intentos fallidos.
#c) Modificar el programa anterior para que después de cada intento agregue una
#   pausa cada vez mayor, utilizando la función time.sleep(…) del módulo time.

import time

def leer_centinela():
    return input("ingrese contraseña: ")

def leer_contrasenia(c):
    """ recibe por parametro una contraseña de 4 caracteres inventada, que le pregunte al usuario
        la contraseña y no le permita continuar hasta que la haya ingresado correctamente.
        b) Modificar el programa anterior para que solamente permita una cantidad fija de
        intentos. Al finalizar, deberá imprimir en pantalla “Eureka” si acertó la clave o, en
        caso contrario, “Clave incorrecta” y la cantidad de intentos fallidos.
        c) Modificar el programa anterior para que después de cada intento agregue una
        pausa cada vez mayor, utilizando la función time.sleep(…) del módulo time."""

    t = 3
    cantidad = 1
    centinela = leer_centinela()
    while centinela != c and cantidad < 3:
        print("contraseña incorrecta")
        time.sleep(t)
        t = t + 2
        centinela = leer_centinela()
        cantidad = cantidad + 1
    if centinela == c:    
        print("Eureka")
    else:
        print("Clave incorrecta. Intentos fallidos: ",cantidad)

def main():
    contrasenia = "1234"
    leer_contrasenia(contrasenia)

main()
    
