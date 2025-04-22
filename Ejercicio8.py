#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

Altura = float (input("por favor ingresa su altura en metro: "))
Peso = float (input("por favor ingrese su peso en kilogramo: "))
Imc = Peso / Altura**2
print(f"su imc es: {Imc}")



if Imc < 18.5:
    print("estas bajito de peso")
elif Imc >= 18.5 and Imc <=24.9:
    print("Su peso es normal")
elif Imc>=18.5 and Imc <=24.9:
    print("estas en sobre peso")
elif Imc>=30:
    print("estas en sobre peso")
