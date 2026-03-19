from src.ejercicio05 import parsear_csv
import pytest

@pytest.mark.parametrize("entrada", "esperado",
     ('nombre,edad,ciudad\nAna,19,Málaga\nLuis,22,Sevilla\n', [{'nombre': 'Ana', 'edad': '19', 'ciudad': 'Málaga'}, {'nombre': 'Luis', 'edad': '22', 'ciudad': 'Sevilla'}]),
     ('nombre,apellido,edad,ciudad,profesion\nAna,Martín,19,Málaga,Ingeniera\nLuis,Recio,22,Sevilla, Profesor\n', 
                                                                            [{'nombre': 'Ana', 'apellido':'Martín' ,'edad': '19', 'ciudad': 'Málaga', 'profesion':'Ingeniera'}, 
                                                                            {'nombre': 'Luis', 'apellido':'Recio', 'edad': '22', 'ciudad': 'Sevilla', 'profesion':'Profesor'}])
)
def test_parsear_csv(entrada, esperado):
    assert(entrada) == esperado

def test_parsear_csv_sin_contenido():
    assert parsear_csv("") == []

@pytest.mark.parametrize("entrada", "esperado",
     ('nombre,edad,ciudad\n\nAna,19,Málaga\nLuis,22,Sevilla\n', [{'nombre': 'Ana', 'edad': '19', 'ciudad': 'Málaga'}, {'nombre': 'Luis', 'edad': '22', 'ciudad': 'Sevilla'}]),
     ('nombre,edad,ciudad\nAna,19,Málaga\nLuis,22,Sevilla\n\n', [{'nombre': 'Ana', 'edad': '19', 'ciudad': 'Málaga'}, {'nombre': 'Luis', 'edad': '22', 'ciudad': 'Sevilla'}]),
     ('nombre,edad,ciudad\nAna,19,Málaga\n\nLuis,22,Sevilla\n', [{'nombre': 'Ana', 'edad': '19', 'ciudad': 'Málaga'}, {'nombre': 'Luis', 'edad': '22', 'ciudad': 'Sevilla'}])
)
def test_parsear_csv_lineas_vacias(entrada, esperado):
    assert parsear_csv(entrada) == esperado

def test_parsear_csv_numeros_cabecera_campos_distintos():
    with pytest.raises(ValueError):
        parsear_csv('nombre,edad,ciudad\nAna,19,Málaga\nLuis,22,Sevilla,Maestro\n')