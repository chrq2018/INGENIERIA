def main():
    dinero = 10000
    sombreros = 13
    print("Bartolome es vendedor de sombreros. Tiene", sombreros, "y $",dinero)
    print()
    precio_venta = 800
    for i in range(2):
        cant_vendida = (sombreros // 2)
        dinero = dinero + (precio_venta * cant_vendida)
        sombreros = sombreros - cant_vendida
        print("Bartolome vende", cant_vendida, "sombreros a $",precio_venta)
        print("Bartolome ahora tiene", sombreros, "sombreros y $",dinero)
        print()
main()    
