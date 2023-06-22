def agregar_texto_al_final(texto, texto_agregado):
    texto2=str.splitlines(texto)
    cont=0
    for i in texto2:
        texto2[cont]+=texto_agregado + "\n"
        cont+=1
    return("".join(map(str, texto2)))  
    # linea_modificada = texto.rstrip() + texto2
    # return linea_modificada

agregar_texto_al_final("Hola\nmundo","hola")


