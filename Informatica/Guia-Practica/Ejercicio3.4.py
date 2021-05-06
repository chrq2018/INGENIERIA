#Ejercicio 3.4. Escribir un programa que lea de teclado dos tiempos expresados en horas,
#minutos y segundos, los sume y muestre por pantalla el resultado en horas, minutos y
#segundos. El programa deberá utilizar las funciones del ejercicio anterior.

def a_hms(segundos):
    """ Dada una duración entera en segundos
        se la convierte en horas, minutos y segundos""" 
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s


def a_segundos(horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo expresada en
        horas, minutos y segundos"""
    return 3600 * horas + 60 * minutos + segundos


def main():
    print("Ingrese dos tiempos expresados en horas, minutos y segundos")
    tiempo_suma = 0
    for i in range (2):
        horas = int(input("ingrese horas: "))
        minutos = int(input("ingrese minutos: "))
        segundos = int(input("ingrese segundos: "))
        tiempo_suma = tiempo_suma + a_segundos(horas, minutos, segundos)
        
    h,m,s = a_hms(tiempo_suma)
    print("Total horas: ", h, "Total minutos:", m, "Total segundos", s)

main()
