# Variable que almacena la contraseña registrada
Var_Con = "contraseña"

# Solicita al usuario que ingrese su contraseña y la convierte a minúsculas
Con_User = input("Ingrese su contraseña(Mayusculas y minusculas indistinguibles): ").lower()

# Compara la contraseña ingresada (en minúsculas) con la registrada
if Con_User == Var_Con:
    print("Su contraseña coincide con la registrada")
else:
    # Si no coincide, muestra un mensaje de error
    print("Su contraseña no coincide con la registrada")