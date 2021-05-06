def a_hms(segundos):
    """ Dada una duración entera en segundos
       se la convierte en horas, minutos y segundos """ 
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 3600
    return h, m, s


def a_segundos(horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo expresada en
        horas, minutos y segundos """
    return 3600 * horas + 60 * minutos + segundos

def main():
    segundos = a_segundos(2,3,33)
    print("Segundos: ",segundos)
    h,m,s = a_hms(10000)	
    print("Horas:",h, "   Minutos:",m, "   Segundos:",s)

main()    
    
    
