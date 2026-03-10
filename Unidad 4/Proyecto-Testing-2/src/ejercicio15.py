def resumen(texto, n):
    """Genera un resumen de longitud n.

    Requisitos:
    - Recibe un texto (str) y un máximo de caracteres `n` (int > 0).
    - Si el texto cabe, devuelve el texto tal cual.
    - Si no cabe, devuelve los primeros `n-1` caracteres y añade '…' (U+2026).
    """
    if n <= 0:
        raise ValueError("n inválido")
    if len(texto) <= n:
        return texto
    return texto[:n] + "…"
