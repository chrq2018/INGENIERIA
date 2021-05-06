#Ejercicio 4.13. Escribir un programa de astrología que pida al usuario que ingrese el
#número de día y el número de mes correspondientes a su fecha de cumpleaños, e
#imprima en pantalla el signo del zodíaco al que pertenece. Considere las siguientes
#fechas:
#Aries: 21 de marzo al 20 de abril.
#Tauro: 21 de abril al 20 de mayo.
#Geminis: 21 de mayo al 20 de junio.
#Cáncer: 21 de junio al 21 de julio.
#Leo: 22 de julio al 22 de agosto.
#Virgo: 23 de agosto al 22 de septiembre.
#Libra: 23 de septiembre al 22 de octubre.
#Escorpio: 23 de octubre al 22 de noviembre.
#agitario: 23 de noviembre al 21 de diciembre.
#Capricornio: 22 de diciembre al 20 de enero.
#Acuario: 21 de enero al 19 de febrero.
#Piscis: 20 de febrero al 20 de marzo.

def signo_zodiaco(d, m):
    """ recibe por parametro el número de día y el número de mes correspondientes
        a su fecha de cumpleaños, e imprima en pantalla el signo del zodíaco al que
        pertenece. Considere las siguientes fechas:
        Aries: 21 de marzo al 20 de abril.
        Tauro: 21 de abril al 20 de mayo.
        Geminis: 21 de mayo al 20 de junio.
        Cáncer: 21 de junio al 21 de julio.
        Leo: 22 de julio al 22 de agosto.
        Virgo: 23 de agosto al 22 de septiembre.
        Libra: 23 de septiembre al 22 de octubre.
        Escorpio: 23 de octubre al 22 de noviembre.
        Sagitario: 23 de noviembre al 21 de diciembre.
        Capricornio: 22 de diciembre al 20 de enero.
        Acuario: 21 de enero al 19 de febrero.
        Piscis: 20 de febrero al 20 de marzo. """
    
    if (21 <= d <= 31 and m == 3) or (1 <= d <= 20 and m == 4):
        print ("Su signo es Aries")
        
    if (21 <= d <= 30 and m == 4) or (1 <= d <= 20 and m == 5):
        print ("Su signo es Tauro")
        
    if (21 <= d <= 31 and m == 5) or (1 <= d <= 20 and m == 6):
        print ("Su signo es Geminis")
        
    if (21 <= d <= 30 and m == 6) or (1 <= d <= 21 and m == 7):
        print ("Su signo es Cáncer")
        
    if (22 <= d <= 31 and m == 7) or (1 <= d <= 22 and m == 8):
        print ("Su signo es Leo")
        
    if (23 <= d <= 31 and m == 8) or (1 <= d <= 22 and m == 9):
        print ("Su signo es Virgo")
        
    if (23 <= d <= 30 and m == 9) or (1 <= d <= 22 and m == 10):
        print ("Su signo es Libra")
        
    if (23 <= d <= 31 and m == 10) or (1 <= d <= 22 and m == 11):
        print ("Su signo es Escorpio")
        
    if (23 <= d <= 30 and m == 11) or (1 <= d <= 21 and m == 12):
        print ("Su signo es Sagitario")
        
    if (22 <= d <= 31 and m == 12) or (1 <= d <= 20 and m == 1):
        print ("Su signo es Capricornio")
        
    if (21 <= d <= 31 and m == 1) or (1 <= d <= 19 and m == 2):
        print ("Su signo es Acuario")
        
    if (20 <= d <= 29 and m == 2) or (1 <= d <= 20 and m == 3):
        print ("Su signo es Piscis")

def main():
    dia = int(input("Ingrese el dia (DD) de su cumpleaños: "))
    mes = int(input("Ingrese el mes (MM) de su cumpleaños: "))
    signo_zodiaco(dia, mes)

main()








    
        
