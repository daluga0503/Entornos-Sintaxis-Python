from ejercicio15 import deg_a_rad
import pytest


@pytest.mark.parametrize("entrada, esperado", [
    (0,0),
    (15, 0.261),
    (30, 0.523),
    (38, 0.663),
    (90, 1.570),
    (100, 1.745)
])
def test_deg_a_grad_entrada_positiva(entrada, esperado):
    assert deg_a_rad(entrada) == esperado


@pytest.mark.parametrize("entrada, esperado", [
    (-5, -0.087),
    (18, -0.314),
    (-30, -0.523),
    (78, -1.361),
    (-196, -3.420),
    (-273, -4.764)
])
def test_deg_a_grad_entrada_negativa(entrada, esperado):
    assert deg_a_rad(entrada) == esperado


@pytest.mark.parametrize("entrada, esperado", [
    (36.6, 0.683),
    (42.5, 0.741),
    (39.2, 0.684),
    (0.01, 0.00017),
    (-2.5, -0.0436),
    (-18.4, -0.3211),
    (-21.1, -0.3683)
])
def test_deg_a_grad_entrada_decimal(entrada, esperado):
    assert deg_a_rad(entrada) == esperado


@pytest.mark.parametrize("entrada, esperado", [
    ("27", TypeError),
    (False, TypeError),
    (True, TypeError),
    ([27], TypeError),
    ({1:27}, TypeError),
    (None, TypeError)
])
def test_deg_a_grad_entrada_incorrecta(entrada, esperado):
    with pytest.raises(esperado):
        deg_a_rad(entrada)