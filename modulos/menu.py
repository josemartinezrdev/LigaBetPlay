import os

def CrearMenu():
    lstOpciones = [1,2,3,4,5]
    titulo = """
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
        ║                                    ║
        ║  L I G A B E T P L A Y    M E N U  ║
        ║                                    ║
        🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙🝙
    """
    os.system('cls')
    print(titulo)
    try:
        opciones = "        1. Agregar equipo\n        2. Mostrar tabla\n        3. Registrar Fecha\n        4. Reportes\n        5. Salir"
        print(opciones)
        op =int(input('        -> '))
        if (op not in lstOpciones):
            CrearMenu()
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        CrearMenu()
    else:
        return op


    