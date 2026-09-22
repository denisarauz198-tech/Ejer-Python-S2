matriz=[
	[85,90,78],
	[92,88,95]
	]
n_estu = 0
for i in matriz:
    n_estu += 1
    print(f"Estudiante {n_estu}:")
    for l in i:
        print(l,end=" ")
    print("\n")