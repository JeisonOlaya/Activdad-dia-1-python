#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

TotalCuenta = float (input("Ingrese el total de la cuenta: "))

propina = float (input("digite que porcentaje de propina quieres dejar: 10%,15%, 20%: "))


if propina == 10:
    propinaTotal = (TotalCuenta/100)*10
    print(f"el total de la propina es: {propinaTotal}")
elif propina ==15:
    propinaTotal = (TotalCuenta/100)*15
    print(f"el total de la propina es:  {propinaTotal}")

elif propina == 20:
    propinaTotal = (TotalCuenta/100)*20
    print(f"el total de la propina es: {propinaTotal}")
else:
    print("el porcentaje no es valido")
    