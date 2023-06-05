def eliminar_espacios(texto):
    res = ""
    for i in texto:
        if i != " ":
            res =res+i
    return res