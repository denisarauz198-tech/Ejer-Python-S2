estudiantes=[
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

calificaciones_max=max(estudiantes, key=lambda x: x ["Calificacion"])
nombre_max=max(estudiantes, key=lambda x: x ["Calificacion"])["Nombre"]
calificaciones_min=min (estudiantes, key=lambda x: x ["Calificacion"])
nombre_min=min(estudiantes, key=lambda x: x ["Calificacion"])["Nombre"]

Reprobados=0
Aprobados=0
total=0

for g in estudiantes:
    total+=g["Calificacion"]
    if g["Calificacion"] >=60:
        Aprobados+=1
    else:
        Reprobados+=1
promedio=total/10
print(f'''La estudiante {nombre_max} tiene la nota mas alta con: {calificaciones_max["Calificacion"]} \n
El estudiante {nombre_min} tiene la nota mas baja con: {calificaciones_min["Calificacion"]}''')

print(f'''El promedio general de la clase es de: {promedio}\n
El total de estudiantes aprobados es de: {Aprobados}\n
El total de estudiantes reprobados es de: {Reprobados}\n''')