# solicitar 2 numeros y mostrar cual es menor. Si son iguales, que lo imprima.

#print("Hola, ingresa 2 números")

a = float(input("Ingresa número 1: "))
b = float(input("Ingresa número 2: "))

if a < b:
    print("El primer número es menor")
elif a > b: 
    print("El segundo número es menor")
else:
    print("Son iguales")