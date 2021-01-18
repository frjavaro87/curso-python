# extractor de palabras 

def extrae(texto):

    b = texto.find(":")             #regresa el valor de posición del caracter buscado
    if b >= 0:
       # tex.rstrip(",.:;")
        c = texto[b: b + 8]
        c = c.strip(" ,;:.!?")  
       # d = int(c)
       # print(c)
        c = float(c)
        print(c)
    else:
        print("valor no encontrado")

#tex = input("Dame el texto a ingresar: ")

extrae("Una zanahoria contiene: 89.265 mg de betacaroteno en promedio ")