nombre="mi_diario.txt"
opcion=input("Quiere ingresar una frase? ")
while opcion=="si":
    frase=input("Ingrese su frase: ")
    try:
        with open(nombre,"w+") as archivo:
            archivo.write(frase)
            print("Se guardo exictosamente su frase.\n")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")
    opcion=input("Quiere ingresar otra frase? ")
    if opcion!="si" or "s":
        break

leer=input("Quiere ver el contenido del diario? ")
if leer=="si" or "s":
    try:
        with open(nombre,"r") as archivo:
            contenido=archivo.read()
            print(f"\n Contenido del archivo: ")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo {nombre}.")
    except IOError as e:
        print(f"Error al leer el archivo {e}.")