from src.ejercicio01 import normaliza_nombre
import pytest

@pytest.mark.parametrize("nombre, esperado", [
    ('DaNIeL LUga', 'Daniel Luga'),
    ('Miguel ÁnGel', 'Miguel Ángel'),
    ('Rosa-María', 'Rosa María'),
    ('Antonio Manuel..', 'Antonio Manuel')
    ('', '')
])

def test_normaliza_nombres_mayusculas_minusculas(valor, esperado):
    assert normaliza_nombre(valor) == esperado

def test_normaliza_nombre_(): 