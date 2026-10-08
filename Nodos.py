import Funciones_Proyecto as fp
import numpy as np

#  Clases para la estructura de un nodo y una lista  enlazada
# Clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase Lista Enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabecera = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabecera
        self.cabecera = nuevo

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabecera:
            self.cabecera = nuevo
            return
        actual = self.cabecera
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def eliminar(self, valor):
        actual = self.cabecera
        anterior = None
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        if not actual:
            print("Valor no encontrado")
            return
        if anterior:
            anterior.siguiente = actual.siguiente
        else:
            self.cabecera = actual.siguiente
    
    def BorrarElementos(self): 
        actual = self.cabecera 
        while (actual): 
            self.cabecera = actual.siguiente
            del actual 
            actual = self.cabecera

    def buscar(self, valor):
        actual = self.cabecera
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.cabecera
        while actual:
            print(actual.valor, end="  ->  ")
            actual = actual.siguiente
        print("None")
        
    def pares_impares(self,opc):
        actual=self.cabecera
        impares=[]
        pares=[]
        while actual:
            if actual.valor %2==0:
                pares.append(actual.valor)
                actual=actual.siguiente
            else:
                impares.append(actual.valor)
                actual=actual.siguiente
        print()
        if opc =="pares":
            print("Pares:")
            for i in pares:
                print(i, end=" ")
            print()
        else:
            print(f"Impares:")
            for e in impares:
                print(e, end=" ")
            print()
        return
        
    def procesar_nodos(self, operacion):
        actual = self.cabecera
        valores = []
        
        # 1. Extraemos todos los valores a una lista de Python
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
            
        # Si la lista está vacía, evitamos errores al calcular max/min
        if not valores:
            return None
        
        # 2. Elegimos la operación según el parámetro
        if operacion == 1:
            return sum(valores)
        
        elif operacion == 2:
            resultado = valores[0]
            for valor in valores[1:]:
                resultado -= valor
            return resultado
            
        
        elif operacion == 3:
            return max(valores)
        
        elif operacion == 4:
            return min(valores)
        
        elif operacion == 5:
            
            return np.mean(valores)
        
        elif operacion == 8:
            self.pares_impares(opc='pares')
        
        else:
            raise ValueError(f"Operación '{operacion}' no soportada")
        
