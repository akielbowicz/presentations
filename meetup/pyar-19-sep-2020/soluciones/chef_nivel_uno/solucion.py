precios = (1.0, 1.2) # Precios : ( duro, frito )

def ejecutar():
    'Cocinar Huevos'
    
    #Cargar ordenes
    O = []
    try:
        with open('ordenes.txt','r') as f:
            i = 0
            for l in f:
#                 print(l)
                if i == 0:
                    i += 1
                    continue
                else:
#                     print(l)
#                     print(l[6:])
                    if (l[6:] == 'duro') or (l[6:] == 'duro\n'):
                        print(f'{l[0]} pidio {l[3]} huevo {l[6:]}')
                        O.append( ('duro', int(l[3]) ) )
                    elif (l[6:] == 'frito') or (l[6:] == 'frito\n'):
                        print(f'{l[0]} pidio {l[3]} huevo {l[6:]}')
                        O.append( ('frito', int(l[3])) )
                i += 1
    except:
        print('No se pudieron cargar las ordenes. Ahhh!!')
#     print(O)
    
    # Calcular total
    t = 0
    for i in O:
        if i[0] == 'duro':
            t += precios[0]*i[1]
        else:
            t += precios[1]*i[1]
            
    print(f'Total: {t}')


if __name__ == '__main__':
    ejecutar()