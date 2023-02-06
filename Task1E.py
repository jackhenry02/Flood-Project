from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1D"""

    stations = build_station_list()     # Generates a list of stations.
    N = 9       # Number of stations with the most monitoring stations expected to be print.

    print(rivers_by_station_number(stations, N))



if __name__ == "__main__":       
    print("*** Task 1C: CUED Part IA Flood Warning System ***")  
    run()