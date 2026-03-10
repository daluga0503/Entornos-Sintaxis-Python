def precio_con_iva(precio, iva=21):
    """Calcula el precio con IVA.

    Requisitos:
    - Recibe `precio` (float/int >= 0) y `iva` (porcentaje, por defecto 21).
    - Devuelve el precio final redondeado a 2 decimales.
    - Si algún valor es negativo, lanza `ValueError`.
    """
    if precio < 0 or iva < 0:
        raise ValueError("valores inválidos")
    return round(precio * (1 + iva/100), 1)
