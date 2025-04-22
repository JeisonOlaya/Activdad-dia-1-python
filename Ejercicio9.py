#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

Año=int(input("Ingresa por favor el año para determinar si es bisiesto o no: "))

if Año % 4 !=0: # EL año no es divisible entre 4
    print("El año que ingresaste no es bisiesto")
elif Año % 4 == 0 and 100 != 0: # El año es divisible entre 4 y no entre 100 o 400
    print ("El año que ingresaste es bisiesto")
elif Año % 4 == 0 and Año % 100 == 0 and Año % 400!= 0: # el año es divisible entre 4 y 100 y no entre 400
    print("El año que ingresaste no es bisiesto")
elif Año % 4 == 0 and Año % 100 == 0 and Año % 400 == 0: #el año es divisible entre 4, 100 y 400
	print("El año que ingresaste es bisiesto")