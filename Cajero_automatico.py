#fuciones de operaciones
def mostrar_menu():
    print("\n ---CajeroAutomatico---")
    print("1-Consular Saldo")
    print("2-Depositar Dinero")
    print("3-Retirar Dinero")
    print("4-Salir")
#__________________________________________________________________________________
def Depositar(Saldo_Actual):
    monto=float(input("Ingrese el monto: "))
    if monto>0:
        nuevo_saldo=Saldo_Actual+monto
        print(f"Deposito exitoso. Nuevo saldo:$ {nuevo_saldo}.")
        return nuevo_saldo
    else:
        print("El monto debe ser psoitivo.")
        return Saldo_Actual
#__________________________________________________________________________________
def retiro(Saldo_Actual):
    monto=float(input("Ingrese el monto a retirar:$ "))
    if monto<=0:
        print("Monto invalido")
        return Saldo_Actual
    elif monto <= Saldo_Actual:
        nuevo_saldo=Saldo_Actual-monto
        print("Retiro exitoso")
        return nuevo_saldo
    else:
        print("Fondos insuficientes")
        return Saldo_Actual
#__________________________________________________________________________________
def main():
    saldo=500
    opcion=""
    while opcion!="4":
        mostrar_menu()
        opcion=input("Seleccione una opcion 1-4: ")
        if opcion =="1":
            print(f"Saldo actual es :$ {saldo:.2f}")
        elif opcion=="2":
            saldo=Depositar(saldo)
        elif opcion=="3":
            saldo=retiro(saldo)
        elif opcion=="4":
            print("gracias por usar nuestros servicios")
        else:
            print("Opcion No Valida")
#__________________________________________________________________________________
if __name__ == "__main__":
    main()