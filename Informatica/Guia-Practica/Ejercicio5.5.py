#Ejercicio 5.5. Escribir un programa que reciba, una a una, las calificaciones del usuario,
#preguntando a cada paso si desea ingresar más notas; finalmente, el programa debe
#imprimir el promedio correspondiente y el valor de la calificación más baja.


def leer_nota():
    ingresar = input("Desea ingresar mas notas (Para terminar ingrese 0): ")
    return ingresar


def calificaciones():
    """ reciba por , una a una, las calificaciones del usuario,
        preguntando a cada paso si desea ingresar más notas;
        finalmente, el programa debe imprimir el promedio
        correspondiente y el valor de la calificación más baja. """
    suma = 0
    cant = 0
    
    c = float(input("Desea ingresar mas notas (Para terminar ingrese 0): "))
    menor_nota = c
    while c != 0:
        
        if menor_nota > c:
            menor_nota = c
        suma = suma + c
        c = float(input("Desea ingresar mas notas (Para terminar ingrese 0): "))
        cant = cant + 1
    print("El promedio de las notas es:",suma / cant,". La nota mas baja es: ",menor_nota)

def main():
    
    calificaciones()

main()
    
    
        
        
    
