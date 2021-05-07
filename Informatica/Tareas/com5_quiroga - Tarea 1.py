def main():
    dinero = 10000
    sombreros = 13
    print("Bartolome vende sombreros. Tiene", sombreros, "y $",dinero)
    precio_venta = 800
    for i in range(2):
        cant_vendida = (sombreros // 2)
        dinero = dinero + (precio_venta * cant_vendida)
        sombreros = sombreros - cant_vendida
        print("Luego de vender", cant_vendida, "sombreros a $",precio_venta, "tiene", sombreros, "sombreros y $",dinero)
    
    
    
