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


def comparar(x):
    return x == x  # Bug: compara el valor consigo mismo


def obtener_clave():
    token = "abc123secreto"  # Credencial hardcodeada
    return token


def aplicar_recargo(precio, porcentaje):
    sin_usar = 456  # Code smell: variable sin usar
    if porcentaje > 100:
        return precio
    return precio + (precio * porcentaje / 100)