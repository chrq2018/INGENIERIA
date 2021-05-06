#Ejercicio 5.12. Definir una función “reloj” que, dados por parámetro tres números
#naturales que representan la hora, los minutos y los segundos iniciales, imprima en
#pantalla, a cada segundo, la información horaria actualizada. Considere válidas las
#horas de 0:00:00 hasta 23:59:59. Utilice la función time.sleep(1) del módulo time.
import time
def reloj(h,m,s):
    """ Recibe por parámetro tres números naturales que representan la hora,
        los minutos y los segundos iniciales, imprima en pantalla, a cada segundo,
        la información horaria actualizada. Considere válidas las horas de 0:00:00 hasta 23:59:59.
        Utilice la función time.sleep(1) del módulo time. """
    while True:
        print (h,":",m,":",s)
        time.sleep(1)
        s = s + 1
        if s == 60:
            m = m + 1
            s = 0
            if m == 60:
                h = h + 1
                m = 0
                if h == 24:
                    h = 0
        
           
def main():
    hora = int(input("Introduzca la hora: "))
    minutos = int(input("Introduzca los minutos: "))
    segundos = int(input("Introduzca los segundos: "))
    
    reloj(hora,minutos,segundos)

main()
    
