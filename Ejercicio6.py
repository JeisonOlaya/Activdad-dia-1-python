#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.

numero_secreto = 7

for intento in range(1, 11):
    adivina = int(input(f"Intento {intento} de 10 - Adivina el número secreto (entre 1 y 10): "))
    
    if adivina < numero_secreto:
        print("Tu número es menor que el número secreto.\n")
    elif adivina > numero_secreto:
        print("Tu número es mayor que el número secreto.\n")
    else:
        print("¡Felicidades! Adivinaste el número secreto.")
        break
else:
    print(f"\nLo siento, se te acabaron los intentos. El número secreto era {numero_secreto}.")
    