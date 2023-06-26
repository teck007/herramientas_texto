def borrar_espacios_extra(texto):
    res=""
    p=1
    for i in texto:
        if i != " ":
            res=res+i
            p=1
        else:
            if p<=1:
                res=res+i
                p=p+1
    return res