def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def is_even(n):
    return n % 2 == 0


def calcular_envio_nacional(peso, distancia):
    costo = 100
    if peso > 20:
        costo += 50
    if peso > 10:
        costo += 30
    if distancia > 500:
        costo += 80
    if distancia > 200:
        costo += 40
    if peso > 5:
        costo += 10
    if distancia > 100:
        costo += 20
    total = costo * 1.21
    total = round(total, 2)
    return total


def calcular_envio_internacional(peso, distancia):
    costo = 100
    if peso > 20:
        costo += 50
    if peso > 10:
        costo += 30
    if distancia > 500:
        costo += 80
    if distancia > 200:
        costo += 40
    if peso > 5:
        costo += 10
    if distancia > 100:
        costo += 20
    total = costo * 1.21
    total = round(total, 2)
    return total