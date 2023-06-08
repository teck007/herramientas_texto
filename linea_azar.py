from random import *
def linea_azar(texto):
    texto2=str.splitlines(texto)
    return choice(texto2)
                  

print(linea_azar("Nayareth\nMargarita\nSteffy"))
