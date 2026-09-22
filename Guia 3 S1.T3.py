print('-----Mi Diario-----')
print('-------------------------------------------------')
c_frase=int(input('Ingrese la cantidad de frases que quiere agregar: '))
l_frases=[]
for i in range(c_frase):
    n_frase=input('Dime cual es tu frase: ').strip()
    l_frases.append(n_frase)
try:
    with open('mi_diario.txt','a') as archivo:
        for frase in l_frases:
            archivo.write(f'{frase} \n')
except IOError:
    print('Error! Algo salio mal!!!!')

mostrar=input('Deseas ver el diario (SI/NO): ').lower().strip()
if mostrar=='si':
    with open('mi_diario.txt','r') as arch:
        frases_t=arch.readlines()
        for j in frases_t:
            print(j)
else:
    print('Grasias por usar el programa!!!')