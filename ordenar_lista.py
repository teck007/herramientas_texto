def ordenar_lista(texto):
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    res=""
    for i in abc:
        for j in str.splitlines(str.lower(texto)):
            if i == j[0:1]:
                res=res+j+"\n"
    return res