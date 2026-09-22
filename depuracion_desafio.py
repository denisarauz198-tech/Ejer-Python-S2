#Python 
# --- INICIO DEL CÓDIGO DE DESAFÍO --- 
# Bloque 1: Problema de Sintaxis 
def saludar(nombre) 
print("Bienvenido a la depuración, " + nombre + "!") 
print("Este programa tiene algunos errores, ¡encuéntralos!") 
# Bloque 2: Problema Lógico y Potencial Excepción 
def calcular_promedio(valores): 
total = 0 
# Queremos sumar todos los valores y luego dividir. 
# ¿Este bucle está sumando correctamente? 
for valor in valores: 
total = valor # Error lógico intencional 
# ¿Qué pasa si la lista está vacía? 
promedio = total / len(valores) 
return promedio 
# Bloque 3: Problemas de Excepción Comunes 
def procesar_datos_usuario(datos_str): 
try: 
# Intenta convertir la cadena a entero 
edad = int(datos_str["edad"]) # KeyError si 'edad' no existe, TypeError si datos_str no es 
dict 
# Simula una operación de archivo 
archivo = open("datos_sensibles.txt", "r") # FileNotFoundError si no existe 
linea = archivo.readline() 
print(f"Dato leído del archivo: {linea}") 
archivo.close() 
# Operación que puede fallar por tipo 
nombre_completo = datos_str["nombre"] + 10 # TypeError 
print(f"Usuario: {datos_str['nombre']}, Edad: {edad}") 
except Exception as e: # Una captura muy general, ¿es lo ideal? 
print(f"Se ha producido un error durante el procesamiento de datos: {e}") 
finally: 
print("Finalizando intento de procesamiento de datos.") 
# --- PRUEBAS DEL PROGRAMA --- 
print("--- Ejecutando Saludo ---") 
# ¿Cómo llamamos a la función saludar correctamente? 
# llamar_saludar("Depurador") 
print("\n--- Calculando Promedio ---") 
lista_numeros_1 = [10, 20, 30, 40] 
print(f"Promedio de {lista_numeros_1}: {calcular_promedio(lista_numeros_1)}") # ¿Qué 
resultado esperas? 
lista_numeros_2 = [] 
print(f"Promedio de {lista_numeros_2}: {calcular_promedio(lista_numeros_2)}") # ¿Qué pasará 
aquí? 
print("\n--- Procesando Datos de Usuario ---") 
# Caso 1: Datos válidos 
usuario_data_1 = {"nombre": "Alicia", "edad": "25"} 
procesar_datos_usuario(usuario_data_1) 
# Caso 2: Falta una clave 
usuario_data_2 = {"nombre": "Bob"} 
procesar_datos_usuario(usuario_data_2) 
# Caso 3: Tipo de datos incorrecto para una operación 
usuario_data_3 = "Carlos" # Debería ser un diccionario 
procesar_datos_usuario(usuario_data_3) 
# --- FIN DEL CÓDIGO DE DESAFÍO ---