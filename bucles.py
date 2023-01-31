# EJERCICIO 2
print("EJERCICIO 2")
num = int(input("Ingresa un número entero positivo: "))
if num >= 0:
    for i in range(num, -1, -1):
        print(i, end=", ")
    #print("0")
else:
    print("El número ingresado no es positivo.")

# EJERCICIO 3
print("\nEJERCICIO 3")
num = int(input("Ingresa un número entero positivo: "))
if num >= 1:
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i, end=", ")
    print("")
else:
    print("El número ingresado no es positivo.")

# EJERCICIO 4
print("\nEJERCICIO 4")
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print("\n")

# EJERCICIO 5
print("\nEJERCICIO 5")
while True:
    user_input = input("Ingrese una frase: ")
    if user_input.lower() == "salir":
        break
    print(user_input)