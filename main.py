import modulos.menu as mp
import modulos.menuReportes as mr
import modulos.equipos as e
import modulos.fechas as fg
import modulos.reportes as rp

if __name__ == '__main__':
    equiposLiga = {}
    fechas = {}
    isAppRunning = True
    while isAppRunning:
        op=mp.CrearMenu()
        if (op ==1):
            isAddTeam = True
            while isAddTeam:
                e.os.system('cls')
                e.AddTeam(equiposLiga)
                isAddTeam = bool(input('        Desea agregar otro Equipo S(Si) o Enter(No)\n        -> '))
        elif (op ==2):
            e.ViewTeams(equiposLiga)
        elif (op ==3):
            fg.AddGame(equiposLiga, fechas)
        elif (op ==4):
            isReport = True
            while isReport:
                optionMenuRep = mr.CrearMenu()
                if optionMenuRep == 'A': #Equipo goleador #! YA
                    eqMaxGoles, eqMaxGolesName = rp.ObtenerEqMaxGoles(equiposLiga)
                    print(f'El equipo con más goles es: {eqMaxGolesName} con: {eqMaxGoles} goles')
                    print('Enter para ir al menu de reportes')
                    rp.os.system('pause')
                elif optionMenuRep == 'B': #Equipo con mas puntos #! YA
                    maxPunts, nameMaxPunts = rp.ObtenerEqMaxPuntos(equiposLiga)
                    print(f'El equipo con más puntos es: {nameMaxPunts} con: {maxPunts} puntos')
                    print('Enter para ir al menu de reportes')
                    rp.os.system('pause')
                elif optionMenuRep == 'C': #Equipo mas ganador de partidos #! YA
                    maxParts, nameMaxParts = rp.ObtenerEqMaxParts(equiposLiga)
                    print(f'El equipo con más partidos ganados es: {nameMaxParts} con: {maxParts} partidos')
                    print('Enter para ir al menu de reportes')
                    rp.os.system('pause')
                elif optionMenuRep == 'D': #Total de goles #! YA
                    totalGoles = rp.ObtenerTotalGoles(equiposLiga)
                    print(f'El total de todos los goles es: {totalGoles}')
                    print('Enter para ir al menu de reportes')
                    rp.os.system('pause')
                elif optionMenuRep == 'E': #Promedio de goles #! YA
                    promGoles = rp.ObtenerPromedioGoles(equiposLiga)
                    print(f'El total de partidos es: {promGoles}')
                    print('Enter para ir al menu de reportes')
                    rp.os.system('pause')
                elif (optionMenuRep == 'F'):
                    isReport = False
        elif (op ==5):
            isAppRunning=False