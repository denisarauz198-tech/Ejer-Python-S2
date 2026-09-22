#Problema: CALCULAR PROMEDIO Y ESTADO
#(>=60, Aprobado, <60, Reprobado)
#Funciones modulares
def solicitar_notas():
    n1=float(input("Ingrese la nota 1: "))
    n2=float(input("Ingrese la nota 2: "))
    n3=float(input("Ingrese la nota 3: "))
    return n1,n2,n3

def calcular_promedio(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    return promedio

def determinar_aprobacion(promedio):
    if promedio>=60:
        return "Aprobado"
    else:
        return "Reprobado"
    
#PROGRAMA PRINCIPAL
def main():
    print(" Sistema de calificaciones")
    nota1,nota2,nota3=solicitar_notas()
    prom=calcular_promedio(nota1,nota2,nota3)
    estado=determinar_aprobacion(prom)
    print(f"promedio final: {prom:.2f}")
    print(f"Estado del estudiante: {estado}")
if __name__ == "__main__":
    main()