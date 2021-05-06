#Ejercicio 5.9. Escribir un programa que le pida al usuario que ingrese una sucesión de
#calificaciones de estudiantes (primero el número de legajo, luego la calificación, y así para
#cada estudiante, hasta que el usuario ingrese el legajo -1 como condición de salida). Al
#final, el programa debe imprimir cuántas calificaciones fueron ingresadas, su valor máximo
#ingresado, la suma total de las calificaciones y el promedio.

def leer_legajo():
    l = input("Ingrese un legajo. (para terminar ingrese -1): ")
    return l

def leer_nota():
    n = input("Ingrese una nota: ")
    return n

def ingresar_calificaciones():
    legajo = int(leer_legajo())
    if legajo == -1:
        print("No ingresó calificaciones")
        return 
    nota = float(leer_nota())
    
    cant_nota = 0
    suma = 0
    max = nota
    while legajo != -1:
        if nota > max:
            max = nota
        suma = suma + nota
        cant_nota = cant_nota + 1
        legajo = int(leer_legajo())
        if legajo == -1:
            break
        nota = float(leer_nota())   
    print("Cantidad de calificaciones: ",cant_nota)
    print("la maxima calificaciones: ", max)
    print("La suma de las calificaciones: ", suma,)
    print("El promedio de las calificaciones: ", float(suma / cant_nota))

def main():
    ingresar_calificaciones()

main()   
    

        
        
        
        
