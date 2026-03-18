# Si el formato no es correcto, devuelve `False` (no lanza excepciones).

from ejercicio02 import validar_nif
import pytest

def test_validar_nif_string():
    assert validar_nif('12345678Z') == True

@pytest.mark.parametrize("nif, esperado", [
    ('12345678Z', True),
    ('12345678z', True)
])
def test_validar_nif_minusculas_mayusculas(nif, esperado):
    assert validar_nif(nif) == esperado

@pytest.mark.parametrize("nif, esperado", [
    (' 12345678Z', True),
    ('12345678Z ', True)
])
def test_validar_nif_espacios_inicio_fin(nif, esperado):
    assert validar_nif(nif) == esperado

@pytest.mark.parametrize("nif, esperado", [
    ('12345678Z', True),
    ('12345678A ', False)
])
def test_validar_nif_letra_control(nif, esperado):
    assert validar_nif(nif) == esperado

@pytest.mark.parametrize("nif, esperado", [
    ('1234 5678Z ', False),
    ('b2345678A ', False),
    ('12345678A', False)
])
def test_validar_nif_formato__correcto(nif, esperado):
    assert validar_nif(nif) == esperado
