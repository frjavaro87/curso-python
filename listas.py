#trabajando con listas

#apertura de archivo y división de líneas
#-*- coding: utf-8 -*-
main = open("/home/francisco/Proyectos/Curso-python/curso-python/ReadingData2.txt")
text = main.read()

listavacia = []
palabras = []

descompone = text.split()

for palabra in descompone:
        if palabra in listavacia:     
        pass
    else:
        listavacia.append(palabra)

print(f'Se eencontraron palabras unicas', len(listavacia))
