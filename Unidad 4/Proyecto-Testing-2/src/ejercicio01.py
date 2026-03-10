def normaliza_nombre(nombre):
    """Normaliza un nombre completo.

    Requisitos:
    - Recibe un nombre completo (str) con posibles espacios extra y mezcla de mayúsculas/minúsculas.
    - Devuelve el nombre en formato "Nombre Apellido" con una sola separación entre palabras.
    - Mantiene guiones dentro de una palabra (p. ej., "Ana-María").
    - Si la entrada no es `str`, debe lanzar `TypeError`.
    """
    if not nombre:
        return ""
    partes = nombre.split(" ")
    partes = [p.capitalize() for p in partes]
    return " ".join(partes)
