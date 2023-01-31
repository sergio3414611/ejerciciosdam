# EJERCICIO 1
print("EJERCICIO 1")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = float(input("Introduce la nota obtenida en " + asignatura + ": "))
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + str(notas[i]))

# EJERCICIO 2
print("\nEJERCICIO 2")
numeros_ganadores = []
fin = False

while not fin:
    num = input("Introduce un número ganador de la lotería (escribe 'salir' para terminar): ")
    if num.lower() == 'salir':
        fin = True
    else:
        numeros_ganadores.append(int(num))

numeros_ganadores.sort()
print("Los números ganadores ordenados de menor a mayor son:", numeros_ganadores)

# EJERCICIO 3
print("\nEJERCICIO 3")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = float(input(f"Introduce la nota de {asignatura}: "))
    notas.append(nota)

asignaturas_suspendidas = []
for i, asignatura in enumerate(asignaturas):
    if notas[i] < 5:
        asignaturas_suspendidas.append(asignatura)

if len(asignaturas_suspendidas) == 0:
    print("Felicidades, has aprobado todas las asignaturas.")
else:
    print("Tienes que repetir las siguientes asignaturas:")
    for asignatura in asignaturas_suspendidas:
        print(asignatura)

# EJERCICIO 4
def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return palabra == palabra[::-1]

palabra = input("Introduce una palabra: ")
if palindromo(palabra):
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")


# EJERCICIO 5
print("\nEJERCICIO 5")
def contar_vocales(palabra):
    vocales = "aeiouáéíóú"
    contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(palabra)):
        if palabra[i].lower() in vocales:
            if palabra[i].lower() == "a":
                contador[0] += 1
            elif palabra[i].lower() == "e":
                contador[1] += 1
            elif palabra[i].lower() == "i":
                contador[2] += 1
            elif palabra[i].lower() == "o":
                contador[3] += 1
            elif palabra[i].lower() == "u":
                contador[4] += 1
            elif palabra[i].lower() == "á":
                contador[5] += 1
            elif palabra[i].lower() == "é":
                contador[6] += 1
            elif palabra[i].lower() == "í":
                contador[7] += 1
            elif palabra[i].lower() == "ó":
                contador[8] += 1
            elif palabra[i].lower() == "ú":
                contador[9] += 1
    return contador

def main():
    palabra = input("Introduce una palabra: ")
    contador = contar_vocales(palabra)
    print("a:", contador[0])
    print("e:", contador[1])
    print("i:", contador[2])
    print("o:", contador[3])
    print("u:", contador[4])
    print("á:", contador[5])
    print("é:", contador[6])
    print("í:", contador[7])
    print("ó:", contador[8])
    print("ú:", contador[9])

"""Forma de ejecutar un script de Python que asegura se asegura que el código en main() 
solo se ejecute cuando se ejecute el script directamente, y no cuando se importe como 
un módulo en otro script."""

if __name__ == "__main__":
    main()


# EJERCICIO 6
print("\nEJERCICIO 6")
def main():
    diccionario = {}
    palabras = input("Introduce las palabras y sus traducciones en formato 'palabra:traducción': ")
    palabras = palabras.split(",")
    
    for palabra in palabras:
        traduccion = palabra.split(":")
        diccionario[traduccion[0]] = traduccion[1]
    
    frase = input("Introduce una frase en español: ")
    frase_traducida = []
    
    for palabra in frase.split(" "):
        if palabra in diccionario:
            frase_traducida.append(diccionario[palabra])
        else:
            frase_traducida.append(palabra)
    
    print("Frase traducida:", " ".join(frase_traducida))

if __name__ == "__main__":
    main()


# EJERCICIO 7
print("\nEJERCICIO 7")
def main():
    facturas = {}
    cobrado = 0
    while True:
        accion = input("¿Quieres añadir una nueva factura, pagar una existente o terminar? (a/p/t): ")
        if accion == 'a':
            num_factura = input("Número de factura: ")
            coste = int(input("Coste de la factura: "))
            facturas[num_factura] = coste
        elif accion == 'p':
            num_factura = input("Número de factura a pagar: ")
            if num_factura in facturas:
                cobrado += facturas[num_factura]
                del facturas[num_factura]
                print("Factura pagada.")
            else:
                print("Factura no encontrada.")
        elif accion == 't':
            break
        print("Cantidad cobrada: ", cobrado)
        print("Cantidad pendiente de cobro: ", sum(facturas.values()))

if __name__ == "__main__":
    main()
