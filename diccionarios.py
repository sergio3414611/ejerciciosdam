# EJERCICIO 2
print("EJERCICIO 2")
divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa usuario: ")

if divisa in divisas:
    simbolo = divisas[divisa]
    print("El símbolo de la divisa " + divisa + " es " + simbolo)
else:
    print("La divisa introducida no está en el diccionario.")

# EJERCICIO 3
print("\nEJERCICIO 3")
usuario = {}
usuario['nombre'] = input("Introduce tu nombre: ")
usuario['edad'] = input("Introduce tu edad: ")
usuario['direccion'] = input("Introduce tu dirección: ")
usuario['telefono'] = input("Introduce tu número de teléfono: ")

print(usuario['nombre'] + " tiene " + usuario['edad'] + " años, vive en " 
+ usuario['direccion'] + " y su número de teléfono es " + usuario['telefono'])

# EJERCICIO 4
print("\nEJERCICIO 4")
frutas = {"piña": 3.5, "cereza": 4.2, "fresa": 4.8}
fruta = input("Introduce una fruta: ")
kg = float(input("Introduce el número de kilos: "))

if fruta in frutas:
  precio = frutas[fruta] * kg
  print(f"El precio de {kg} kilos de {fruta} es {precio}")
else:
  print(f"La fruta {fruta} no está en el diccionario.")