#Ejercicio 2.1. Desarrolle los primeros 3 pasos de la metodología de construcción de
#programas, para el caso que se enuncia a continuación: Escribir un programa que le
#solicite al usuario una cantidad de pesos (capital), una tasa de interés anual (tasa) y un
#número entero de años (tiempo), para mostrar, como resultado, el monto final a obtener,
#de acuerdo a la fórmula:
# Cn = C x (1 + t / 100)n

#Donde C es el capital inicial, t es la tasa de interés y n es el tiempo en años.
#Identifique las variables con nombres adecuados a su significado.

capital = float(input("Ingrese el Capital: "))
tasa = float(input("Ingrese la tasa de interes anual: "))
tiempo = int(input("Ingres el tiempo en años: "))
resultado = capital*(1+tasa/100)**tiempo
print("El monto final es: ",resultado)

