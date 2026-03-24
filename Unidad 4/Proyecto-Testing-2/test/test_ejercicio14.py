from ejercicio14 import interseccion_estable
import pytest

@pytest.mark.parametrize("lista1, lista2, esperado", [
    ([1,2,3,4,5], [5,4,3,2,1], [1,2,3,4,5]),
    ([5,4,3,2,1], [1,2,3,4,5], [5,4,3,2,1]),
    ([1,0,1,0,1,0], [1,2,3,4,5], [1,0,2,3,4,5]),
    ([1,1,1], [1,1,1], [1]),
    ([1,0,1,0], [1,0,1,0], [1,0]),
    ([], [1,2,3,1,2,3], [1,2,3]),
    ([1,2,3,1,2,3], [], [1,2,3]),
    ([1,2,3,4,5,5,4,3,2,1], [5,4,3,2,1], [1,2,3,4,5]),
    ([5,4,3,2,1], [1,2,3,4,5,4,3,2,1], [5,4,3,2,1]),
])
def test_interseccion_estable_exitoso(lista1, lista2, esperado):
    assert interseccion_estable(lista1, lista2) == esperado

@pytest.mark.parametrize("lista1, lista2, esperado", [
    ([1,2,3,4], 'cadena', TypeError),
    ([1,2,3,4], 2, TypeError),
    ([1,2,3,4], False, TypeError),
    ([1,2,3,4], None, TypeError),
    ('cadena', [1,2,3,4], TypeError),
    (2, [1,2,3,4], TypeError),
    (False, [1,2,3,4], TypeError),
    (None, [1,2,3,4], TypeError),
    ('cadena1', 'cadena2', TypeError),
    (10, 20, TypeError),
    (False, True, TypeError),
    (None, None, TypeError)
])
def test_interseccion_estable_parametros_erroneos(lista1, lista2, esperado):
    with pytest.raises(esperado):
        interseccion_estable(lista1, lista2)

def test_interseccion_estable_listas_vacias():
    interseccion_estable([], []) == []