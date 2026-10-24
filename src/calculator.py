def es_igual(a):
    # Bug: compara el valor consigo mismo, siempre es True
    return a == a


def calcular_descuento(precio, porcentaje):
    sin_usar = 123  # code smell: variable sin usar
    if porcentaje > 100:
        return 0
    return precio - (precio * porcentaje / 100)