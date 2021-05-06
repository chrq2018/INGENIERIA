#Ejercicio 5.1. Considerando la siguiente función para obtener la multiplicación de dos
#números, por sumas sucesivas:


def prod_en_sumas_for (num, cant):
    """Calcula el producto de dos números por sumas sucesivas"""
    prod = 0
    for i in range(cant):
        prod = prod + num
    return prod

def main():
    numero = int(input("Ingrese un numero: "))
    cantidad = int(input("Ingrese la cantidad: "))
    print("El producto entre",numero, "y", cantidad,"por sumas sucesivas es: ", prod_en_sumas_for(numero, cantidad))

main()    
