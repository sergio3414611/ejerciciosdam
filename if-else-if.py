# EJERCICIO 2
print("EJERCICIO 2")
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# EJERCICIO 3
print("\nEJERCICIO 3")
contraseña = "contraseña"
respuesta = input("Introduce la contraseña: ")

if respuesta.lower() == contraseña.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

# EJERCICIO 4
print("\nEJERCICIO 4")
num = int(input("Ingresa un número entero: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# EJERCICIO 5
print("\nEJERCICIO 5")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num2 != 0:
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
else:
    print("Error: No se puede dividir por cero.")