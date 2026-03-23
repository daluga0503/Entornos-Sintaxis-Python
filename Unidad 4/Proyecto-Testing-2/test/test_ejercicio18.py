from ejercicio18 import unicos
import pytest

def test_unicos_lista_vacia():
    assert unicos([]) == []

@pytest.mark.parametrize("entrada, esperado",[
    (['león', 'zebra', 'geopardo', 'jirafa'], ['león', 'zebra', 'geopardo', 'jirafa']),
    ([1,2,3,4,5], [1,2,3,4,5])
])
def test_unicos_exitoso_sin_duplicados(entrada, esperado):
    assert unicos(entrada) == esperado

@pytest.mark.parametrize("entrada, esperado", [
    (['jirafa', 'león', 'geopardo', 'zebra', 'geopardo', 'jirafa'], ['jirafa', 'león', 'geopardo', 'zebra']),
    ([1,5,2,4,3,4,5], [1,5,2,4,3])
])
def test_unicos_exitoso_con_duplicados(entrada, esperado):
    assert unicos(entrada) == esperado

@pytest.mark.parametrize("entrada, esperado", [
    (['jirafa', 10, 'león', 'geopardo', 5, 'zebra', 'geopardo', 10, 'jirafa'], ['jirafa', 10, 'león', 'geopardo', 5, 'zebra']),
    ([1,5,'mariposa',2,4,3,'libelula',4,5], [1,5,'mariposa',2,4,3,'libelula'])
])
def test_unicos_exitoso_con_duplicados_valores_distintos(entrada, esperado):
    assert unicos(entrada) == esperado

