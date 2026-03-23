from ejercicio10 import contar_por_clave
import pytest

def test_contar_por_clave_vacio():
    assert contar_por_clave({}) == {}

items1 = [ 
    {"tipo": "error", "msg": "fallo A"},
    {"tipo": "warning", "msg": "aviso"},
    {"tipo": "error", "msg": "fallo B"},
    {"tipo": "warning", "msg": "aviso"},
]

result_items_1 = {"error": 2, "warning": 2}

items2 = [
    {"tipo": "error", "msg": "fallo A"},
    {"tipo": "warning", "msg": "aviso"},
    {"tipo": "error", "msg": "fallo B"},
    {"msg": "sin tipo"},
]

result_items_2 = {"error": 2, "warning": 1}

items3 = [
    {"tipo": "error", "msg": "fallo A"},
    {"tipo": "warning", "msg": "aviso"},
    {"tipo": "error", "msg": "fallo B"},
    {"tipo": "vulnerabilidad", "msg": "cuiadado"},
    {"tipo": "vulnerabilidad"},
]

result_items_3 = {"error": 2, "warning": 1, "vulnerabilidad": 2}


def test_contar_por_clave_correcto():
    assert contar_por_clave({}, 'tipo') == {}

@pytest.mark.parametrize("entrada, esperado", [
    (items1, result_items_1),
    (items2, result_items_2),
    (items3, result_items_3)
])
def test_contar_por_clave(entrada, esperado):
    assert contar_por_clave(entrada, 'tipo') == esperado