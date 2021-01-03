# operaciones entre 2 num + - * /

a = input()
b = input()

c = a + b
d = a * b
e = a - b
f = a / b

# suma
print(f' la suma es: {c}')
# se usa la f para formatear sin necesidad de usar str o int
# resta
print(f' la resta es: {e}')
#se usan las llaves para reducir la linea de codigo, la comilla después de las llaves
#e = int(a * b)
# mult
#print(a * b)
print(f' la mult es: {e}')

# en caso de que se pongan textos en una operación, es cuando se tienen problemas de sintaxis
f = int(a / b)
#división
print(f' la div es: {f}')