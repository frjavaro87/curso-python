# operaciones entre 2 num + - * /

a = 458
b = 569
c = a + b
# suma
print(f' la suma es: %2d' %  (c))

# se usa la f para formatear sin necesidad de usar str o int

# resta
print(f' la resta es: {c}')

#se usan las llaves para reducir la linea de codigo, la comilla después de las llaves

# mult
#print(a * b)
print(f' la mult es: {a * b}')

# en caso de que se pongan textos en una operación, es cuando se tienen problemas de sintaxis
#división
print(f' la div es: {a / b}')

