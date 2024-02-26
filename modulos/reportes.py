import os

def ObtenerTotalGoles(lstEquipos: dict):
    totalGoles = 0
    for equipos in lstEquipos:
        totalGoles = (lstEquipos[equipos]['GF']) + (lstEquipos[equipos]['GC'])
        # totalGoles += (equipos[5] + equipos[6]) / 2
    return totalGoles

def ObtenerTotalPartidos(lstEquipos: dict):
    totalPartidos = 0
    for equipos in lstEquipos:
        totalPartidos = (lstEquipos[equipos]['PJ'])
    return totalPartidos

def ObtenerPromedioGoles(lstEquipos: dict):
        totalGoles = ObtenerTotalGoles(lstEquipos)
        totalPartidos = ObtenerTotalPartidos(lstEquipos)

        return (totalGoles / totalPartidos)