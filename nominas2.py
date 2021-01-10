# nominas con def()

def impuestos(pago):

    return pago * 0.15

def nomina():

    horas = float(input("Dame horas: "))
    pago = float(input("Dame el costo: "))
    bruto = horas * pago
    imp = impuestos(bruto)
    pago_neto = bruto - imp
    
    if horas > 40:
        extra = horas - 40
        extra_time = extra * pago * 1.5
        print("bruto: ", bruto, "neto: ", pago_neto + extra_time)
    else:
        print("El bruto es de: ", bruto, " y el neto es de: ", pago_neto)

nomina()
