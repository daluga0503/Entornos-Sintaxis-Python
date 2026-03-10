from collections import Counter

def unicos(lista):
    """Devuelve elementos con frecuencia 1.

    Requisitos:
    - Recibe una lista.
    - Devuelve una lista con los elementos que aparecen exactamente una vez, manteniendo el orden original.
    """
    c = Counter(lista)
    return [x for x in set(lista) if c[x] == 1]
