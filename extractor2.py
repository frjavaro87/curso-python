#extractor de un texto con función

def extrae(texto):

    b = texto.find(":")
    print(b)             #regresa el valor de posición del caracter buscado
    if b >= 0:
        c = texto[b: b + 100]
        c = c.strip(" ,;:.!?")  
        c = float(c)
        print(c)
    else:
        print("valor no encontrado")

    pandemiatext = "/home/francisco/Proyectos/Curso-python/curso-python/pandemia.txt"
    virus = open(pandemiatext)
    print(virus.readlines())
    virus.close()

extrae("virus")