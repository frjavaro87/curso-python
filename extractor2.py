#extractor de un texto con función

def extrae(texto):

    b = texto.find(":")             #regresa el valor de posición del caracter buscado
    if b >= 0:
       # tex.rstrip(",.:;")
        c = texto[b: b + 10]
        c = c.strip(" ,;:.!?")  
       
        c = float(c)
        print(c)
    else:
        print("valor no encontrado")

pandemiatext = "/home/francisco/Proyectos/Curso-python/curso-python/pandemia.txt"
virus = open(pandemiatext)
print(virus.readline())
virus.close()

extrae(virus)