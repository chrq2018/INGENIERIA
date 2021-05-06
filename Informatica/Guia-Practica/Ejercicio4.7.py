#Ejercicio 4.7. Definir una función “fecha_valida” que, dada por parámetros una fecha en
#números (día, mes, año), devuelva un resultado booleano que indique si es válida o no.
#¿Qué función debería invocar?


def es_bisiesto(n):
    """ reciba por parámetro un número, que representa un año, y
        devuelva un resultado booleano que indique si es, o no
        es, bisiesto. """
    if n == 0:
        return False
    elif n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 400 == 0:
        return True
    else:
        return False
    
def fecha_valida(d, m, a):
    """
        recibe por parámetros una fecha en
        números (día, mes, año), devuelva un resultado
        booleano que indique si es válida o no.
    """
    dia = False
    mes = False
    anio = False
    
    if  a >= 1:
        anio = True
        
    if (m == 4 or m == 6 or m == 9 or m == 11) and (d >= 1 and d <= 30) :
        mes = True
        dia = True
        
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d == 31:
        mes = True
        dia = True
        
    if m == 2 and (d >= 1 and d <= 28):
        mes = True
        dia = True
        
    if m == 2 and d == 29 and es_bisiesto(a) == True:
        mes = True
        dia = True  
        
    if dia == True and mes == True and anio == True:
        return True
    else:
        return False


def main():
    
    dia = int(input("Ingrese el dia como DD: "))
    mes = int(input("Ingrese el mes como MM: "))
    anio = int(input("Ingrese el año como AAAA: "))

    fecha = fecha_valida(dia, mes, anio)
    
    if fecha == True:
        print("La fecha Ingresada: ",dia,"/",mes,"/",anio, "es valida")
    else:
        print("La fecha ingresada: ",dia,"/",mes,"/",anio, "no es valida")
        
main()    
        
    
