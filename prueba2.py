"""Una juguetería tiene mucho éxito en dos de sus productos: 
payasos y muñecas. Suele hacer venta por correo y la empresa 
de logística les cobra por peso de cada paquete así que deben 
calcular el peso de los payasos y muñecas que saldrán en cada 
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado."""

print('Juguetería Nueva Infancia')

clowns = int(input('Indica las piezas de payasos solicitados: '))
it = clowns * 112
dolls = int(input('Indica las piezas de muñecas: '))
anabelle = dolls * 75

weigth = it + anabelle

print('El peso total de tu paquete es de: ', weigth, 'grs')
