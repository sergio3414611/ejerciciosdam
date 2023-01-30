# EJERCICIO 1
nombre = "Juan Perez"
balance = 53.44

cadena_formateada = "Hola %s. Tu balance es %.2f$" % (nombre, balance)
print(cadena_formateada)

# EJERCICIO 2
a_float = float("3.14")
print("Conversion a float:", a_float)
print("Tipo:", type(a_float))

a_int = int(a_float)
print("\nConversion a int:", a_int)
print("Tipo:", type(a_int))

a_bool = bool(a_int)
print("\nConversion a bool:", a_bool)
print("Tipo:", type(a_bool))

a_string = str(a_float)
print("\nConversion a string:", a_string)
print("Tipo:", type(a_string))

# EJERCICIO 3
import sys
a_int = 300120023
a_string = "Eso no es muy Pythonico de tu parte"
a_float = 7.896

print("Longitud de int:", sys.getsizeof(a_int))
print("Longitud de string:", sys.getsizeof(a_string))
print("Longitud de float:", sys.getsizeof(a_float))


# EJERCICIO 4
texto = "El perro de Juan Vicente come pienso"

# strip
print("\nstrip:", texto.strip())

# split
palabras = texto.strip().split(" ")
print("\nsplit:", palabras)

# lower
print("\nlower:", texto.strip().lower())

# upper
print("\nupper:", texto.strip().upper())

# find
posicion = texto.strip().find("texto")
print("\nfind:", posicion)

# index
posicion = texto.strip().index("texto")
print("\nindex:", posicion)

# startswith
resultado = texto.strip().startswith("Ejemplo")
print("\nstartswith:", resultado)

# EJERCICIO 5
import re

frase = """En un lugar de la Mancha,
de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo
de los de lanza en astillero, adarga antigua,
rocín flaco y galgo corredor."""

num_ocurrencias = len(re.findall("a", frase))

print("\nEl número de ocurrencias de la letra 'a' es:", num_ocurrencias)
