#pares ordenados

cuadrados = []
raices = []

def raiz(num):
    return num * 0.5

for y in range(50):

    w = (y ** 2)

    cuadrados.append(w)
    raices.append(raiz(w))

print(raices)