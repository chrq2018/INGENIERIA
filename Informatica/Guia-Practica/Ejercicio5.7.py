#Ejercicio 5.7. Definir y documentar una función que, dados dos números naturales pasados
#como argumentos (parámetros de la función), devuelva la suma de todas las potencias de 2
#que hay en el rango formado por esos números (0, si no hay potencia de 2 entre ellos).
#Utilice la función “es_potencia_de_dos” del ejercicio anterior.


def es_potencia_de_dos(n):
    """ recibe como parámetro un número natural, y
    devuelva el valor booleano True si el número es una
    potencia de 2, y False en caso contrario. """

    p = 0
    potencia = 0
    if n < 1:
        return False
    
    while potencia < n:
        potencia = 2**p
        p = p + 1
    
    if potencia == n:
        return True
    else:
        return False


def suma_de_potencia_de_2(p, c):
    """ dados dos números naturales pasados como argumentos
        (parámetros de la función), devuelva la suma de todas
        las potencias de 2 que hay en el rango formado por esos
        números (0, si no hay potencia de 2 entre ellos).
        Utilice la función “es_potencia_de_dos” del ejercicio anterior."""
    suma = 0
    for i in range(p, c):
        if es_potencia_de_dos(i) == True:
            suma = suma + i
    return suma    
        

def main():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print("la suma de todas las potencias que hay entre",num1,"y",num2,"es: ",suma_de_potencia_de_2(num1, num2))

main()
