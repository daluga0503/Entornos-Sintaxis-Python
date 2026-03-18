from ejercicio03 import agrupar_por_inicial
import pytest

def test_agrupar_por_inicial_mantiene_orden_duplicados():
    entrada = ['perro', 'gato', 'zebra', 'caballo', 'colibrí', 'perro']
    esperado = {'p': ['perro', 'perro'], 'g':['gato'], 'z':['zebra'], 'c':['caballo', 'colibrí']}

    assert agrupar_por_inicial(entrada) == esperado

def test_agrupar_por_inicial_mayusculas_minusculas():
        entrada = ['Perro', 'gato', 'zebra', 'Caballo', 'colibrí', 'perro']
        esperado = {'p': ['Perro', 'perro'], 'g':['gato'], 'z':['zebra'], 'c':['Caballo', 'colibrí']}

        assert agrupar_por_inicial(entrada) == esperado

def test_agrupar_ignorar_vacios_nulos():
    entrada = ['gato', 'zebra', "", 'colibrí', 'perro', None]
    esperado = {'g':['gato'], 'z':['zebra'], 'c':['colibrí'], 'p': ['perro']}

    assert agrupar_por_inicial(entrada) == esperado








