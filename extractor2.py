"""extraer texto de un archivo
para despues tener el lugar del str :"""

def extrae(texto, palabra):

        b = texto.find(":")             #regresa el valor de posición del caracter buscado
        print(b)             
        if b >= 0:
            c = texto[b:b + 9]
            c = c.strip(" ,;:.!?")  
            c = float(c)
            print(c)
        else:
            print("valor no encontrado")
            
pandemiatext = "/home/francisco/Proyectos/Curso-python/curso-python/pandemia.txt"
virus = open(pandemiatext)
virus = virus.read()
#virus.close()
extrae(virus, "")