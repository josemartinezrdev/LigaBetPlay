import os

fecha = {}
def AddGame(lstEquipos:dict, lstFechas:dict, counter=1):
    msg = ''
    os.system('cls')
    titulo = """
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
        ║                                        ║
        ║  L I G A B E T P L A Y    F E C H A S  ║
        ║                                        ║
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
    """
    print(titulo)
    for idx, item in lstEquipos.items(): 
        print(f'        -> {idx}')

    if counter == 1:
        msg = '        Seleccione el Equipo Local'
        estado = 'L'
    else:
        msg = '        Seleccione el Equipo Visitante'
        estado = 'V'

    try:
        opcion = str(input(f'{msg}\n        -> '))

        if opcion.capitalize() not in lstEquipos:
            raise IndexError
        
        goles = int(input(f'        Ingrese los goles marcados por {opcion.capitalize()}\n        -> '))

    except ValueError:
        os.system('cls')
        print('El valor de goles debe ser numérico')
        os.system('pause')
        AddGame(lstEquipos, lstFechas)

    except IndexError:
        os.system('cls')
        print('Aun no has registrado este equipo, Enter para volver al menú')
        os.system('pause')
    
    else:

        fecha.update({opcion:{'nombre':opcion, 'goles':goles, 'estado':estado}})

        os.system('pause')
        counter += 1
        if counter <= 2:
            AddGame(lstEquipos, lstFechas, counter)
        else:

            equipoLocal = lstEquipos[fecha[opcion]['nombre'].capitalize()]

            equipoVisitante = lstEquipos[[k for k in lstEquipos.keys() if k != fecha[opcion]['nombre']][0]]

            golesEc = fecha[[k for k in fecha.keys() if k != opcion][0]]['goles']

            print(lstEquipos[fecha])
            
            equipoLocal['PJ'] += 1
            equipoLocal['GF'] += fecha[opcion]['goles']
            equipoLocal['GC'] += golesEc

            equipoVisitante['PJ'] += 1
            equipoVisitante['GF'] += golesEc
            equipoVisitante['GC'] += fecha[opcion]['goles']

            if fecha[opcion]['goles'] > golesEc:

                equipoLocal['PG'] += 1
                equipoLocal['PT'] += 3

            elif golesEc > fecha[opcion]['goles']:

                equipoVisitante['PG'] += 1
                equipoVisitante['PT'] += 3

            else:
                equipoLocal['PE'] += 1
                equipoVisitante['PE'] += 1
                
                equipoLocal['GF'] += fecha[opcion]['goles']
                equipoVisitante['GF'] += golesEc

                equipoLocal['GC'] += golesEc
                equipoVisitante['GC'] += fecha[opcion]['goles']

                equipoLocal['PT'] += 1
                equipoVisitante['PT'] += 1

            print(lstEquipos)
            print(fecha)
            print(equipoLocal)
            print(equipoVisitante)

            fechaVer(lstFechas)

def fechaVer(lstFechas):
    nroFecha = input('        Ingrese el número de fecha:\n        -> ')

    try:
        nroFecha = int(nroFecha)
    except ValueError:
        print("Error: El número de fecha debe ser un valor numérico.")
        os.system('pause')
        fechaVer(lstFechas)
        
    lstFechas[nroFecha] = fecha
    print(lstFechas)

    os.system('pause')