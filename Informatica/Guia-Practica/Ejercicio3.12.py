#Ejercicio3.12. Definir una función denominada “domino_n”, que reciba como
#parámetro un número natural n y que imprima por pantalla, de una por línea y sin
#repetir, todas las fichas de un juego similar al dominó, incluyendo los números de 0 a n.

def domino_n(n):
    """ recibe como parámetro un número natural n y que
        imprima por pantalla, de una por línea y sin
        repetir, todas las fichas de un juego similar
        al dominó, incluyendo los números de 0 a n. """
    for i in range(n+1):
      for j in range(n+1):
          if i>=j:
            print(i,"|",j)  

def main():
    num = int(input("Ingrese un numero: "))
    domino_n(num)
    
main()
    
