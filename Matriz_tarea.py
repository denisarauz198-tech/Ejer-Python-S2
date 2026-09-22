matriz=[
	[85,90,78],
	[92,88,95]
	]
cont = 0
for i in matriz:
    cont += 1
    print(f"Estudiante {cont}:")
    for l in i:
        print(l,end=" ")
    print("\n")