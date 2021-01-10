# nominas con def()

def impuestos(pago):

    return pago * 0.15

def nomina():

    horas = float(imput("Dame horas: "))
    pago = float(input("Dame el costo: "))
    bruto = horas * pago
    imp = impuestos(bruto)
    pago_neto = bruto - imp

if horas > 40:
    extra_time = pago * 1.5
    print("Bruto es de: ", bruto, "neto es de: ", )
    print("El bruto es de: ", bruto, " y el neto es de: ", pago_neto)

nomina()
