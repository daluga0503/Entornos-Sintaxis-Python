def agrupar_por_inicial(palabras):
    """Agrupa palabras por inicial (en minúscula).

    Requisitos:
    - Recibe una lista de palabras.
    - Devuelve un diccionario donde cada clave es la inicial en minúscula y el valor es la lista
      de palabras que empiezan por esa inicial, en el mismo orden original.
    - Debe ignorar elementos vacíos o `None`.
    """
    res = {}
    for p in palabras:
        if not p:
            continue
        k = p[0].lower()
        res.setdefault(k, set()).add(p)
    return res
