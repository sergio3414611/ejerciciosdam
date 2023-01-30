# EJERCICIO 2
print("EJERCICIO 2")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("Las asignaturas del curso son:")
for asignatura in asignaturas:
    print("- " + asignatura)

# EJERCICIO 3
print("\nEJERCICIO 3")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for asignatura in asignaturas:
    print("Yo estudio " + asignatura)

# EJERCICIO 4
print("\nEJERCICIO 4")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] * 3

asignaturas_set = set(asignaturas)

asignatura = input("Introduce una asignatura: ")

if asignatura in asignaturas_set:
    print("Sí, está en el set de asignaturas.")
else:
    print("No, no está en el set de asignaturas.")

# EJERCICIO 5
print("\nEJERCICIO 5")
numeros = [1, 2, 3]
cadenas = ["hola", "mundo"]

numeros.append(13)
cadenas.append("El perro de Juan Vicente come pienso")

print(numeros)
print(cadenas)

# EJERCICIO 6
"""En python se puede usar el método difference de un objetoset para obtener los 
elementos que están en el primer set y no están en el segundo set"""

print("\nEJERCICIO 6")
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

diferencia = a.difference(b)

print(diferencia)

# EJERCICIO 7
print("\nEJERCICIO 7")
cuadrado = [n**2 for n in range(1,6)]
print(cuadrado)
