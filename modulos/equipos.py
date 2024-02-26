import os
from tabulate import tabulate

equipo = {}

def AddTeam(lstEquipos : dict):
    nombre = input('        Ingrese el nombre del Equipo:\n        -> ')
    equipo = {
        'nombre': nombre.capitalize(),
        'PJ': 0,
        'PG': 0,
        'PP': 0,
        'PE': 0,
        'GF': 0,
        'GC': 0,
        'PT': 0,
    }

    lstEquipos.update({(nombre).capitalize():equipo})
    
def DelTeam(lstEquipos : dict):
    palabra = input('        Ingrese nombre del equipo a borrar')
    for idx,item in enumerate(lstEquipos):
        if (palabra in item):
            lstEquipos.pop(idx)
            break

def ViewTeams(lstEquipos: dict):

    os.system('cls')
    titulo = """
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
        ║                                      ║
        ║  L I G A B E T P L A Y    T A B L A  ║
        ║                                      ║
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
    """
    print(titulo)

    info = []
    for key, value in lstEquipos.items(): #? .items() para desestructurar (enumerate)
        info.append(value)
    print(tabulate(info, headers="keys", tablefmt='grid'))      
    os.system('pause')