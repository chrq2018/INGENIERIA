
# Ejercicio 1.4. Expresar la situación que se describe a continuación,
# a través de asignación sobre variables (Python 3) cuyos identificadores
# son dinero y paraguas:

# Bartolomé vende paraguas. Tiene 10 paraguas y $10000.
# a) Escriba instrucciones que permitan ver en pantalla los valores iniciales de las
# variables dinero y paraguas.


dinero = 10000
paraguas = 10
print("Bartolome tiene",dinero, "pesos  y" ,paraguas, "paraguas.")
cant_paraguas_vend = 5
precio_de_venta = 400
print()


# b)Agregue instrucciones que describan las respectivas variaciones que resultan de la
# venta de 5 paraguas, a $400 cada uno (utilice variables para representar la cantidad
# vendida y el precio de venta), y muestre en pantalla las consecuencias de la venta.

print("Vendió" ,cant_paraguas_vend, "paraguas a",precio_de_venta,"pesos cada uno.")
total_ventas = dinero + cant_paraguas_vend*precio_de_venta
total_paraguas = paraguas - cant_paraguas_vend
print("Bartolome tiene",total_ventas, "pesos  y" ,total_paraguas, "paraguas.")
print()



# c)Agregue instrucciones para representar y mostrar la venta de la mitad (entera) de
# paraguas restantes, con la respectiva variación de las variables dinero y paraguas.

cant_paraguas_vend = 5//2
print("Vendió" ,cant_paraguas_vend, "paraguas a",precio_de_venta,"pesos cada uno.")
total_ventas = total_ventas + cant_paraguas_vend*precio_de_venta
total_paraguas = total_paraguas - cant_paraguas_vend
print("Bartolome tiene",total_ventas, "pesos  y" ,total_paraguas, "paraguas.")



      


