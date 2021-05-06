#Ejercicio 3.7. Definir (y documentar) dos funciones. Una función …
#a) denominada “numero_pi”, que devuelva como resultado el valor redondeado del
#número PI: 3.14159. [Utilice el dato math.pi del módulo math y la función round(n, d) ]
#b) con nombre apropiado, que reciba el radio de un círculo por parámetro y devuelva
#como resultado el valor del área respectiva. Utilice la función del ítem a).

import math

def numero_pi():
    """ devuelva como resultado el valor redondeado del
        número PI: 3.14159 """
    return (round(math.pi,5))

def area_circulo(r):
    """ reciba el radio de un círculo por parámetro y devuelva
        como resultado el valor del área respectiva """
    return 2*r*numero_pi()

def main():
    radio = float(input("Ingrese el radio del circulo: "))
    area = round(area_circulo(radio),4)
    print("El area del circulo de radio", radio, "es: ", area)

main()    

    
