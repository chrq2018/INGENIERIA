def leer_centinela():
    return input("Ingrese un numero. ('*' para salir): ")

def leer_numero():
    centinela = leer_centinela()
    while centinela != '*':
        x = int(centinela)
        if x > 0:
            print(x, "es positivo")
        elif x == 0:
            print(x, "es cero")
        else:
            print(x, "es negativo")
        centinela = leer_centinela()

def main():
    leer_numero()

main()
    
