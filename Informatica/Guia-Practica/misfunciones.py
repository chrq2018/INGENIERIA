def potencia_cubo(b):
    """ Calcula e imprime el valor de cualquier numero n
        elevado al cubo  """
    return b**3


def potencia(b, e):
    """ Calcula e imprime el valor de cualquier numero n
        elevado a cualquier potencia """
    return b**e


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


def numero_pi():
    """ devuelva como resultado el valor redondeado del
        número PI: 3.14159 """
    return (round(math.pi,5))


def velocidad_descarga(b, t):
    """ reciba por parámetros la
        cantidad de bytes descargados y el tiempo expresado en minutos y segundos, y devuelva la
        velocidad de descarga expresada en kB/seg (kilobytes por segundo) """
    velocidad = (b / t)/1000
    return velocidad


def area_triangulo(b, a):
    """ recibe por parámetros dos números, cuyos valores representan la base y la
        altura de un triángulo, y devuelva como resultado el área respectiva. """
    return (b*a)/2


def num_triangular(n):
    """ reciba un número n por parámetro y muestre en pantalla los primeros n números
        triangulares, junto con su índice (considerar que el número triangular de orden x
        se obtiene mediante la suma de los números naturales desde 1 hasta x). """
    suma = 0
    for i in range(1,n+1):
        suma = suma + i
        print(i,"-",suma)

def factorial(n):
    """ que reciba un número natural por parámetro y
        devuelva como resultado su factorial (cuya definición
        matemática es: n ! = 1 x 2 x 3 x … x (n-1) x n ). """
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial        


def pinta_cuadro(n):
    """ reciba como parámetro un número natural n y dibuje con
        el carácter ‘x’ un cuadrado relleno, de lado igual al parámetro """
    for i in range(n):
        print('X'*n)

def domino_n(n):
    """ recibe como parámetro un número natural n y que
        imprima por pantalla, de una por línea y sin
        repetir, todas las fichas de un juego similar
        al dominó, incluyendo los números de 0 a n. """
    for i in range(n+1):
      for j in range(n+1):
          if i>=j:
            print(i,"|",j)


def suma_n(n):
    """ recibe como parámetro un número natural n y devuelva como resultado
        la suma de naturales desde 1 hasta n. """
    suma = 0
    for i in range(n+1):
        suma = suma + i
    return suma

def a_segundos(m, s):
    """ recibe como parametros minutos y segundos
        y devuelve como resultado segundos """
    s = s + (m * 60)
    return s


def fecha_valida(d, m, a):
    """recibe por parámetros una fecha en
        números (día, mes, año), devuelva un resultado
        booleano que indique si es válida o no."""
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


def es_primo(n):
    """ reciba por parametro un número entero por parámetro y devuelva
        un resultado booleano que indique si es primo, o no.
        [Un número natural es primo, si solamente es divisible
        por sí mismo y por 1]. """
    if n == 2 or n == 3 or n == 5:
        return True
    for i in range (2, n):
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 :
            return True
        else:
            return False


def rango_etario(e):
    """ que reciba por parámetro un número natural (que representa una edad)
        y devuelva como resultado la denominación de su respectivo grupo etario.
        Considere la siguiente clasificación:
        “primera infancia” (0 a 5 años),
        “infancia” (6 a 11 años),
        “adolescencia” (12 a 18 años),
        “juventud” (19 a 29 años),
        “adultez” (30 - 64 años) y
        “vejez” (65 años o más). """

    if 0 <= e <= 5:
        return "Primera infancia"
    elif 6 <= e <= 11:
        return "Infancia"
    elif 12 <= e <= 18:
        return "Adolecencia"
    elif 19 <= e <= 29:
        return "Juventud"
    elif 30 <= e <= 64:
        return "Adultes"
    else: 
        return "Vejez"


def nombre_dia(d):
    if d == 1:
        return "Domingo"
    elif d == 2:
        return "Lunes"
    elif d == 3:
        return "Martes"
    elif d == 4:
        return "Miércoles"
    elif d == 5:
        return "Jueves"
    elif d == 6:
        return "Viernes"
    elif d == 7:
        return "Sábado"



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


def leer_centinela():
    return input("Ingrese un numero. ('*' para salir): ")

        
def leer_numero():
    return input("Ingrese un numero: ")

def adivina_numero():
    intentos = 1
    n = random.randrange(1, 100)
    centinela = int(leer_numero())
    while centinela != n:
        if centinela > n:
            print("Incorrecto, mi numero es menor")
        elif centinela < n:
            print("Incorrecto, mi numero es mayor")
        centinela = int(leer_numero())
        intentos = intentos + 1
    print("El numero correct es:",centinela,". Y cantidad de intentos fueron: ",intentos)


def max_com_div(n, m):
    """ recibe por parámetro dos números n y m, devuelva como resultado el
        Máximo Común Divisor entre ambos, implementando el algoritmo
        de Euclides. Se describen a continuación los pasos de ese algoritmo matemático:
        1. Teniendo n y m, se obtiene r, el resto de la división entera de m / n.
        2. Si r es cero, entonces n es el MCD de los valores iniciales.
        3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
        Hacer un seguimiento del algoritmo implementado, para los pares de números: (15,9);
        (9,15); (10,8) y (12,6). """

    if m > n:
        aux = n
        n = m
        m = aux
          
    while m != 0:   
        r = m
        m = n % m
        n = r
    
    return n


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
