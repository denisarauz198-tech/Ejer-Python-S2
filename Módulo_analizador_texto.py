from collections import Counter

def contar_palabras(texto):
    c_palabras=texto.split()
    return len(c_palabras)
def contar_caracteres(texto):
    caracteres_t=len(texto)
    sin_espacios=texto.replace(' ','')
    conteos={'caracteres totales' : caracteres_t, 'sin espacios' : len(sin_espacios)}
    return conteos
def frecuencia_letras(texto):
    texto_limpio = texto.lower().replace(" ", "")
    dic_frecuencia=Counter(texto_limpio)
    res=dict(dic_frecuencia.most_common())
    return (res)
