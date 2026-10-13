from collections import deque 
    
class ColaEficiente: 
    def __init__(self): 
        self.items = deque()  # Mucho más rápido 
    
    def encolar(self, item): 
        self.items.append(item) 
    
    def desencolar(self): 
        if self.esta_vacia(): 
            raise IndexError("Cola vacía") 
        return self.items.popleft()  # O(1) 
    
    def frente(self): 
        if self.esta_vacia(): 
            raise IndexError("Cola vacía") 
        return self.items[0] 
    
    def esta_vacia(self): 
        return len(self.items) == 0 
    
    def tamano(self): 
        return len(self.items) 
    
    def __str__(self): 
        return f"Cola: {list(self.items)}"