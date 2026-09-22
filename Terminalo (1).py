class ErroresPersonalisados(Exception):
    pass
#___________________________________________________________________________________________________________________________
from Funciones_Proyecto import letras, decimales, valor_numerico,texto_con_guiones
#___________________________________________________________________________________________________________________________
def validar_nombre(mensaje):
    intentos = 3
    while intentos > 0:
        try:
            nombre=letras(mensaje)
            if len (nombre) < 3 or len(nombre) > 50:
                intentos -= 1
                raise ErroresPersonalisados('el nombre debe tener entre 3 y 50 caracteres')
            else:
                return nombre.title()
        except ErroresPersonalisados as e:
            print(e)
            print(f'Intentos = {intentos} ')
    if intentos == 0:
        print('Intentos Insuficientes vuelva a empezar!!!')
        exit()
#___________________________________________________________________________________________________________________________
def validar_apellido(mensaje):
    intentos = 3
    while intentos > 0:
        try:
            apellido=letras(mensaje)
            if len(apellido) < 3 or len(apellido) > 35:
                intentos -= 1
                raise ErroresPersonalisados('El apellido debe tener entre 3 y 35 caracteres.')
            else:
                return apellido.title()
        except ErroresPersonalisados as e:
            print(e)
            print(f'Intentos = {intentos}')
    if intentos == 0:
        print('Intentos Insuficientes vuelva a empezar!!!')
        exit()
#___________________________________________________________________________________________________________________________
def validar_edad(mensaje):
    intentos = 3
    while intentos > 0:
        try:
            edad=valor_numerico(mensaje)
            if edad < 18 or edad > 60:
                intentos -= 1
                raise ErroresPersonalisados('La edad debe estar entre 18 y 60 años.')
            else:
                return edad
        except ErroresPersonalisados as e:
            print(e)
            print(f'Intentos = {intentos}')
    if intentos == 0:
        print('Intentos Insuficientes vuelva a empezar!!!')
        exit()
#___________________________________________________________________________________________________________________________
def validar_altura(mensaje):
    intentos = 3
    while intentos > 0:
        try:
            altura=decimales(mensaje)
            if altura < 1.50 or altura > 2.50:
                intentos -= 1
                raise ErroresPersonalisados('La altura debe estar entre 1.50 y 2.50 metros.')
            else:
                return altura
        except ErroresPersonalisados as e:
            print(e)
            print(f'Intentos = {intentos}')
        if intentos == 0:
            print('Intentos Insuficientes vuelva a empezar!!!')
            exit()
#___________________________________________________________________________________________________________________________
def validar_cedula(mensaje):
    intentos = 3 
    while intentos > 0:
        try:
            cedula=input(mensaje)
            if len(cedula) != 16 or cedula[3] != "-" or cedula[10] != "-":
                intentos -= 1
                raise ErroresPersonalisados('La cédula debe tener el formato ddd-dddddd-ddddL.')
            else:
                return cedula
        except ErroresPersonalisados as e:
            print(e)
            print(f'Intentos = {intentos}')
    if intentos == 0:
        print('Intentos Insuficientes vuelva a empezar!!!')
        exit()
#___________________________________________________________________________________________________________________________
def validar_telefono(mensaje):
    intentos = 3
    while intentos > 0:
        try:
            telefono=texto_con_guiones(mensaje)
            if len(telefono) != 9 or telefono[4] != '-':
                intentos -= 1
                raise ErroresPersonalisados('el telefono debe cumplir con el formato 0000-0000')
            else:
                return telefono
        except ErroresPersonalisados as e:
            print(e)
            print(f'Intentos = {intentos}')
    if intentos == 0:
        print('Intentos Insuficientes vuelva a empezar!!!')
        exit()
#___________________________________________________________________________________________________________________________
def main():
    personas_registradas=[]

    n = valor_numerico('ingrese la cantidad de personas a registrar:')

    for i in range(n):
        print("\nPersona", i + 1)
        nombre= validar_nombre(mensaje='Nombre: ')
        
        apellido= validar_apellido(mensaje='Apellido: ')

        edad= validar_edad(mensaje='Edad: ')

        altura = validar_altura(mensaje='Altura: ')

        cedula = validar_cedula(mensaje='Cedula: ')

        telefono = validar_telefono(mensaje='Telefono: ')
        
        persona={f'Nombre:': {nombre},
                'Apellido:': {apellido},
                'Edad:' :{edad},
                'Altura:': {altura},
                'Cedula:': {cedula},
                'Telefono:': {telefono}}
        personas_registradas.append(persona)
        print('Persona registrada con exito!!!')
        print()

    for e in personas_registradas:
        print('---Datos de la Persona---')
        for i,o in e.items():
            print(f"{i}{o}")
            print('________________________________________')
        print()

    print("Datos registrados correctamente.")
#___________________________________________________________________________________________________________________________
if __name__ == '__main__':
    main()