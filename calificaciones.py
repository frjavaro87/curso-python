# calificaciones

print("Favor de ingresar un numero del 0 al 10")
calif = float(input())

if (calif >= 10.0 and calif <= 0.0):
    print("La calificación es errónea")
else:
    if(calif >= 9):
        print("A")
    elif(calif >= 8.0 and calif <= 9.0):
        print("B")
    elif(calif >= 7.0 and calif <= 8.0):
        print("C")
    elif(calif >= 6.0 and calif <= 7.0):
        print("D")
    else:
        print("F")