# Elaborado por: Denis Steve Arauz Orozco
# Carrera: Ingenieria en sistemas
# Grupo: #1

# Clase pila 
class Pila:
    """
    Clase que implementa una estructura de datos tipo Pila (LIFO).
    Métodos:
        apilar(x): agrega un elemento a la pila.
        desapilar(): elimina y retorna el último elemento.
        es_vacia(): verifica si la pila está vacía.
    """
    # Este es un metodo constructor(__init__ se ejecuta antes de hacer cualquier cosa en una prueba)
    def __init__(self):
        """Inicializa la pila vacía"""
        self.items = []

    def apilar(self, x):
        """Agrega un elemento a la pila"""
        self.items.append(x)

    def desapilar(self):
        """Quita y retorna el último elemento de la pila"""
        if self.es_vacia():
            raise ValueError("La pila está vacía, no se puede desapilar.")
        return self.items.pop()

    def es_vacia(self):
        """Verifica si la pila está vacía"""
        return self.items == []


def parentesis_balanceados(expresion):
    """
    Verifica si los paréntesis de una expresión están balanceados.
    Parámetro:
        expresion (str): cadena de texto con la expresión a evaluar
    Retorna:
        True si están balanceados, False si no
    """
    pila = Pila()

    for caracter in expresion:
        if caracter == "(":
            pila.apilar( x = caracter)  # si encuentra un parentesis de apertura lo apilamos
        elif caracter == ")":
            if pila.es_vacia():
                return False  # hay un cierre sin apertura, intento cerrar un parentesis sin abrir antes
            pila.desapilar()  # Elimina el ultimo "(" guardado indicando que ya encontro la pareja de ese parentesis

    # Si al final la pila está vacía, todo está balanceado, si no , devuelve False
    return pila.es_vacia()


# ============================
# PRUEBAS DE LA FUNCIÓN
# ============================

ejem = [
    "(a + b) * (c - d)",   # balanceado
    "((x + y) * z)",       # balanceado
    "((a + b)",            # falta un cierre
    "a + b) * c",          # cierre sin apertura
    "((())))"              # cierres extra
]

for i in ejem:
    print(f"Expresión: {i} = {parentesis_balanceados(i)}")

# Eleborado por: Denis Steve Arauz Orozco
# Fecha: 05/10/2026
# Actividad Independiente: Verificación de Paréntesis Balanceados con Pilas

# ============================
# EXPLICACIÓN DEL PROGRAMA
# ============================

#Resultados:
#1. (a + b) * (c - d) -> True
#   Cada apertura tiene su cierre correcto.

#2. ((x + y) * z) -> True
#   Los paréntesis están bien anidados y todos se cierran.

#3. ((a + b) -> False
#   Falta un paréntesis de cierre, la pila queda con un "(" pendiente.

#4. a + b) * c -> False
#   Hay un paréntesis de cierre sin que exista uno de apertura.

#5. ((()))) -> False
#   Hay más paréntesis de cierre que de apertura, la pila se vacía antes de tiempo.

