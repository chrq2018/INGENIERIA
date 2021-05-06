#Ejercicio 4.8. Definir una función “fecha_siguiente” que, dada por parámetros una fecha en
#números (día, mes, año), devuelva como resultado la fecha (día, mes, año) del día siguiente.
from misfunciones import fecha_valida


def fecha_siguiente(d, m, a):
    
    """
        recibe por parámetros una fecha en números (día, mes, año),
        devuelva como resultado la fecha (día, mes, año) del día siguiente.
    """

    d = d + 1

    if (m == 4 or m == 6 or m == 9 or m == 11) and d == 31:
        m = m + 1
        d = 1
    elif ( m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d == 32:
        m = m + 1
        d = 1
        if m == 13:
            a = a + 1
            m = 1
    elif m == 2 and (d == 30 or d == 29):
        m = m + 1
        d = 1

    return d,m,a

def main():
    dia = int(input("Ingrese dia como DD: "))
    mes = int(input("Ingrese mes como MM: "))
    anio = int(input("Ingrese año como AAAA: "))
    if fecha_valida(dia, mes, anio) == False:
        print("La fecha que ingreso no es valida")
    else:
        print("Fecha actual: ",dia,"/",mes,"/",anio)
        dia, mes, anio = fecha_siguiente(dia, mes, anio)
        print("Fecha siguiente: ",dia,"/",mes,"/",anio)

main()
