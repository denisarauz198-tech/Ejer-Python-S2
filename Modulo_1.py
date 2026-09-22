def registrar_libro(libros,id_libro, titulo, autor, anio):
    libro_nuevo = {"id": id_libro,
            "titulo": titulo,
            "autor": autor,
            "anio": anio,
            "estado": "disponible"}
    libros.append(libro_nuevo)
    print("¡Libro registrado éxitosamente!")
    return True
def buscar_libro_por_id(libros, id_libro):
    if id_libro == False:
        return
    encontrado=False
    for l in libros:
        if l["id"] == id_libro:
            encontrado = True
            print("¡Libro encontrado!\n\nImprimiendo información...\n ")
            for v,r in l.items():
                print(f"    {v.capitalize()}: {r}")
                print('|______________________________________|')
            return id_libro
    if not encontrado:
        print('Libro no encontrado!!!')