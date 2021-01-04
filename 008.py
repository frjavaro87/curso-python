#solicitar user, pasword, y validar si están bien, imprimir sesión iniciada
#con elif que lo revise
#si ninguno es correcto, que inicie de nuevo

username = None #input("Dame tu usuario")
password = input("Dame tu password")

if(username != None):
    if(username == "Javier" and (password == "fcojavi" and len(password) == 7)):
        if(len(username) > 4):
            print(f"Acceso correcto, bienvenido usuario: {username}")
        else:
            print("bienvenido")
elif(username == None):            
    print("Tu usuario está mal")

elif(username == "Javier" and (password != "fcojavi" and len(password) >= 1 and len(password) < 8)):

    if(len(password) < 7):
        print("La contraseña tiene menos caracteres")
    else:
        print("Contraseña errónea")
     

else:
    print("Todo mal, largo...")