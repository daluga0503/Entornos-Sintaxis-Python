from src.ejercicio08 import es_palindromo
import pytest

@pytest.mark.parametrize("entrada, esperado",
    ("ala", True),
    ("radar", True),
    ('balón', False),
    ('manzana', False),
    (12344321, True),
    (123, False),
)
def test_es_palindromo(entrada, esperado):
     assert es_palindromo(entrada) == esperado

@pytest.mark.parametrize("entrada, esperado",
    ("1ala1", True),
    ("12ra22dar12", True),
    ('12balón23', False),
    ('12manzana12', False)
)
def test_es_palindromo_mezcla_str_int(entrada, esperado):
     assert es_palindromo(entrada) == esperado


@pytest.mark.parametrize("entrada, esperado",
    ("AlA", True),
    ("RadaR", True),
    ('Ana', False),
    ('Abba', False),
    ('ReConoCeR', True),
    ('ABBA', True),
    ('AbBa', False)
)
def test_es_palindromo_mayusculas_minusculas(entrada, esperado):
     assert es_palindromo(entrada) == esperado

def test_palindromo_con_espacios_y_simbolos():
    assert es_palindromo("Anita lava la tina") == True
    assert es_palindromo("123...21") == True

@pytest.mark.parametrize("entrada, esperado",
    ("A", True),
    ("Z", True),
    (1, True),
    (2, True),
)
def test_es_palindromo_solo_un_caracter(entrada, esperado):
     assert es_palindromo(entrada) == esperado

def test_es_palindromo_cadena_vacia():
     assert es_palindromo("") == True

def test_es_palindromo_cadena_vacia_espacios():
     assert es_palindromo("    ") == True


