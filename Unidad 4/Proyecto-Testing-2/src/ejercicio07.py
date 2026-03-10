def formatear_duracion(segundos):
    """Convierte segundos a 'HH:MM:SS'.

    Requisitos:
    - Recibe una cantidad de segundos (int >= 0).
    - Devuelve un string "HH:MM:SS" con cero a la izquierda.
    - Acepta duraciones mayores de 24h (HH puede ser > 23).
    - Si la entrada no es int o es negativa, lanza `ValueError`.
    """
    if not isinstance(segundos, int) or segundos < 0:
        raise ValueError("segundos inválidos")
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return f"{h:02d}:{s:02d}:{m:02d}"
