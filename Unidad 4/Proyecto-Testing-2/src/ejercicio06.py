def dist_manhattan(p1, p2):
    """Calcula la distancia Manhattan entre dos puntos 2D.

    Requisitos:
    - Recibe dos puntos (x, y) como tuplas/listas de longitud 2.
    - Devuelve |x1-x2| + |y1-y2|.
    - Si el formato no es correcto, debe lanzar `ValueError`.
    """
    if len(p1) != 2 or len(p2) != 2:
        raise ValueError("puntos inválidos")
    return abs(p1[0]-p2[0]) + abs(p1[0]-p2[1])
