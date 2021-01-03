# tipos de datos en Python

x = "Hola mundo" #string
edad = 25 #entero
peso = 78.5 #float
delta = 5j #complex
lista = ["Rodolfo", "javier", "martin"] #list, puedo modificarlo
tupledata = {"Rodolfo", "javier", "martin"} #tupla, NO MODIFICABLE
rangedata = range(100) #rango
dicdata = {"nombre": "rodolfo", "edad": 25} #llave valor, uno a uno, siempre. SI NO PONGO LLAVES,
#SE COMPORTA COMO LISTA
flag = True #booleano, siemprela primera en maúscula

userdata = [{"nombre": "rodolfo", "edad": 25}, {"nombre": "rodolfo", "edad": 25}]

print(type(userdata[0]['nombre']))
