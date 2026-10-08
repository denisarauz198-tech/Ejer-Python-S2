import Funciones_Proyecto as fp
import Nodos as nd, time as tm
lista = nd.ListaEnlazada()
def menus():
    # Menu 1
    menu_2 = False
    
    while True:
        
        print('='*40)
        print('Menu Principal')
        print('='*40)
        print('Operaciones:')
        print('='*40)
        print('1. Incertar nodo al inicio.')
        print('2. Incertar nodo al final.')
        print('3. Ver si existe un nodo.')
        print('4. Mostrar los nodos.')
        print('5. Eliminar un nodo.')
        print('6. Borrar los nodos.')
        print('7. Salir.')
        print('='*40)
        
        operacion = fp.valor_numerico('Ingrese la operacion que desea realizar: ')
        match operacion:
            
            case 1:
                nodo = fp.valor_numerico('Ingrese el nuevo nodo: ')
                lista.insertar_inicio(valor= nodo)
                print('='*40)
                print('Insertado al inicio con Exito!!!')
                print('='*40)
                
                if fp.s_n('Desea realizar otra operaion: ') != True:
                    break
                else:
                    continue
                
                
            case 2:
                nodo = fp.valor_numerico('Ingrese el nuevo nodo: ')
                lista.insertar_final(valor= nodo)
                print('='*40)
                print('Insertado con Exito!!!')
                print('='*40)
                
                if fp.s_n('Desea realizar otra operaion: ') != True:
                    break
                else:
                    continue
                
            case 3:
                nodo = fp.valor_numerico('Ingrese el valor del nodo a verificar: ')
                print('='*40)
                print('Buscando...')
                tm.sleep(2)
                print(f'Existencia: {lista.buscar(valor= nodo)}')
                print('='*40)
                
                if fp.s_n('Desea realizar otra operaion: ') != True:
                    break
                else:
                    continue
                
            case 4:
                print('='*40)
                print('=============Nodos==============')
                lista.mostrar()
                print('='*40)
                
                if fp.s_n('Desea realizar otra operaion: ') != True:
                    break
                else:
                    continue
                
            case 5:
                nodo = fp.valor_numerico('Ingrese el nuevo nodo: ')
                lista.eliminar(valor= nodo)
                print('='*40)
                print('Eliminado con Exito!!!')
                print('='*40)
                
                if fp.s_n('Desea realizar otra operaion: ') != True:
                    break
                else:
                    continue
                
            case 6:
                lista.BorrarElementos()
                print('Nodos borrados con exito!!!')
                
                if fp.s_n('Desea realizar otra operaion: ') != True:
                    break
                else:
                    continue
                
            case 7:
                exit()
                
            case _:
                print(f'ERROR: La operacion {operacion} no es reconocida!!!')
                if fp.s_n('Desea Cerrrar el prgrama: ') == True:
                    break
                else:
                    continue
                
    menu_2 = fp.s_n('Desea segir al siguiente menu: ')
    while menu_2:
        # Menu 2
        print('='*40)
        print('Operaciones Disponibles para los nodos!!')
        print('='*40)
        print('1. Sumar nodos.')
        print('2. Restar nodos.')
        print('3. Obtener el nodo mas grande.')
        print('4. Obtener el nodo mas pequeño.')
        print('5. Obtener el promedio de los nodos.')
        print('6. Obtener los nodos Pares.')
        print('7. Obtener los nodos impares.')
        print('8. Salir')
        print('='*40)
        
        proc = fp.valor_numerico('Ingrese el Proceso que desea: ')
        print('='*40)
        if proc == 6:
            lista.pares_impares(opc='pares')
            print('='*40)
            
        elif proc == 7:
                    lista.pares_impares(opc='impares')
                    print('='*40)
        
        else:
            try:
                print(f'Resultado del proceso {proc}: {lista.procesar_nodos(operacion= proc)}')
                print('='*40)
            except ValueError as e:
                print(e)
        menu_2 = fp.s_n('Desea realizar otra operacion: ')

menus()