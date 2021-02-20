""" se abre archivo"""

rick = '/home/francisco/Proyectos/Curso-python/curso-python/rick.py'
data = open(rick)
rick2 = data.readlines()

""" creando diccinarios"""

for text in rick2:
    print(text)