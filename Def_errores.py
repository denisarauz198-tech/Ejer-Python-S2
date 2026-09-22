# Ejercicio 1:

# se corrigio el error de los dos puntos al final
def calcular_area_circulo(radio): 
    # Error de sintaxis
    # Se agrego un (;) para la declaracion de (area).
    pi=3.14159 ; area = pi * (radio**2)
    print(f'El area del circulo es: {area}')

# Error logico
# Se corrigio el error de llamar la funcion dentro del bloque (def)
calcular_area_circulo(10)

# Ejercicio 2:

def presentar_usuario(nombre,ciudad):
    print(f'Hola, {nombre}, :Que bueno que nos visites desde {ciudad}!')

# Error de sintaxis y logico
# Se corrigio el error de llamar la funcion dentro del bloque (def)
# Se corrigio el error logico al no pasar todos los argumentos
presentar_usuario('Denis','Corn Island')

# Ejercicio 3:

def registrar_producto(nombre,stock,codigo_barras):
    print(f'''Registrando: {nombre}
    codigo = {codigo_barras}
    stock_inicial: {stock}''')
    
registrar_producto('Laptop Gamer', 0 , codigo_barras='12345678')