def saludar(nombre):
    print("Hola, " + nombre)
    nombre_usuario = input("Introduce tu nombre: ")
    if nombre_usuario != "":
        saludar(nombre_usuario)
    else:
        print("No has introducido un nombre")
    print("Gracias por usar nuestro programa")
    print("Hasta pronto")
nombre=input('Ingrese su nombre:')
saludar(nombre)