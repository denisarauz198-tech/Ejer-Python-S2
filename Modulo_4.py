# ============================================================================== 
# PLANTILLA MÓDULO 4: REPORTES Y MENÚ PRINCIPAL (Estudiante 4) 
# ============================================================================== 
# Inicialización de las estructuras de datos en memoria 
import Funciones_Proyecto as fp

import Modulo_1 as M1, Mudulo_2 as M2, Modulo_3 as M3

libros = [] 
usuarios = [] 
prestamos = [] 


def mostrar_libros_disponibles(libros,prestamos):
    if not libros:
        print("\nNo hay libros registrados actualmente.")
        return
    
    print('=====================================================')
    print('Libros disponibles:')
    hay_libros=False
    for libro in libros:
        if libro['estado'] == 'disponible' and libro not in prestamos:
            hay_libros=True
            print('=====================================================')
            for f,d in libro.items():
                print(f'_______________________________\n{f}:{d}')
    if hay_libros == False:
        print('No hay libros disponibles!!!')
    # TODO: Filtrar o recorrer los libros cuyo estado sea 'disponible' 
    # TODO: Si la lista resultante está vacía, imprimir mensaje informativo 
    # TODO: Si hay elementos, imprimir cada registro formateado en consola  

def mostrar_libros_prestados(prestamos): 
    if not prestamos:
        print("\nNo hay préstamos registrados actualmente.")
        return

    print("=== Reporte de Libros Prestados ===")
    for prestamo in prestamos:
        libro = next((l for l in libros if l["id"] == prestamo["id_libro"]), None)
        usuario = next((u for u in usuarios if u["id"] == prestamo["id_usuario"]), None)

        if libro and usuario:
            print(f"ID: {prestamo['id_prestamo']} | Título: {libro['titulo']} | Usuario: {usuario['nombre']} | Fecha: {prestamo['fecha']}")
        else:
            print(f"ID: {prestamo['id_prestamo']} | Datos incompletos (libro o usuario no encontrado)")



    # TODO: Verificar si hay préstamos en la lista. Si no hay, notificar al usuario. 
    # TODO: Iterar sobre cada préstamo y localizar el título del libro y el nombre del usuario. 
    # TODO: Imprimir el detalle del préstamo con ID, título, usuario y fecha. 

def menu_principal(): 
    """ 
    Objetivo: Desplegar el menú interactivo, capturar entradas del usuario y  
    coordinar la ejecución de las funciones de los demás módulos. 
    """ 
    
    while True: 
        print("\n=== SISTEMA DE BIBLIOTECA ESCOLAR ===") 
        print("1. Registrar libro") 
        print("2. Registrar usuario") 
        print("3. Prestar libro") 
        print("4. Ver libros disponibles") 
        print("5. Ver libros prestados") 
        print("6. Buscar libro")
        print("7. Buscar usuario")
        print("8. Salir")
        
        opcion = fp.valor_numerico("Seleccione una opción (1-8): ")
        
        if opcion == 1: 
            M1.registrar_libro(libros=libros,
                                    id_libro=fp.verificar_id_libros(libros=libros,mensaje='Ingrese el ID del libro: '),
                                    titulo=input('Ingrese el titulo del libro: '),
                                    autor=fp.validar_nombre('Ingrese el nombre del autor: '),
                                    anio=fp.validar_anio('Ingrese el año del libro: '))
            # TODO: Solicitar datos del libro (ID, título, autor, año) 
            # TODO: Invocar a la función registrar_libro con los argumentos correctos 
            
        elif opcion == 2: 
            M2.registrar_usuario(id_usuario=fp.verificar_id_usuario(usuarios=usuarios,
                                    mensaje='Ingrese el ID para el Usuario: '),
                                    nombre=fp.validar_nombre('Ingrese su nombre: '),
                                    grado=fp.validar_grado('Ingrese su grado: '),
                                    usuarios=usuarios)
            # TODO: Solicitar datos del usuario (ID, nombre, grado) 
            # TODO: Invocar a la función registrar_usuario con los argumentos correctos 
        
        elif opcion == 3:
            M3.prestar_libro(libros=libros, prestamos=prestamos, usuarios=usuarios,
                            id_libro=fp.verificar_id_libro_existencia(libros=libros, mensaje='Ingrese el ID del libro: '),
                            id_usuario=fp.verificar_id_usuario_existencia(usuarios=usuarios, mensaje='Ingrese el ID del usuario: '),
                            fecha=fp.validar_Fecha('Ingrese la fecha del prestamo realizado: '))
            # TODO: Solicitar ID del libro, ID del usuario y fecha 
            # TODO: Invocar a la función prestar_libro con los argumentos requeridos  
        
        elif opcion == 4: 
            mostrar_libros_disponibles(libros=libros,prestamos=prestamos)
            
        
        elif opcion == 5:
            mostrar_libros_prestados(prestamos=prestamos)
            # TODO: Invocar a la función mostrar_libros_prestados 
        
        elif opcion == 6:
            M1.buscar_libro_por_id(libros=libros, id_libro=fp.validar_id(objeto=libros, mensaje='Ingrese el ID del libro:'))
        
        elif opcion == 7:
            M2.buscar_usuario_por_id(usuarios=usuarios, id_usuario=fp.validar_id(objeto=usuarios, mensaje='Ingrese el ID del usuario: '))
        
        elif opcion == 8:
            print("Cerrando el sistema...")
            break 
        else: 
            print("Opción inválida. Intente de nuevo.") 
if __name__ == "__main__": 
    menu_principal()

