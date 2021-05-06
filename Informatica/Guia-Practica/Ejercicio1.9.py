# Ejercicio 1.9. Reescribir el programa del ejercicio 1.3 para que pida al usuario que ingrese
# la cantidad de agua inicial del tanque y la pileta, y que muestre los cambios, al transvasar
# un balde, luego otros dos, luego otros tres, luego otros cuatro y, finalmente, otros cinco.

def main():
    tanque = float(input("Ingrese la cantidad de agua que hay en el tanque: "))
    pileta = float(input("Ingrese la cantidad de agua que hay en el pileta: "))
    balde = float(input("Ingrese la cantidad de agua que hay en el balde: "))
    print ( 'El tanque contiene:',tanque,'litros de agua y la pileta:',pileta,'litros' )

    for i in range(1, 6):
        print ( 'Transvasa',i,'baldes de agua de:',balde,'litros' )
        tanque = tanque - i * balde
        pileta = pileta + i * balde
        print ( 'El tanque contiene:',tanque,'litros de agua y la pileta:',pileta,'litros' )

main()
