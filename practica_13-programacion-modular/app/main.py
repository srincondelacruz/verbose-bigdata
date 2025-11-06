from app.operaciones_basicas import operar_todo
from app.estadisticas import calcular_media, calcular_mediana, calcular_moda
from operaciones_especiales.potencias_raices import potencia, raiz_cuadrada
from operaciones_especiales.log_exp import logaritmo, exponencial

def main():
    a = 10
    b = 5
    lista = [1, 2, 3, 4, 4, 5]

    print("=== Operaciones Básicas ===")
    resultados = operar_todo(a, b)
    for operacion, resultado in resultados.items():
        print(f"{operacion}: {resultado}")

    print("\n=== Estadísticas Básicas ===")
    print(f"Media: {calcular_media(lista)}")
    print(f"Mediana: {calcular_mediana(lista)}")
    print(f"Moda: {calcular_moda(lista)}")

    print("\n=== Operaciones Especiales ===")
    print(f"Potencia ({a}^{b}): {potencia(a, b)}")
    print(f"Raíz cuadrada de {a}: {raiz_cuadrada(a)}")
    print(f"Logaritmo de {a} base e: {logaritmo(a)}")
    print(f"Exponencial de {b}: {exponencial(b)}")

if __name__ == "__main__":
    main()

