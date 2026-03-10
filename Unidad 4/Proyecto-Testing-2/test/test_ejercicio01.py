from ejercicio01 import normaliza_nombre
import pytest


# para ejecutar el test debes estar en la raíz del directorio test y ejecutar este coimando: pytest test_ejercicio01.py
@pytest.mark.parametrize("nombre, esperado", [
    ('DaNIeL LUga', 'Daniel Luga'),
    ('Miguel ÁnGel ', 'Miguel Ángel'),
    (' rosa maría', 'Rosa María'),
    ('Antonio  MANUEL', 'Antonio Manuel'),
])
def test_normaliza_nombres_mayusculas_minusculas_espacios(nombre, esperado):
    assert normaliza_nombre(nombre) == esperado

def test_normaliza_nombres_guines_entre_palabras():
    assert normaliza_nombre('Ana-María Quintero') == 'Ana-María Quintero'


@pytest.mark.parametrize("valor", [
    10,
    10.0,
    True,
    None
])
def test_normalize_nombres_entrada_diferente_str(valor):
    with pytest.raises(TypeError):
        normaliza_nombre(valor)

