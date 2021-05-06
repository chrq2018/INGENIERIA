def ciclo_interactivo():
    hay_datos = "si"
    while hay_datos == "si":
        x = int(input("Ingrese un dato: "))
        if x > 0:
            print(x,"es positivo")
        elif x == 0:
            print(x,"es negativo")
        else:
            print(x,"es negativo")
        hay_datos = input("Quiere seguir? <si o no>: ")

def main():
    ciclo_interactivo()

main()


                
                
