def parsear_csv(texto):
    """Parsea un CSV simple sin comillas.

    Requisitos:
    - Recibe un string con filas separadas por `\n`.
    - La primera fila es cabecera con nombres de columnas separados por comas.
    - Devuelve una lista de diccionarios (uno por fila) mapeando cabecera->valor (string).
    - Debe ignorar líneas vacías.
    - Si una fila tiene distinto número de campos que la cabecera, debe lanzar `ValueError`.
    """
    lineas = [l for l in texto.split("\n") if l]
    cab = lineas[0].split(",")
    datos = []
    for l in lineas[1:]:
        campos = l.split(",")
        if len(campos) != len(cab):
            continue
        datos.append(dict(zip(cab, campos)))
    return datos
