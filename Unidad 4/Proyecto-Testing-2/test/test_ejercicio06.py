from src.ejercicio06 import dist_manhattan
import pytest


# Recibe dos puntos (x, y) como tuplas/listas de longitud 2.
# Devuelve |x1-x2| + |y1-y2|.
# Ejemplo:
# p1 = [10, -2]
# p2 = [7, 5]
# dist_manhattan(p1, p2) -> |10-7| + |-2-5| = 3 + 7 = 10
# Si el formato no es correcto, debe lanzar `ValueError`.

@pytest.mark.parametrize("entrada1, entrada2, esperado", 
    ([10, -2], [7, 5], 10),
    ((10, -2), (7, 5), 10),
    ((10, -2), [7, 5], 10)
    ([0, 0], [0, 0], 0)
)
def test_dist_manhattan(entrada1, entrada2, esperado):
    assert dist_manhattan(entrada1, entrada2) == esperado

def test_dist_manhattan_formato_incorrecto():
    with pytest.raises(ValueError):
        dist_manhattan("", 0)