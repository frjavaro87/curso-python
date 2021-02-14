"""Los alumnos de un curso se han dividido en dos grupos A y B 
de acuerdo al sexo y el nombre. El grupo A esta formado por 
las mujeres con un nombre anterior a la M y los hombres con un 
nombre posterior a la N y el grupo B por el resto. Escribir un 
programa que pregunte al usuario su nombre y sexo, y muestre por 
pantalla el grupo que le corresponde."""

print('Grupos extraños')
nombre = input('Introduce un nombre: ')
sexo = input('Ingresa el sexo: ')
name = nombre[0]
excentos = ['m', 'n']

mujeres = ['a','b','c','d','e','f','g','h','i','j','k','l']
hombres = ['o', 'p','q','r','s','t','u','v','w','x','y','z']

if (sexo == 'F'):
    if name[0] in mujeres:
        print(nombre, 'pertenece al grupo A')
    else:
        print(nombre, 'pertenece al grupo B')
elif (sexo == 'M'):
    if name[0] in hombres:
        print(nombre, 'pertenece al grupo A')
    else:
        print(nombre, 'pertenece al grupo B')
