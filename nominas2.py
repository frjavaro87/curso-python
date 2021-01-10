# nominas con def()

def impuestos(pago):

    return pago * 0.15

def nomina(horas, pago):

    bruto = horas * pago
    imp = impuestos(bruto)
    pago_neto = bruto - imp

    print("El bruto es de: ", bruto, " y el neto es de: ", pago_neto)

nomina(23, 34)
