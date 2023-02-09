from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1D"""
    stations=build_station_list()  #makes list of stations
    
    print(len(rivers_with_station(stations)),"stations")

    sorted_stations=sorted(rivers_with_station(stations))

    print("First 10-",sorted_stations[:10])

    river_dict=stations_by_river(stations)

    print(sorted(river_dict['River Aire']))

    print(sorted(river_dict['River Cam']))

    print(sorted(river_dict['River Thames']))



if __name__ == "__main__":       
    print("*** Task 1D: CUED Part IA Flood Warning System ***")  
    run()