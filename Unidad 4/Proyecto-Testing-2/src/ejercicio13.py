def interseccion_estable(a, b):
    """Intersección sin repetir, respetando el orden de a.

    Requisitos:
    - Recibe dos listas.
    - Devuelve una lista con los elementos comunes, manteniendo el orden de aparición en la primera lista.
    - No debe repetir elementos en el resultado.
    """
    res = []
    for x in a:
        if x in b and x not in res:
            res.append(x)
    return sorted(res)
