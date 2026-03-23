def es_estrictamente_creciente(nums):
    """Comprueba si la lista es estrictamente creciente.

    Requisitos:
    - Recibe una lista de números.
    - Devuelve True si cada elemento es estrictamente mayor que el anterior.
    - Lista vacía o de un elemento devuelve True.
    """
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True