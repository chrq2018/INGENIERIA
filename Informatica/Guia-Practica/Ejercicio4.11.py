#Ejercicio 4.11. Definir una función denominada “rango_etario”, que reciba por
#parámetro un número natural (que representa una edad) y devuelva como resultado la
#denominación de su respectivo grupo etario. Considere la siguiente clasificación:
#“primera infancia” (0 a 5 años), “infancia” (6 a 11 años), “adolescencia” (12 a 18 años),
#“juventud” (19 a 29 años), “adultez” (30 - 64 años) y “vejez” (65 años o más).

def rango_etario(e):
    """ que reciba por parámetro un número natural (que representa una edad)
        y devuelva como resultado la denominación de su respectivo grupo etario.
        Considere la siguiente clasificación:
        “primera infancia” (0 a 5 años),
        “infancia” (6 a 11 años),
        “adolescencia” (12 a 18 años),
        “juventud” (19 a 29 años),
        “adultez” (30 - 64 años) y
        “vejez” (65 años o más). """

    if 0 <= e <= 5:
        return "Primera infancia"
    elif 6 <= e <= 11:
        return "Infancia"
    elif 12 <= e <= 18:
        return "Adolecencia"
    elif 19 <= e <= 29:
        return "Juventud"
    elif 30 <= e <= 64:
        return "Adultes"
    else: 
        return "Vejez"

def main():
    edad = int(input("Ingrese su edad: "))
    print("Su grupo etario es: ", rango_etario(edad))

main()
