# calculadora de nómina que toma 2 parametros de entrada, las horas trabajadas, y el pago por hora
# si viene vacío, termina, en caso contrario, da el resultado.

try:
    print("Buenas tardes, favor de introducir los campos requeridos: ")
    print("Horas trabajadas?: ")
    horas = int(input())
    print("Pago por tiempo?: ")
    pago = float(input())

    print("El pago por tu trabajo es de: ", horas * pago)

except:
        print("Error, ingrese nuevamente")
