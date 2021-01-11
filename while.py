# ciclo while

i = 0
total = 0
num = 0

while num != 'Total':
    num = input("Favor de ingresar número o escriba Total: ")
    if num == 'Total':
        print("Proceso terminado")
        break
    else:
        i+= 1
        total = total + int(num)
        print("La suma es de: ", total)

#print("la suma es de: ", i )

    