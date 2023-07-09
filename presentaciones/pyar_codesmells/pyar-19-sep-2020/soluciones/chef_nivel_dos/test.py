from .solucion import CocinarHuevos

esperado = '''La orden 1 es de 1 huevo 🥚
La orden 2 es de 2 huevos 🍳
El total a pagar es 0.5 pesos.
'''

def test_CocinarHuevos(capsys):
    CocinarHuevos().ejecutar()
    captured = capsys.readouterr()
    assert captured.out == esperado