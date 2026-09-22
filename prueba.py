producto="Manzana"

precio= 19.50

hay_descuento=True

print(f'''Producto:{producto}, Tipo de dato:{type(producto)}
Precio: {precio}, Tipo de dato:{type(precio)}
Descuento:{hay_descuento}, Tipo de dato:{type(hay_descuento)}''')

a= 50

b= 70

print(a > b)
print(a != b)

es_mayor_edad = True
tiene_permiso= False

# El print nos devolvera un False ya que el operador logico "and" compara los valores de cada variable
# si ambas se cumplen sera True pero si almenos una es False el resultado es False aunque uno sea True.

print(es_mayor_edad and tiene_permiso)

print(not(10 >5 and 20 < 15))