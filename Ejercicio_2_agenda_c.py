# Importamos nuetro modulo Funciones_Proyecto
# Para validar datos con un alisa 'fp'.
import Funciones_Proyecto as fp

# Creamos la clase Nodo para contruir nuetro contacto
# en un nuevo nodo.
class Nodo:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direcion = direccion
        self.siguiente = None

# Clase Lista Enlazada.
# Aca cramos una lista enlazada formada por los nodos.
class ListaEnlazada:
    # Metodo constructor para una cabezera.
    def __init__(self):
        self.cabecera = None

    # Este es el metodo que se encarga de agregar contactos.
    def insertar_contacto(self, nombre, telefono, direccion):
        nuevo = Nodo(nombre, telefono, direccion)
        nuevo.siguiente = self.cabecera
        self.cabecera = nuevo

    # Este metodo se encarga de eliminar
    # un contacto en especifico.
    def eliminar(self, nombre):
        
        actual = self.cabecera
        anterior = None
        
        while actual and actual.nombre != nombre:
            anterior = actual
            actual = actual.siguiente
        
        # Si el contacto no existo lo notificamos.
        if not actual:
            print("ERROR: Contacto no encontrado!!!")
            return
        
        # De lo contrario realizamos la eliminacion.
        if anterior:
            anterior.siguiente = actual.siguiente
        
        else:
            self.cabecera = actual.siguiente
        
        print(f"Contacto '{nombre}' eliminado con éxito.")
    
    # Metodo para la busqueda de un contacto en especifico.
    def buscar(self, nombre):
        
        actual = self.cabecera
        
        # Durante tengamos valores buscaremos hasta
        # encontrar el contacto.
        while actual:
            
            if actual.nombre == nombre:
                print('Encontrado!!')
                print(f'Nombre: {actual.nombre}')
                print(f'Telefono: {actual.telefono}')
                print(f'Direccion: {actual.direcion}')
                return
            
            actual = actual.siguiente
        
        # Si no se encuentra lo notificamos.zSD
        print('ERROR:El contacto no se encuentra en agenda!!!')

    # Metodo que nos permite ver toda la agenda.
    def mostrar(self):
        
        actual = self.cabecera
        # Si hay contactos los imprime.
        if actual:
            print('=' * 65)
            print(f"{'Nombre':<20} | {'Teléfono':<15} | {'Dirección':<20}")
            print('=' * 65)
            
            # Recorrer la lista enlazada e imprimir cada fila
            while actual:
                print(f"{actual.nombre:<20} | {actual.telefono:<15} | {actual.direcion:<20}")
                actual = actual.siguiente
                    
            print('=' * 65)
        # De lo contrario nos notifica que la agenda esta vacia.
        else:
            print("La agenda se encuentra vacia por el momento!!!")

# Creamos nuetra lista enlazada en la variable agenda.
agenda = ListaEnlazada()

# creamos nuestro menu para el usuario.
def menu():
    while True:
        print('='*40)
        print('Agenda de contactos:')
        print('='*40)
        print('Opcione:')
        print('='*40)
        print('1. Agregar contacto.')
        print('2. Mostrar contactos.')
        print('3. Buscar contacto.')
        print('4. Eliminar contacto.')
        print('5. Salir.')
        print('='*40)
        
        # Preguntamos cual sera su opcion a elegir.
        opc = fp.valor_numerico('Ingese su opcion: ')
        print('='*40)
        
        # Con un match-case realizamos la nevegacion entre opciones
        # segun la que elija el usuario.
        match opc:
            
            # El case 1 se encarga de agregar los contactos
            case 1:
                nombre = fp.validar_nombre('Ingrese el nombre del nuevo contacto: ')
                numero_t = fp.validar_numero_t('Ingrese el numero de y telefono: ')
                direccion = fp.letras(f'Ingrese la direccion de {nombre}: ')
                
                agenda.insertar_contacto(nombre=nombre, telefono= numero_t, direccion= direccion)
                
                print('='*40)
                print('Agregado con exito a la agenda!!!')
                print('='*40)
                
                # Siempre le preguntamos al usuario si desea realizar otra accion.
                if fp.s_n('Desea realizar otra accion: ') != True:
                    break
            
            # El case 2 se encarga de mostrar toda la agenda.
            case 2:
                agenda.mostrar()
                if fp.s_n('Desea realizar otra accion: ') != True:
                    break
            
            # El case 3 realiza la busqueda de un contacto en especifico.
            case 3:
                nombre = fp.validar_nombre('Ingrese el nombre del contacto que desea: ')
                print('='*40)
                agenda.buscar(nombre= nombre)
                print('='*40)
                
                if fp.s_n('Desea realizar otra accion: ') != True:
                    break
            
            # El case 4 realiza la eliminacion de un contacto en especifico.
            case 4:
                nombre = fp.validar_nombre('Ingrese el nombre del contacto a eliminar: ')
                print('='*40)
                agenda.eliminar(nombre= nombre)
                print('='*40)
                if fp.s_n('Desea realizar otra accion: ') != True:
                    break
                
                # El case 5 cierra el programa por completo.
            case 5:
                exit()
                
                # Este case se encarga de desirle al usuario que no existe
                # la opcion que ingreso.
            case _:
                print(f'ERROR: Opcion {opc} no soportada!!!')
                print('='*40)
                if fp.s_n('Desea salir del programa: ') != True:
                    exit()
    
# Aca llamamos nuestro menu para interaccion del usuario.
if __name__ == '__main__':
    menu()