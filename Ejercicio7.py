#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

num1 = 0
num2 = 0

num1 = input("Digite el primer numero: ")
num2 = input("Digite el segundo numero: ")


if num1>num2:
    print("el numero 1 es mayor que el numero 2")
elif num2>num1:
    print("el numero 2 es menor que el numero 1")
else:
    print("el numero 1 y el numero 2 son iguales")
    