def mezclar(a, b):
    """Combina dos diccionarios, prevalece b.

    Requisitos:
    - Recibe dos diccionarios.
    - Devuelve un nuevo diccionario con todas las claves, donde en caso de conflicto gana el de la derecha.
    - No debe modificar los originales.
    """
    res = a
    res.update(b)
    return res
