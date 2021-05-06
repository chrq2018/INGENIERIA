#Ejercicio 4.12. Definir una función “nombre_dia” que, dado por parámetro un número
#de día de la semana, devuelva como resultado su nombre. Considere 2do día a “lunes”.

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
    

def main():
    dia = int(input("Ingrese un número entre 1 y 7: "))
    if 1 <= dia <= 7:
        print(dia, "es igual a ", nombre_dia(dia))
    else:
        print("El número que ingresó no es válido")

main()


    
    
    
