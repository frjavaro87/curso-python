"""traer todos los correos del mailing text que se anexa
la intención es saber como extraer el texto que necesitemos de una lista de n lineas"""

datamail = open("/home/francisco/Proyectos/Curso-python/curso-python/mailing2.txt")
mails = datamail.read()

i = 0
result = []
subject = 0
keyword1 = 'From'
keyword2 = 'Received'
print(keyword1)
print(keyword2)

for keyword1 in mails:
    if keyword1 == 'From':
       print(encontrado)
    else:
       print(2)