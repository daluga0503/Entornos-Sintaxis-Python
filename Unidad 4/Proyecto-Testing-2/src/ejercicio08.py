import re

def es_palindromo(texto):
    """Comprueba si un texto es palíndromo.

    Requisitos:
    - Recibe un string.
    - Considera solo letras y números.
    - No distingue mayúsculas/minúsculas.
    - Devuelve `True` si es palíndromo, `False` si no.
    """
    if not isinstance(texto, str):
        raise TypeError("texto debe ser str")

    limpio = "".join(ch for ch in texto.casefold() if ch.isalnum())
    return limpio == limpio[::-1]