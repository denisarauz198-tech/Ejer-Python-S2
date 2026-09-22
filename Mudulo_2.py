# Definición de la función para registrar un nuevo usuario
def registrar_usuario(usuarios, id_usuario, nombre, grado):
    # Crea un diccionario con los datos del nuevo usuario (id, nombre y grado)
    nuevo_usuario={'id': id_usuario, 'nombre': nombre, 'grado': grado}
    # Añade el nuevo usuario a la lista de usuarios
    usuarios.append(nuevo_usuario)
    print('Usuario registrado con exito!!!')

# Definición de la función para buscar un usuario por su ID
def buscar_usuario_por_id(usuarios, id_usuario):
    if id_usuario == False:
        return
    # Recorre cada usuario en la lista de usuarios
    for usuario in usuarios:
        # Verifica si el ID del usuario actual coincide con el ID que se busca
        if usuario ['id']== id_usuario:
            print('Usuario encontrado con exito!!!\n')
            # Si encuentra coincidencia, retorna el diccionario del usuario
            for i,l in usuario.items():
                print(f'     {i}:{l}')
                print('|_____________________________________|')
            break
        if usuario['id'] != id_usuario:
            continue
    # Si no encuentra el usuario después de recorrer toda la lista, lanza un (error)
    else:
        print("Error, Usuario no existe")