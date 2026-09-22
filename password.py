class ErroresPersonalizados(Exception):
    pass
errores=[]
#______________________________________________________________________________________________________
def validar_password(password):

    if len(password) < 8:
        errores.append("Error de password: debe tener al menos 8 caracteres")

    if not any(c.islower() for c in password):
        errores.append("Error de password: debe contener al menos una letra minúscula")

    if not any(c.isupper() for c in password):
        errores.append("Error de password: debe contener al menos una letra mayúscula")

    if not any(c.isdigit() for c in password):
        errores.append("Error de password: debe contener al menos un número")

    caracteres_especiales = "!@#$%^&*"
    if not any(c in caracteres_especiales for c in password):
        errores.append("Error de password: debe contener al menos un carácter especial")
    if errores:
        raise ErroresPersonalizados("\n"+'\n'.join(errores))

    return True
#______________________________________________________________________________________________________
def main():
    try:
        validar_password(input('Ingrese su Password: '))
        print("Contrasenna válida")
    except ErroresPersonalizados as e:
        print(e)
#______________________________________________________________________________________________________
if __name__ == '__main__':
    main()