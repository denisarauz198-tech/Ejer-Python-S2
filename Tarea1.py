from Funciones_Proyecto import decimales, valor_numerico
#__________________________________________________________________________________________
def CelsiusFahrenheit(celsius):
    Fah_T=(celsius*1.8)+32
    return Fah_T
#__________________________________________________________________________________________
def FahrenheitCelsius(fahrenheit):
    cel_t=(fahrenheit-32)*5/9
    return  cel_t
#__________________________________________________________________________________________
def main():
    while True:
        print("Conversor de fahrenheit/Celsius \n")
        print("---Menu de opciones---\n" \
        "1-Convertir de Celsius a Fahrenheit \n" \
        "2-Convertir de Fahrenheit a Celsius\n" \
        "3-Salir\n")
        opcion=valor_numerico("Elija su opcion 1/3: ")
        match opcion:
            case 1:
                cel=decimales("Cantidad de grados Celsius: ")
                total=CelsiusFahrenheit(cel)
                print(f"De {cel} Celsius se convierten a {total} grados fahrenheit")
            case 2:
                fah=decimales("Cantidad de grados fahrenheit\n: ")
                tot=FahrenheitCelsius(fah)
                print(f"De {fah} fahrenheit se convierten a ={tot} grados Celsius\n")
            case 3:
                print("----Saliendo del programa ...---\n")
                break
            case _:
                print("Opcion NO VALIDA (1/3)")
#__________________________________________________________________________________________
if __name__ == "__main__":
    main()