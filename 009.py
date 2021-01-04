# ejercicio con try y except

try:
    paciente = input("Ingrese el nombre del paciente")
    print("Cálculo de Indice de Masa Corporal")
    print("Favor de ingresar tu estatura en m")
    estatura = float(input())
    print("Favor de ingresar tu peso en kg")
    peso = float(input())

    IMC = peso / (estatura ** 2)

    print(f'El peso de {paciente} es de {peso}Kg; mide {estatura}m y tiene un IMC de {IMC}')

except:
    print("Ingrese los valores correctos")
