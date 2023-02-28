"""This module contains a function to sort levels by relative water levels over a tolerance"""

from .station import *
from .utils import *

def stations_level_over_threshold(stations, tol):
    '''returns tuples of station and relative water level'''
    floodlist = []
    for item in stations:
        if MonitoringStation.relative_water_level(item) == None:
            pass
        elif MonitoringStation.relative_water_level(item) > tol:
            floodlist.append((item,MonitoringStation.relative_water_level(item)))
    return sorted_by_key(floodlist, 1, True)


def stations_highest_rel_level(stations, N):
    """Function that returns a list of N stations at which the water level, relative to the typical range is the highest"""
    output_list = []
    stations_highest_risk = []

    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            pass
        else:
            output_list.append((station, MonitoringStation.relative_water_level(station)))
    output_list.sort(key=lambda x: x[1], reverse=True)

    if output_list == []:
        return None
    else:
        for i in range(N):
            stations_highest_risk.append(output_list[i])

        return stations_highest_risk