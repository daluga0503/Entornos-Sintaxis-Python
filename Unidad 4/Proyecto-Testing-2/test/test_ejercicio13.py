from ejercicio13 import dominio_email
import pytest

"""Devuelve el dominio de un email.

    Requisitos:
    - Recibe un email (str).
    - Devuelve el dominio (parte tras '@') en minúsculas.
    - Si no tiene '@' o el dominio está vacío, lanza `ValueError`.
    """

@pytest.mark.parametrize("entrada, esperado", [
    ("prueba@gmail.com", "prueba@gmail.com"),
    ("Prueba@gmail.com", "prueba@gmail.com"),
    ("PRUEBA@gmail.com", "prueba@gmail.com"),
    ("PrUebA@gmail.com", "prueba@gmail.com")
])
def test_dominio_formato_correcto(entrada, esperado):
    assert dominio_email(entrada) == esperado

@pytest.mark.parametrize("entrada, esperado", [
    ("",ValueError),
    ("hola.com", ValueError),
    ("hola@", ValueError)

])
def test_dominio_email_formato_invalido(entrada, esperado):
    with pytest.raises(esperado):
        dominio_email(entrada)


@pytest.mark.parametrize("entrada, esperado", [
    (12,ValueError),
    (10.5, ValueError),
    (True, ValueError),
    ([], ValueError),
    ({}, ValueError),
    (None, ValueError)

])
def test_dominio_email_valor_entrada_incorrecto(entrada, esperado):
    assert dominio_email(entrada) == esperado