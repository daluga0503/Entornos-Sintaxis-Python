from ejercicio11 import es_password_segura
import pytest

def test_es_password_segura_vacio():
    assert es_password_segura('') == False

@pytest.mark.parametrize("entrada, esperado", [
    ("12345678910", False),
    ("abcdefghijk", False),
    ("ABCDEFGHIJK", False),
    ('password123', False),
    ('Hola12', False),
    ('Password123', True),
    ("Contraseña@123_", True)
])
def test_es_password_segura_correcto(entrada, esperado):
    assert es_password_segura(entrada) == esperado