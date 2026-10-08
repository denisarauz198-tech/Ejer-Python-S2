class Pila:  
    def __init__(self): 
    # La pila vacía se representa con una lista vacía 
        self.items = [] 
    def apilar(self, x): 
        """Agrega el elemento x a la pila.""" 
        # Apilar es agregar al final de la lista 
        self.items.append(x) 
    def desapilar(self): 
        """Devuelve el elementuuuujjjjo tope y lo elimina de la pila. 
        Si la pila está vacía levanta una excepción.""" 
        try: 
            return self.items.pop() 
        except IndexError: 
            raise ValueError("La pila está vacía") 
    def es_vacia(self): 
        """Devuelve True si la pila está vacía, False si no.""" 
        return self.items == [] 
    def tope(self): 
        """Devuelve el elemento del tope sin eliminarlo.""" 
        if self.es_vacia(): 
            raise ValueError("La pila está vacía") 
        return self.items[-1] 
    def tamaño(self): 
        """Devuelve la cantidad de elementos en la pila.""" 
        return len(self.items)
def invertir_cadena(cadena): 
    """Invierte una cadena usando una pila.""" 
    p = Pila() 
    # Apilar cada carácter 
    for caracter in cadena: 
        p.apilar(caracter) 
# Desapilar para formar la cadena invertida 
    cadena_invertida = "" 
    while not p.es_vacia(): 
        cadena_invertida += p.desapilar() 
    return cadena_invertida 
# Prueba 
p = Pila()
print(p.es_vacia())
p.apilar(10)
p.apilar(20)
p.apilar(30)
print(p.tamaño())
print(invertir_cadena("Python"))  # nohtyP 
print(invertir_cadena("Hola"))    # aloH 