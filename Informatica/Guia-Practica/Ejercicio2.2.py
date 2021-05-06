#Ejercicio 2.2. Ídem anterior: Escribir un programa Python que le solicite al usuario que
#ingrese el costo (en pesos) de cada uno de los siguientes dispositivos de almacenamiento:
# Memoria RAM de 4GB para PC
# Pendrive 16 GB
# Disco rígido interno 2 TB
#Considerando que en el Sistema Internacional de Unidades (Decimal) un Terabyte (TB)
#equivale a 1012 Gigabytes y un Gigabyte (GB) equivale a 109 Megabytes, el programa deberá informar
#en la pantalla:
#a) ¿Cuánto costaría almacenar 1 GB en cada uno de esos dispositivos?
#b) ¿Cuánto más cara (en forma relativa) es la memoria RAM que el pendrive?
#c) ¿Cuánto más cara (en forma relativa) es la memoria RAM que el disco rígido?
#d) ¿Cuánto más caro (en forma relativa) es el pendrive que el disco rígido?

def costo_almacenamiento(cantidad, precio):
    costo = precio / cantidad
    return costo

print("ingrese el costo (en pesos) de cada uno de los siguientes dispositivos de almacenamiento")
costo_ram = float(input("Memoria RAM de 4GB para PC cuesta: "))
costo_pendrive = float(input("Pendrive 16 GB cuesta: "))
costo_discorigido = float(input("Disco rígido interno 2 TB cuesta: "))


print("almacenar 1 GB en memoria RAM de 4GB para PC cuesta: ",costo_almacenamiento(4,costo_ram),"pesos")
print("almacenar 1 GB Pendrive 16 GB cuesta: ",costo_almacenamiento(16,costo_pendrive),"pesos")
print("almacenar 1 GB Disco rígido interno 2 TB cuesta: ",costo_almacenamiento(2000,costo_discorigido),"pesos")
print()
print("El pendrive es ",costo_almacenamiento(16,costo_pendrive)/costo_almacenamiento(2000,costo_discorigido),"veces mas caro que el disco rígido")
    
                          
                              


    
                    
