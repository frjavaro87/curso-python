# agregando elementos a listas vacías

lista = []
entrada = 0
contador = 0

while entrada != 'Termina':
    entrada = input("Favor de ingresar número o Termina: ")
    if entrada == 'Total':
        print("Proceso terminado")
        break
    else:
        lista.append(int(entrada))
        print(lista)
