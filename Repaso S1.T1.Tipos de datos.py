producto=["Melon", "sandia"]

precio=[9.75, 20.50]

for i in range(len(producto)):
    if precio[i] > 10:
        descuento=True
    else:
        descuento=False
    print(f"Producto:{producto[i]} Decuento: {descuento}")