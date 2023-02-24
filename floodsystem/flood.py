"""This module contains a function to sort levels by relative water levels over a tolerance"""

from .station import *
from .utils import *

def stations_level_over_threshold(stations, tol):
    floodlist = []
    for item in stations:
        if MonitoringStation.relative_water_level(item) == None:
            pass
        elif MonitoringStation.relative_water_level(item) > tol:
            floodlist.append((item,MonitoringStation.relative_water_level(item)))
    return sorted_by_key(floodlist, 1, True)
        

