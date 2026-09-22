def decimales(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print('ERROR: Debe ingresar un numero!!!')
#___________________________________________________________________________________________________________________________
def valor_numerico(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('ERROR: Debe ingresar un numero entero!!!')
#___________________________________________________________________________________________________________________________
def letras(mensaje):
    while True:
        entrada=input(mensaje).strip()
        
        if all(c.isalpha() or c.isspace()for c in entrada) and entrada!='':
            return entrada.title()
        else:
            print('Error: No puede contener numeros ni estar vacio.')
#___________________________________________________________________________________________________________________________
def texto_con_guiones(mensaje):
    while True:
        entrada=input(mensaje).strip()
        
        if all(c.isdigit() or c=='-' for c in entrada) and entrada !='':
            return entrada
        else:
            print('ERROR: Solo se aceptan numeros y guiones!!!')
#___________________________________________________________________________________________________________________________
def validar_Fecha(mensaje):
    while True:
        Fecha=texto_con_guiones(mensaje)
        if len(Fecha) != 10 or Fecha[2] != '-' or Fecha[5] != '-' or Fecha == '':
            print('La fecha debe cumplir con el formato dd-mm-aaaa y no puede estar vacio!!!')
        else:
            return Fecha
#___________________________________________________________________________________________________________________________
def validar_anio(mensaje):
    while True:
        anio=valor_numerico(mensaje)
        if anio>=1600 and anio<=2026:
            return anio
        else:
            print('El año no es valido o no esta en el rango establecido!!!')
#___________________________________________________________________________________________________________________________
def verificar_id_libros(libros,mensaje):
    while True:
        id_libro=input(mensaje)
        if all(c.isdigit() for c in id_libro) and id_libro != '':
            existe= any(l["id"] == id_libro for l in libros)        
            if existe:
                print("¡Error: El ID del libro que está tratando de registrar ya se encuentra asignado!")
                continue
            else:
                return id_libro
        else:
            print('Error: Solo se aceptan numeros para el ID y no puede estar vacio!!!')
#___________________________________________________________________________________________________________________________
def verificar_id_usuario(usuarios,mensaje):
    while True:
        id_usuario=validar_id(objeto=usuarios, mensaje=mensaje)
        if  all(c.isdigit() for c in id_usuario) and id_usuario != '':
            existe= any(usuario['id']==id_usuario for usuario in usuarios)
        
            if existe:
                print("¡Error: El ID de usuario que está tratando de registrar ya se encuentra asignado!")
            else:
                return id_usuario
        else:
            print('Solo se aceptan numeros para el ID y no puede estar vacio!!!')
#___________________________________________________________________________________________________________________________
def validar_nombre(mensaje):
    while True:
            nombre=letras(mensaje)
            if len (nombre) < 3 or len(nombre) > 50:
                print('El nombre debe tener entre 3 y 50 caracteres')
            else:
                return nombre.title()
#___________________________________________________________________________________________________________________________
def validar_grado(mensaje):
    while True:
        grado=input(mensaje).lower()
        partes = grado.split()
        if len(partes) == 2:
            numero, palabra = partes
            if numero.isdigit and palabra == 'grado':
                return grado
            else:
                print('Error: el grado debe comenzar con números y terminar con la palabra grado !!!')
        else:
            print('Error: el grado debe cumplir con el formato NN grado !!!')
#___________________________________________________________________________________________________________________________
def validar_id(mensaje, objeto):
    if objeto:
        while True:
            id=input(mensaje)
            if len(id) == 3 and all(c.isdigit for c in id):
                return id
            else:
                print('El ID debe cumplir con el formato NNN')
    else:
        print('\nNo hay registros por el momento!!!')
        return False
#___________________________________________________________________________________________________________________________
def verificar_id_usuario_existencia(usuarios,mensaje):
    while True:
        id_usuario=input(mensaje)
        if all(c.isdigit() for c in id_usuario) and id_usuario != '':
            existe= any(usuario['id']==id_usuario for usuario in usuarios)
        
            if existe:
                return id_usuario
            else:
                print('El ID no esta registrado')
        else:
            print('Solo se aceptan numeros para el ID y no puede estar vacio!!!')
#___________________________________________________________________________________________________________________________
def verificar_id_libro_existencia(libros,mensaje):
    while True:
        id_libro=input(mensaje)
        if all(c.isdigit() for c in id_libro) and id_libro != '':
            existe= any(libro['id']==id_libro for libro in libros)
        
            if existe:
                return id_libro
            else:
                print('El ID no esta registrado')
        else:
            print('Solo se aceptan numeros para el ID y no puede estar vacio!!!')
#___________________________________________________________________________________________________________________________
def s_n(mensaje):
    while True:
        res=input(mensaje).lower()
        if res == 's' or res == 'n':
            if res == 's':
                return True
            if res == 'n':
                return False
        else:
            print('ERROR: Solo se acepta S o N como respuesta!!!')
#___________________________________________________________________________________________________________________________
