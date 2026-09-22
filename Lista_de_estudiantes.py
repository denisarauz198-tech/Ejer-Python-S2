est = [
    {"Nombre": "Carlos", "Calificacion": 70},
    {"Nombre": "Roberto", "Calificacion": 72},
    {"Nombre": "Mario", "Calificacion": 65},
    {"Nombre": "Emanuel", "Calificacion": 60},
    {"Nombre": "Fanny", "Calificacion": 100},
    {"Nombre": "Steve", "Calificacion": 90},
    {"Nombre": "Pepe", "Calificacion": 71},
    {"Nombre": "Edy", "Calificacion": 95},
    {"Nombre": "Rosa", "Calificacion": 68},
    {"Nombre": "Gabriel", "Calificacion": 37}
    ]

calificaciones_max = max(est, key=lambda x: x ["Calificacion"])
nombre_max = max(est, key=lambda x: x ["Calificacion"])["Nombre"]
calificaciones_min = min (est, key=lambda x: x ["Calificacion"])
nombre_min = min(est, key=lambda x: x ["Calificacion"])["Nombre"]

total = 0
apro = 0
rpro = 0

for f in est:
    total += f["Calificacion"]
    if f["Calificacion"] >= 60:
        apro += 1
    else:
        rpro += 1

promedio = total / len(est)

print(f'''La estudiante {nombre_max} tiene la nota mas alta con: {calificaciones_max["Calificacion"]} \n
El estudiante {nombre_min} tiene la nota mas baja con: {calificaciones_min["Calificacion"]}''')

print(f'''El promedio general de la clase es de: {promedio}\n
El total de est aprobados es de: {apro}\n
El total de est reprobados es de: {rpro}\n''')