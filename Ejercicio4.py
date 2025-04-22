# Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".

contraseñaReal = "python123"
contraseñaUsuario = str(input("Digite la contraseña: "))


if contraseñaUsuario==contraseñaReal:
    input("acceso concedido")
else:
    input("acceso denegado")
   

