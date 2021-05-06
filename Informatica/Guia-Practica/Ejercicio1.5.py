
# Ejercicio 1.5. Implementar algoritmos que permitan:

# a) Obtener el perímetro de un rectángulo, dada su base y su altura.
    
print("Vamos a calcular el Perímetro y el Area de un rectángulo, dada su base y su altura.")
base = float(input("Ingrese la base de un rectangulo: "))
altura = float(input("Ingrese la altura de un rectangulo: "))             
perimetro = 2*(base+altura)
area = base*altura
print()
print("El primetro del rectangulo es igual a:",perimetro)
              

# b) Obtener el área de un rectángulo, dada su base y su altura.

print("El area del rectangulo es igual a:",area) 
print()

# c) Dados dos números n1 y n2, indicar la suma, resta, multiplicación, división y división
# entera de ambos. Analizar el resultado, con los números: 5 y 2 ; 2 y 5 ; 5 y 0.


print("Dados dos números n1 y n2, vamos a calcular la suma, resta, multiplicación, división y división entera de ambos.")
n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese otro numero (debe ser distinto de cero): "))
suma = n1+n2
resta = n1-n2
multiplicacion = n1*n2
division = n1/n2
division_entera = n1//n2

print("La suma es igual a: ",suma)
print("La resta es igual a: ",resta)
print("La multiplicacion es igual a: ",multiplicacion)
print("La division es igual a: ",division)
print("La division_entera es igual a: ",division_entera)



