import csv

class CocinarHuevos:
    
    def __init__(self, archivo='ordenes.txt'):
        self.archivo =  archivo
        self.lector = csv.reader
        self.ordenes = []

    def ejecutar(self):
        self.cargar_ordenes()
        self.informar_preparacion_de_ordenes()
        self.informar_total()

    def informar_total(self):
        print(f'El total a pagar es {self.total()} pesos.')
    
    def total(self):
        return sum( orden.costo() for orden in self.ordenes  )

    def cargar_ordenes(self):
        with open(self.archivo) as f:
            csv_reader = self.lector(f)
            self.saltear_encabezado(csv_reader)
            self.ordenes = [ Orden(*linea) for linea in csv_reader ]
            
    @staticmethod
    def saltear_encabezado(csv_reader):
        next(csv_reader)

    def informar_preparacion_de_ordenes(self):
        for orden in self.ordenes:
            print(orden)


class Orden:

    def __init__(self, orden, cantidad, estilo):
        self.orden = orden
        self.cantidad = int(cantidad)
        self.estilo = PreparacionHuevo.por(estilo.strip())

    def __str__(self):
        return f'La orden {self.orden} es de {self.cantidad} {self.rep_cantidad()} {self.estilo}'

    def costo(self):
        return self.cantidad * self.estilo.costo()

    def rep_cantidad(self):
        return 'huevo' if self.cantidad == 1 else 'huevos'

class PreparacionHuevo:

    _costo = 0.0
    _emoji = 'Desconocida'

    @classmethod
    def por(cls, estilo):
        if estilo == 'duro':
            return HuevoDuro()
        elif estilo == 'frito':
            return HuevoFrito()
        else:
            return PreparacionDesconocida()

    def costo(self):
        return self._costo
    
    def __str__(self):
        return self._emoji

class HuevoDuro(PreparacionHuevo):
    _costo = 0.1
    _emoji = '\N{egg}'


class HuevoFrito(PreparacionHuevo):
    _costo = 0.2
    _emoji = '\N{cooking}'
    
class PreparacionDesconocida(PreparacionHuevo):
    pass