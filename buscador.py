#búsqueda en textos

#definiendo la función de búsqueda

def busqueda(texto, keyword):

    descompone = texto.split()
    print(descompone)
    #text.rstip(",.;:")
    for palabra in descompone:
        print(palabra)
        if palabra == keyword:
            print("alabra encontrdad")
            break
        else:
            pass

tex = input("Ingresa el texto a buscar: ")
search = input("Ingresa tu palabra a buscar: ")

busqueda(tex,search)