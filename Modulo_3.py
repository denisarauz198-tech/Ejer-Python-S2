def prestar_libro(libros,usuarios,prestamos,id_libro,id_usuario,fecha):
    acces=False
    while acces == False:
        for i in libros:
            if i["id"]==id_libro:
                print("Libro Encontrado")
                if i["estado"]=="disponible":
                    print("Libro disponible")
                    acces=True
                    break
                elif i["estado"]=="prestado":
                    print("Error! el libro se encuentra prestado")
                    return False
    if acces ==True:
        for i in usuarios:
                if i["id"]== id_usuario:
                    print("\n")
                    long=(len(prestamos))+1
                    prestamo={"id_prestamo":long,
                            "id_libro":id_libro,
                            "id_usuario":id_usuario,
                            "fecha":fecha}
                    for libro in libros:
                        if libro["id"] ==  id_libro:
                            if libro["estado"]=="disponible":
                                libro["estado"]="prestado"
                    prestamos.append(prestamo)
                    print("Prestamo del libro con exito")
