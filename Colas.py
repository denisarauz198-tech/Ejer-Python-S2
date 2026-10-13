class Cola: 
    """ Representa a una cola, con operaciones de encolar y 
    desencolar. El primero en ser encolado es también el primero 
    en ser desencolado. """ 
    def __init__(self): 
        #Crea una cola vacía. 
        # La cola vacía se representa por una lista vacía 
        self.items=[] 
    
    #El método encolar se implementará agregando el nuevo elemento al final de la lista: 
    def encolar(self, x): 
        #Agrega el elemento x como último de la cola. 
        self.items.append(x) 
    
    """Para implementar desencolar, se eliminará el primer elemento de la lista y se devolverá 
    el valor del elemento eliminado, utilizaremos nuevamente el método pop, pero en este caso le 
    pasaremos la posición 0, para que elimine el primer elemento, no el último. Si la cola está vacía 
    se levantará una excepción.""" 
    def desencolar(self): 
        #Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, lanza ValueError. 
        try: 
            return self.items.pop(0) 
        except: 
            raise ValueError("La cola está vacía") 
    
    #Por último, el método es_vacia, que indicará si la cola está o no vacía. 
    def es_vacia(self): 
        #Devuelve True si la cola está vacía, False si no. 
        return self.items == [] 
    
q = Cola() 
print(q.es_vacia()) 
q.encolar(1) 
q.encolar(2) 
q.encolar(5) 
print(q.es_vacia()) 
print(q.desencolar()) 
q.encolar(8) 
print(q.desencolar()) 
print(q.desencolar()) 
print(q.es_vacia()) 
print(q.desencolar())