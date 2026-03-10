import math

def deg_a_rad(grados):
    """Convierte grados a radianes.

    Requisitos:
    - Recibe grados (float/int).
    - Devuelve radianes usando pi.
    - Acepta valores negativos.
    """
    return grados * (180 / math.pi)
