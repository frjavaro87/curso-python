"""escritura de archivos que tengan que ver con nóminas
en el archivo creado habrá nombre empleado, fecha en formato YYYY, MM, DD
horas trabajadas, salario por día, bruto, impuestos y deberá generarse una línea"""

def write(concatenado):
    documento = open("nomina.txt", "a")
    documento.write(concatenado)
    documento.close()

def impuestos(pago):
    return pago * 0.15

def nomina():
    
    nombre = str(input("Dame el nombre del empleado: "))
    date = str(input("Dame la fecha de trabajo (Formato YYYY-MM-DD): "))
    horas = float(input("Dame horas trabajadas ese día: "))
    pago = float(input("Dame el costo: "))

    bruto = horas * pago
    imp = impuestos(bruto)
    pago_neto = bruto - imp

    if horas > 40:
        extra = horas - 40
        extra_time = extra * pago * 1.5
        concatenado = "El salario de bruto de " + nombre + "quien trabajó el día: " + date + "trabajando: " + str(horas) + "es de: " + str(pago_neto)
        write(concatenado)
    else:
        concatenado = "El salario de bruto de " + nombre + "quien trabajó el día: " + date + "trabajando: " + str(horas) + "es de: " + str(pago_neto)
        write(concatenado)
nomina()


