import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase  # siempre incluye minúsculas
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    pasword = []
    if incluir_mayusculas:
        pasword.append(random.choice(string.ascii_uppercase))
    if incluir_numeros: 
        pasword.append(random.choice(string.digits))
    if incluir_simbolos:
        pasword.append(random.choice(string.punctuation))

    while len(pasword) < longitud:
        pasword.append(random.choice(caracteres))

    random.shuffle(pasword)
    return ''.join(pasword)