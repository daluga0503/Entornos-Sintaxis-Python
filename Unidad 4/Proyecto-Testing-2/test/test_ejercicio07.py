from src.ejercicio07 import formatear_duracion
import pytest

@pytest.mark.parametrize("entrada", "esperado",
    (10, '00:00:20'),
    (121, '00:02:01'),
    (3600, '01:00:00'),
    (3721, '01:02:01')
)
def test_formatear_duracion(entrada, esperado):
    assert formatear_duracion(entrada) == esperado


def test_formatear_duracion_mayor_24h():
    assert formatear_duracion(90125) == '25:02:05' 

@pytest.mark.parametrize("entrada", "esperado", 
    ("Hola", ValueError),
    (-10, ValueError)                         
)
def test_formatear_duracion_valores_negativos_str(entrada, esperado):
    with pytest.raises(esperado):
        formatear_duracion(entrada)
