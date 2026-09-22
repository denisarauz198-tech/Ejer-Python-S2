import Módulo_analizador_texto as at, Funciones_Proyecto as fp, time as t

def menu_principal():
    while True:
        print("======Analizador de texto======")
        print("======Opciones======")
        print(" 1. Contar numero de palabras ")
        print(" 2. contar caracteres total y sin espacios ")
        print(" 3. Mostrar frecuencia de letras ")
        print(" 4. salir ")
        opcion=fp.valor_numerico("Elija una opcion del 1-4: ")
        print('====================================================')
        match opcion:
                case 1:
                    texto = fp.letras("Por favor ingresa el texto a analizar: ")
                    print('=============================================================')
                    print("Procesando, Contar numero de palabras...")
                    t.sleep(2)
                    n_palabras = at.contar_palabras(texto=texto)
                    print(f'Total de palabras: {n_palabras}')
                    print('============================================')
                    if fp.s_n('Desea volver al menu (S/N): ') != True:
                        break
                case 2:
                    texto = fp.letras("Por favor ingresa el texto a analizar: ")
                    print('=============================================================')
                    print("Procesando, Contar caracteres total y sin espacio...")
                    t.sleep(2)
                    dict_caracteres = at.contar_caracteres(texto=texto)
                    print('============================================')
                    for i,l in dict_caracteres.items():
                        print(f'{i}:{l}')
                        print('_______________________________')
                    print('============================================')
                    if fp.s_n('Desea volver al menu (S/N): ') != True:
                        break
                    
                case 3:
                    texto=fp.letras("Por favor ingresa el texto a analizar: ")
                    print('=============================================================')
                    print("Procesando, Mostrar frecuencia de letras ")
                    t.sleep(2)
                    l_frecuentes = at.frecuencia_letras(texto=texto)
                    for i,l in l_frecuentes.items():
                        print(f'{i}:{l}')
                        print('_______________________________')
                    print('============================================')
                    if fp.s_n('Desea volver al menu (S/N): ') != True:
                        break
                    
                case 4:
                    print('SALIENDO!!!')
                    t.sleep(2)
                    print("Gracias por usar el programa ")
                    break
                
                case _:
                    print("Error, debe seleccionar una opcion del 1-4: ")