import os
def CrearMenu():
    lstOpciones = ['A','B','C','D','E','F']
    opciones = '        A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO\n        B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE\n        C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO\n        D. TOTAL DE GOLES ANOTADOS POR TODOS LOS EQUIPOS\n        E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO\n        F. VOLVER AL MENÚ'
    os.system('cls')
    titulo = """
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
        ║                                            ║
        ║  L I G A B E T P L A Y    R E P O R T E S  ║
        ║                                            ║
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
    """
    print(f'{titulo}\n{opciones}')
    try:
        op = input('        -> ').upper()
        if op not in lstOpciones:
            CrearMenu()
    except:
        os.system('cls')
        print('Error en la opcion')
        os.system('pause')
        CrearMenu()
    else:
        return op
