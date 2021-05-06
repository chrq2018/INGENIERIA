#Ejercicio 4.4. Escribir un programa que pida al usuario que ingrese dos números naturales,
#n1 y n2, e imprima en pantalla la secuencia de enteros comprendida entre n1 y n2
#(incluidos) con la siguiente particularidad: si el número es múltiplo de 3, en lugar del número
#debe imprimir “TRES”, si es múltiplo de 5, en vez del número debe imprimir “CINCO” y si es
#múltiplo de 3 y de 5, en lugar del número debe imprimir “TRES Y CINCO”.

def sec_entre_dosnum(n1, n2):
    for i in range(n1,n2 + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("TRES Y CINCO")
        elif i % 3 == 0:
            print("TRES")
        elif i % 5 == 0:
            print("CINCO")
        else:
            print(i)

def main():
    num1 = int(input("Ingrese un mumero natural: "))
    num2 = int(input("Ingrese un mumero natural: "))
    sec_entre_dosnum(num1,num2)

main()
        
