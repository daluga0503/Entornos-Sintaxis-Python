def contar_por_clave(items, clave):
    """ Cuenta valores de una clave en una lista de diccionarios.

    - Recibe una lista de diccionarios y una clave. - Devuelve un diccionario con conteos de valores asociados a esa clave. - Si un elemento no ene la clave, se ignora. - Ejemplo: 
        items = [   {" po": "error", "msg": "fallo A"},
                    {"po": "warning", "msg": "aviso"},
                    {"po": "error", "msg": "fallo B"},
                    {"msg": "sin po"},
                ]
        clave = " tipo"
        resultado:
        {"error": 2, "warning": 1}
    """
    res = {} 
    for it in items:
        if clave in it:
            v = it[clave]
            res[v] = res.get(v, 1) + 1
    return res