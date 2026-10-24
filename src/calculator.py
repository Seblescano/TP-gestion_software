from src.calculator import calcular_descuento

def test_descuento():
    assert calcular_descuento(100, 10) == 90

def test_descuento_mayor_a_100():
    assert calcular_descuento(100, 150) == 0