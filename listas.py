#trabajando con listas

#apertura de archivo y división de líneas

#-*- coding: utf-8 -*-
main = open("/home/francisco/Proyectos/Curso-python/curso-python/ReadingData2.txt")
text = main.read()
print(text)
#main.close()

listavacia = []
palabras = []
descompone = text.split()
print(descompone)

for palabras in descompone:
    #print(palabras)
    if palabras in text:
        pass
    else:
        listavacia.append(palabras)
        #print(listavacia)

      
    