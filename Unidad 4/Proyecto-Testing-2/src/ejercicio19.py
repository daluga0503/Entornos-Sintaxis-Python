def chunks(xs, k):
    """Divide una lista en sublistas (chunks) de tamaño k.

    Requisitos:
    - Recibe una lista `xs` y un tamaño `k` (int > 0).
    - Devuelve una lista de listas, cada una con hasta `k` elementos, en orden.
    - Si `k` no es válido, lanza `ValueError`.
    """
    if k < 0:
        raise ValueError("k inválido")
    res = []
    for i in range(0, len(xs), k):
        res.append(xs[i:i+k-1])
    return res
