#extractor de un texto con función

def extrae(texto):

    b = texto.find(":")             #regresa el valor de posición del caracter buscado
    print(b)             
    if b >= 0:
        c = texto[b:]
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