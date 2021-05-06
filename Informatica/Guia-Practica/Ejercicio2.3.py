#Ejercicio 2.3. Ídem anterior: Escribir un programa que solicite diez valores expresados en
#grados Fahrenheit y los muestre convertidos a grados Celsius. Considere que la fórmula
#para conversión de grados Celsius a grados Fahrenheit es:
#F = 9 / 5 x C + 32

"""
ANALISIS DEL PROBLEMA (cual es el problema): 

    El usuario nos pide escribir un programa que solicite diez valores expresados en
    grados Fahrenheit y los muestre convertidos a grados Celsius. Considere que la fórmula
    para conversión de grados Celsius a grados Fahrenheit es:

       F = 9 / 5 x C + 32

    Donde F es el valor ingresado en grados Fharenheit
    y C es el valor en grados Celsius se obtiene
    considerando la formula:  C = (F-32)*5/9
"""

"""
ESPECIFICACIÖN DEL PROBLEMA (que debe hacer el programa):
    El programa debe solicitar 10 valores expresados en grados Fahrenheit y
    devolver 10 valores enpresados en grados Celsius
    teniendo en cuenta la formula:  C = (F-32)*5/9
    Datos de entrada:
        - 10 valores en grados fharenheit
    Datos de salida:
        - 10 valores expresados en grados Celsius
"""

"""
DISEÑO (como vamos a resolver el problema):
    repetir 10 veces
        pedir al  usuario que ingrese un valor en grados fharenheit (referenciarlo con la variable F)
        calcular C = (F-32)*5/9
        mostrar por pantalla la variable C
    fin

"""

def fharenheit_a_celsius(f):
    c = float((f-32)*5/9)
    return c

print("Ingrese diez valores expresados en grados Fahrenheit")
print()
for i in range (1,11):
    fharenheit = float(input("Ingrese grados fahrenheit: "))
    print("Valor",i,":  equivale a ",'{:.2f}'.format(fharenheit_a_celsius(fharenheit),"grados Celsius"))
print("Gracias por ingresar los valores")          
    



