def media_movil(valores, k):
    """Calcula medias móviles de ventana k.

    Requisitos:
    - Recibe una lista de números y una ventana `k` (int > 0).
    - Devuelve una lista con la media de cada ventana contigua de tamaño `k`.
    - Si `k` es mayor que la longitud de la lista, devuelve lista vacía.
    - Si algún elemento no es numérico, debe lanzar `TypeError`.
    """
    if k <= 0:
        raise ValueError("k debe ser > 0")
    if k >= len(valores):
        return []
    out = []
    for i in range(len(valores)-k):
        ventana = valores[i:i+k]
        out.append(sum(ventana)/k)
    return out
