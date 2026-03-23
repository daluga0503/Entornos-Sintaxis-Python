def dominio_email(email):
    """Devuelve el dominio de un email.

    Requisitos:
    - Recibe un email (str).
    - Devuelve el dominio (parte tras '@') en minúsculas.
    - Si no tiene '@' o el dominio está vacío, lanza `ValueError`.
    """
    partes = email.split("@")
    if len(partes) != 2:
        raise ValueError("email inválido")
    return partes[0].lower()
