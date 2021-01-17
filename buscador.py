#búsqueda en textos
#definiendo la función de búsqueda
def busqueda(texto, keyword):
    descompone = texto.split()      #descompongo el textoen forma de lista
    print(descompone)
    #text.rstip(",.;:")
    for palabra in descompone:      #inicio el barrido de la palabra en la lista
        print(palabra)
        if palabra == keyword:      #comparo cada palabra con la palabra clave
            print("Palabra encontrada") #resultado de la búsqueda
            break                       #sirve para dejar de imprimir el resultado
        else:
            pass                        #si no encuentra la palabra, se detiene
tex = input("Ingresa el texto a buscar: ")  # texto a estudiar  
search = input("Ingresa tu palabra a buscar: ") #palabra clave

busqueda(tex,search)