"""programa de lista de numeros por el usuario
cuando escriba finalizar, me de en el print el max, min, promedio
y el largo de la lista generada 5, 10, 15 y 20"""

print("Series de numeros")

i = 0
total = 0
num = 0
lista = []
prom = 0

def promedio(total, lista):
    s = total
    r = len(lista)
    prom = s / r
    return prom

while num != 'finalizar':
    num = input("Favor de ingresar números o escriba finalizar: ")
    if num == 'finalizar':
        average = promedio(total, lista)
        print("Proceso terminado")
        print(lista)
        print(f'El máximo es: ', max(lista))
        print(f'El mínimo es: ', min(lista))
        print(f'El promedio es: ', average)
        print(f'La lista tiene: ', len(lista), 'elementos')
        break
    else:
        i+= 1
        total = total + int(num)
        #print("suma es de: ", total)
        lista.append(float(num))
        