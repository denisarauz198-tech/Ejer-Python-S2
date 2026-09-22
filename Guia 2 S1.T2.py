estudiantes_programacion = {"ernesto", "antonio", "carlos", "mariano"}
estudiantes_diseño = {"pedro", "ernesto", "francisco", "luciano"}
ambas_clases = estudiantes_programacion.intersection(estudiantes_diseño)
print("Estudiantes en ambas clases:",ambas_clases)
una_clase = estudiantes_programacion.union(estudiantes_diseño)
print("Estudiantes en al menos una clase:",una_clase)
solo_programacion = estudiantes_programacion.difference(estudiantes_diseño)
print("Estudiantes solo en programación:",solo_programacion)