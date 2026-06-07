def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo")
    return n ** 0.5