from collections import deque as dq

class ColaFarmacia: 
    def __init__(self): 
        """Inicializa una cola vacía usando una lista.""" 
        self.items = dq()
    
    def agregar_paciente(self, nombre): 
        
        self.items.append(nombre) 
        print(f"Paciente '{nombre}' agregado a la cola.") 
    
    def atender_paciente(self): 
        """ 
        Atiende (elimina y devuelve) al primer paciente de la cola. 
        :return: Nombre del paciente atendido o mensaje si está vacía. 
        """ 
        if self.esta_vacia(): 
            print("No hay pacientes en la cola para atender.") 
            return None 
        paciente = self.items.popleft()  # Ojo: pop(0) es O(n) 
        print(f"Paciente '{paciente}' ha sido atendido.") 
        return paciente 
    
    def proximo_paciente(self): 
        """ 
        Devuelve el nombre del próximo paciente sin atenderlo. 
        :return: Nombre del paciente o mensaje si está vacía. 
        """ 
        if self.esta_vacia(): 
            print("No hay pacientes en la cola.") 
            return None 
        return self.items[0] 
    
    def esta_vacia(self): 
        """ 
        Verifica si la cola está vacía. 
        :return: True si está vacía, False en caso contrario. 
        """ 
        return len(self.items) == 0 
    
    def tamanio(self): 
        """ 
        Devuelve el número de pacientes en la cola. 
        :return: int, tamaño de la cola. 
        """ 
        return len(self.items) 
    
    def mostrar_cola(self): 
        """ 
        Muestra todos los pacientes en la cola, en orden de llegada. 
        """ 
        if self.esta_vacia(): 
            print("La cola está vacía.") 
        else: 
            print("Pacientes en la cola:", ", ".join(self.items)) 
    
    def __str__(self): 
        """ 
        Representación en cadena de la cola. 
        """ 
        return f"ColaFarmacia({self.items})"
    
pasientes = ColaFarmacia()

print(pasientes.esta_vacia())
pasientes.agregar_paciente('Eddy')
pasientes.agregar_paciente('Denis')
pasientes.agregar_paciente('Mario')
pasientes.agregar_paciente('Juan')
pasientes.atender_paciente()
print(pasientes.proximo_paciente())
print(pasientes.tamanio())
pasientes.mostrar_cola()
print(pasientes.esta_vacia())
