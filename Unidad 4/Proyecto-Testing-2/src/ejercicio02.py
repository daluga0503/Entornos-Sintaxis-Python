TABLA = "TRWAGMYFPDXBNJZSQVHLCKE"

def validar_nif(nif):
    """Valida un NIF español (8 dígitos + letra).

    Requisitos:
    - Recibe un NIF como string: 8 dígitos + letra.
    - Acepta minúsculas o mayúsculas en la letra.
    - Ignora espacios al inicio y fin.
    - Devuelve `True` si el NIF es válido según la letra de control, `False` en caso contrario.
    - Si el formato no es correcto, devuelve `False` (no lanza excepciones).
    """
    nif = nif.strip()
    if len(nif) != 9:
        return False
    numero, letra = nif[:8], nif[8]
    if not numero.isdigit():
        return False
    idx = int(numero) % 23
    return TABLA[idx] == letra
