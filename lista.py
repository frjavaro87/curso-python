# agregando elementos a listas vacías
#max()
#min()

lista = []
entrada = 0
contador = 0

while entrada != 'Termina':
    entrada = input("Favor de ingresar número o Termina: ")
    if entrada == 'Termina':
        print(f'Proceso terminado, el máximo es: {max(lista)} ')
        print(f'Proceso terminado, el mínimo es: {min(lista)} ')
        print(f"Las interaciones fueron: {contador} ")
        
        #print("Tu lista es: ", lista)

        break
    else:
        lista.append(int(entrada))
        contador+= 1
        
