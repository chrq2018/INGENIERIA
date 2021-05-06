#Ejercicio 5.6. Definir y documentar una función “es_potencia_de_dos” que reciba como
#parámetro un número natural, y devuelva el valor booleano True si el número es una
#potencia de 2, y False en caso contrario.


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
      

def main():
    num = int(input("Ingrese un numero: "))
    print(num,"Es potencia de 2 ?",es_potencia_de_dos(num))
    

main()

    
        
        
        
        
