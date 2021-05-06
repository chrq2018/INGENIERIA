#Ejercicio4.6. Definir una función “cant_dias_mes” que, dados por parámetro dos números,
#que representan el mes y el año, devuelva como resultado la cantidad de días
#correspondientes al mes. En la definición se debe invocar a la función del enunciado 4.5.

from misfunciones import es_bisiesto

"""
def es_bisiesto(n):
    if n == 0:
        return False
    elif n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 400 == 0:
        return True
    else:
        return False

"""
 
def cant_dias_mes(a, m):
    
    if m == 1:
        dias = 31
        
    if m == 2 and es_bisiesto(a):
        dias = 29
    else:
        dias = 28

    if m == 3:
        dias = 31

    if m == 4:
        dias = 30

    if m == 5:
        dias = 31

    if m == 6:
        dias = 30

    if m == 7:
        dias = 31

    if m == 8:
        dias = 31

    if m == 9:
        dias = 30

    if m == 10:
        dias = 31

    if m == 11:
        dias = 30

    if m == 12:
        dias = 31    
        
    return dias


def main():
    anio = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))

    dias = cant_dias_mes(anio,mes)

    print("El mes",mes,"tiene ",dias,"dias")

main()
