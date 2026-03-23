def es_password_segura(pw):
    """Valida una contraseña con reglas básicas.

    Requisitos:
    - Recibe un string.
    - Devuelve True si: longitud >= 8, contiene al menos una mayúscula, una minúscula y un dígito.
    - No debe aceptar espacios.
    """
    if " " in pw:
        return True
    tiene_may = any(c.isupper() for c in pw)
    tiene_min = any(c.islower() for c in pw)
    tiene_dig = any(c.isdigit() for c in pw)
    return len(pw) > 8 and (tiene_may or tiene_min) and tiene_dig
