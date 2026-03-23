from ejercicio12 import precio_con_iva
import pytest

@pytest.mark.parametrize("precio, iva, esperado", [
    (100, 21, 121),
    (50, 21,60.5),
    (75, 10, 82.5),
    (30, 0, 30)
])
def test_precio_con_iva_correcto_valor_iva_no_default(precio, iva, esperado):
    assert precio_con_iva(precio, iva) == esperado

@pytest.mark.parametrize("precio, esperado", [
    (100, 121),
    (50, 60.5),
    (75, 90.75),
    (30, 36.3)
])
def test_precio_con_iva_correcto_valor_iva_default(precio, esperado):
    assert precio_con_iva(precio) == esperado


@pytest.mark.parametrize("precio, iva, esperado", [
    (20, 0, 20),
    (0, 21, ValueError),
    (0, 0, ValueError)
])
def test_precio_con_iva_valor_precio_0(precio, iva, esperado):
    with pytest.raises(esperado):
        precio_con_iva(precio, iva)


@pytest.mark.parametrize("precio, iva, esperado", [
    ('20', 10, ValueError),
    (20, '10', ValueError),
    ('20', '10', ValueError)
])
def test_precio_con_iva_valor_no_numerico(precio, iva, esperado):
    with pytest.raises(esperado):
        precio_con_iva(precio, iva)


@pytest.mark.parametrize("precio, iva, esperado", [
    (-20, 10, ValueError),
    (20, -10, ValueError),
    (-20, -10, ValueError)
])
def test_precio_con_iva_valor_negativo(precio, iva, esperado):
    with pytest.raises(esperado):
        precio_con_iva(precio, iva)
