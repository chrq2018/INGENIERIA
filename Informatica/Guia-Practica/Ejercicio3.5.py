#Ejercicio 3.5. Definir (con nombre apropiado) una función que reciba por parámetros la
#cantidad de bytes descargados y el tiempo expresado en minutos y segundos, y devuelva la
#velocidad de descarga expresada en kB/seg (kilobytes por segundo). [Considere el Sistema
#Internacional de Unidades (Decimal) donde un kilobyte (kB) equivale a 103 bytes].

def a_segundos(m, s):
        """ recibe como parametros minutos y segundos
            y devuelve como resultado segundos """
    segundos = s + m*60
    return segundos
    

def velocidad_descarga(b, t):
    """ reciba por parámetros la cantidad de bytes descargados
        y el tiempo expresado en minutos y segundos, y devuelva la
        velocidad de descarga expresada en kB/seg (kilobytes por segundo) """
    velocidad = (b / t)/1000
    return velocidad

def main():
    
    byte = int(input("Ingrese la cantidad de byte: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    tiempo = a_segundos(minutos, segundos)
    resultado = velocidad_descarga(byte, tiempo)
    print("La velocidad de descarga es: ", round(resultado,4), "kB/seg")             

main()
