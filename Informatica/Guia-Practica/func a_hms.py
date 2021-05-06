def a_hms(segundos):
    """Dada una duración entera en segundos
       se la convierte en horas, minutos y segundos""" 
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 3600
    return h, m, s
