#Ejercicio 4.3. Definir una función denominada “mayor_de_3” que devuelva como resultado
#el mayor de tres números dados por parámetro. Pruebe la función con 6 ternas de valores.

def may_de_3(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def main():
    num1 = int(input("Ingrese un numero :"))
    num2 = int(input("Ingrese un numero :"))
    num3 = int(input("Ingrese un numero :"))
    print("el mayor de los tres numeros ingresados es: ",may_de_3(num1,num2,num3))

main()
        
    
    
        
    
