#Ejercicio 3.1. Mostrar el resultado de ejecutar en Python 3 la función main() y elaborar
#conclusiones (señalar definiciones e invocaciones de función, distinguir formas de
#invocación, señalar argumentos y cambios de estado en parámetros, finalmente ejecutar la
#instrucción comentada con #):

def triplica(param):
    """ Recibe valor en param y devuelve el valor de resulta """
    resulta = param * 3
    return resulta

def prueba_triplica(entrada):
    """ Recibe valor en entrada y muestra resultados de invocaciones """
    print ( '---[ Debug:] valor del parametro', entrada )
    salida = triplica(entrada)
    print ( 'La salida de', entrada, 'es ==>', salida )
    entrada = 'alfa'
    print ( '\n---[ Debug:] valor del argumento es', entrada )
    salida = triplica(entrada)
    print ( 'La salida de', entrada, 'es ==>', salida )
    print ( '---[ Debug:] valor del parametro', entrada )
    print ( '\nError de invocacion sin parentesis ==>', triplica )        
        
def main():
    prueba_triplica(8)
    print ( '\n-[ Debug:]: valor del argumento es 200' )
    print ( 'La salida de', 200, 'es ==>', triplica(200) )
    print ('\nError: invoca sin argumentos ==>', triplica())
    
main()
