import math
def leer_entero_seguro(mensaje):
	while True:
		entrada=input(mensaje)
		try:
			valor=int(entrada)
			return valor
		except ValueError:
			print("Error: Debe ingresar un numero entero valido")
#uso de la funcion
edad=leer_entero_seguro('ingrese su edad: ')
print(f'Edad registrada {edad}')

def calcular_raiz_cuadrada():
    try:
        numero=float(input('Ingrese un numero positivo: '))
        if numero < 0:
            raise ValueError('No se puede calcular la raiz cuadrada de un numero negativo!!!')
        resultado=math.sqrt(numero)
    except ValueError as error:
        print(f'Error capturado:{error}')
    else:
        print(f'La raiz cuadrada es {resultado: .2f}')
#llamada de la funcion
calcular_raiz_cuadrada()