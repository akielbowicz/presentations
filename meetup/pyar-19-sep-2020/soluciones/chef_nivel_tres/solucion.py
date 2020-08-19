import csv
from collections import Counter, namedtuple

Orden = namedtuple('Orden','orden cantidad estilo')

class CocinarHuevos:

    PRECIOS = { 'duro' : 0.1, 
                'frito': 0.2,
              }
    
    REPR = { 'duro'  : '\N{egg}',
             'frito' : '\N{cooking}',
           }
    
    @staticmethod
    def ejecutar(archivo='ordenes.txt'):
        with open(archivo) as f:
            csv_reader = csv.reader(f)
            ordenes = list(csv_reader)[1:]
            
            cuentas = Counter( row[2] for row in ordenes for _ in range(int(row[1].strip())) )
            total = sum( CocinarHuevos.PRECIOS.get(k.strip(),0)*v for k,v in cuentas.items()  )
            
            CocinarHuevos.informar(ordenes)
            print(f'El total a pagar es {total} pesos.')
            
    @staticmethod
    def informar(ordenes):
        for orden in ordenes:
            orden = Orden(*orden)
            x = ( f'huevo {CocinarHuevos.REPR.get(orden.estilo.strip())}'
                   if int(orden.cantidad.strip()) == 1 
                   else f'huevos {CocinarHuevos.REPR.get(orden.estilo.strip())}' )
            print(f'La orden {orden.orden} es de {orden.cantidad.strip()} {x}')