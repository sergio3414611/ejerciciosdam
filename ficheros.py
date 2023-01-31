# EJERCICIO 1
print("EJERCICIO 1")
def main():
    num = int(input("Introduce un número entero entre 1 y 10: "))
    if num < 1 or num > 10:
        print("El número introducido no es válido.")
        return
    
    fichero = "tabla-" + str(num) + ".txt"
    with open(fichero, "w") as f:
        for i in range(1, 11):
            f.write(str(num) + " x " + str(i) + " = " + str(num * i) + "\n")
    print("La tabla de multiplicar se ha guardado en el archivo " + fichero)

if __name__ == "__main__":
    main()

# EJERCICIO 2
print("\nEJERCICIO 2")
def main():
    num = int(input("Introduce un número entero entre 1 y 10: "))
    if num < 1 or num > 10:
        print("El número introducido no es válido.")
        return
    try:
        with open(f'tabla-{num}.txt', 'r') as f:
            for line in f:
                print(line, end='')
    except FileNotFoundError:
        print(f"No se encontró el archivo tabla-{num}.txt.")

if __name__ == "__main__":
    main()