import random

def pba_dados():
##    for tiro in range(10):
        dado_1 = random.randrange(1,7)
        dado_2 = random.randrange(1,7)
        print("mis dados son: ",dado_1," y ", dado_2)
        resulta = tira_dados_1(dado_1, dado_2)
        print("El resultado con",dado_1, " ", dado_2, " ",resulta, "es --->",resulta) 
        if (resulta != 1) and (resulta != -1):
            dado_1 = random.randrange(1,7)
            dado_2 = random.randrange(1,7)
            print("mis dados son: ",dado_1,"  ", dado_2)
            resulta_2 = tira_dados_2(dado_1, dado_2, resulta)
            print("El resultado con",dado_1, " ", dado_2," ",resulta, " es --->",resulta_2)    
        
def tira_dados_0(d_uno, d_dos):
    suma = d_uno + d_dos
    if suma == 11 or suma == 7:
        print("GANA con",d_uno," ",d_dos) 
    elif suma == 2 or suma == 3:
        print("PIERDE con",d_uno," ",d_dos)
    else:
        print("DEBE SALIR antes que 7, la suma", suma)
        

def tira_dados_1(d_uno, d_dos):
    suma = d_uno + d_dos
    if suma == 11 or suma == 7:
        return 1 
    elif suma == 2 or suma == 3:
        return -1
    else:
        return suma

def tira_dados_2(d_uno, d_dos, num_para_ganar):
    suma = d_uno + d_dos
    if  suma == num_para_ganar:
        return 1 
    elif suma == 7:
        return -1
    else:
        return 0    
    
def main():
    pba_dados()

main()
        
    
    
    




