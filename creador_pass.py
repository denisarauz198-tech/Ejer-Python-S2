import Modulogenerador as mg, Funciones_Proyecto as fp
def main():
    while True:
        try:
            longitud=fp.valor_numerico("Ingrese su longitud deseada para su contraseña: ")
            if longitud <= 2 or longitud >= 21:
                raise ValueError("ERROR: La longitud debe estar entre 3 y 20!!!")
            
            incluir_mayusculas=fp.s_n("Desea incluir mayusculas? (S/N): ")
            incluir_numeros=fp.s_n("Desea incluir  numeros? (S/N): ")
            incluir_simbolos=fp.s_n("Desea incluir simbolos? (S/N): ")
            
            pasword=mg.generar_contraseña(incluir_mayusculas= incluir_mayusculas,
                                        incluir_numeros= incluir_numeros,
                                        incluir_simbolos= incluir_simbolos,
                                        longitud=longitud)
            print(pasword)
            if fp.s_n('Desea crear otro pasword: ') != True:
                break
            
        except ValueError as ve:
            print(f" Error: {ve}")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")

if __name__== "__main__":
    main()