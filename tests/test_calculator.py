import pytest

from src.calculator import add, subtract, divide, is_even


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False

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