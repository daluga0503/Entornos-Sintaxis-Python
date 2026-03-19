from src.ejercicio04 import media_movil
import pytest

def test_media_movil_k_2():
    assert media_movil([1,2,3,4,5,6], 2) == [1.5, 2.5, 3.5, 4.5]

def test_media_movil_numero_suelto():
    assert media_movil([1,2,3,4,5,6,7], 2) == [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]

def test_media_movil_k_igual_lista():
    assert media_movil([1, 2, 3, 4], 4) == [2.5]

def test_media_movil_k_mayor_lista():
    assert media_movil([1, 2, 3, 4], 5) == []

def test_media_movil_k_0():
    with pytest.raises(ValueError):
        media_movil([1, 2, 3, 4], 0)

def test_media_movil_k_negativo():
    with pytest.raises(ValueError):
        media_movil([1, 2, 3, 4], -1)

def test_media_movil_valor_no_numerico():
    with pytest.raises(TypeError):
        media_movil([1, 2, 3, 4, 'a', 5, 6], 2)

