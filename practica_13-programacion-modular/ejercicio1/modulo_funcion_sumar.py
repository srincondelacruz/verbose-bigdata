# Definimos las funciones
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

def restar(a, b):
    resultado_resta = a - b
    return resultado_resta

def multiplicar(a, b):
    resultado_multiplicacion = a * b
    return resultado_multiplicacion

def dividir(a, b):
    if b != 0:
        resultado_division = a / b
        return resultado_division
    else:
        return "Error: División por cero no permitida"




# Prueba de la función sumar
# print(f'Prueba de la función sumar desde el módulo: {sumar(15, 30)} ')

'''
if __name__ == '__main__':
    print(f'Prueba de la función sumar desde el módulo: {sumar(15, 30)} ')
    print('__name__')
'''