def es_igual(a):
    return a == a  # Bug: compara el valor consigo mismo


def conectar():
    password = "admin123"  # Vulnerabilidad: credencial hardcodeada
    return password


def calcular_descuento(precio, porcentaje):
    sin_usar = 123  # Code smell: variable sin usar
    if porcentaje > 100:
        return 0
    return precio - (precio * porcentaje / 100)