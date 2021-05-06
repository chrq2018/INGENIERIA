#Ejercicio 4.2. Definir y documentar una función denominada “val_abs”, que reciba un
#número por parámetro y devuelva como resultado su valor absoluto. [No utilizar la función
#abs () provista por Python]

def val_abs(n):
    if n >= 0:
        return n
    else:
        return -n

def main():
    num = int(input("Ingrese un numero: "))
    print("el valor absoluto de ",num,"es ",val_abs(num))
    
main()
    
