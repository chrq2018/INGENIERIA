def suma_n(num):
    """ recibe por parámetro un número natural num
        y devuelva como resultado la suma de naturales
        desde 1 hasta num (incluido). """
    s = 0
    for i in range(1, num + 1):
        s = s + i
    return s

def tabla_n(num):
    """ recibe por parámetro un número natural num,
        y muestre en pantalla, con descripciones expresivas,
        su tabla de multiplicar desde 0 hasta num (incluido). """
    print("tabla de multiplicar desde 0 hasta ",num,":")
    for i in range(num + 1):
        t = num * i
        print(num,"x",i,"=",t)

def main():
    n = int(input("Ingrese un número natural: "))
    print()
    tabla_n(n)
    sumatoria = n * ( n + 1 ) / 2
    print()
    print("sumatoria =", sumatoria, "(es el resultado de (",n," ∗ ( ",n," + 1 ) / 2))")
    print()
    sumatoria = sumatoria - suma_n(n)
    print("sumatoria =", sumatoria, "(es el resultado de (",n," ∗ ( ",n," + 1 ) / 2) - suma_n(",n,"))")


  
    
