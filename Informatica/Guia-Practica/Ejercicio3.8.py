#Ejercicio 3.8. Definir (y documentar) una función que reciba un número n por parámetro
#y muestre en pantalla los primeros n números triangulares, junto con su índice (considerar
#que el número triangular de orden x se obtiene mediante la suma de los números naturales
#desde 1 hasta x). Es decir, si se piden los primeros 5 números triangulares, la función
#debería imprimir:
#1 - 1
#2 - 3
#3 - 6
#4 - 10
#5 - 15

def num_triangular(n):
    """ reciba un número n por parámetro y muestre en pantalla los primeros n números
        triangulares, junto con su índice (considerar que el número triangular de orden x
        se obtiene mediante la suma de los números naturales desde 1 hasta x). """
    suma = 0
    for i in range(1,n+1):
        suma = suma + i
        print(i,"-",suma)

        
def main():
    num = int(input("Ingrese un numero: "))
    num_triangular(num)

main()





