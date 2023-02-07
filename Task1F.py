from floodsystem.stationdata import build_station_list
from floodsystem.station import *
from floodsystem.geo import *

def run():
    """Builds and prints a list of all the stations with inconsistent typical range data."""

    stations = build_station_list()     # Generates a list of stations.
    output_list =[]

    inconsistent_stations = inconsistent_typical_range_stations(stations)       # Generates a list of stations with inconsistent typical range data.

    for station in inconsistent_stations:
        output_list.append(station.name)

    print(sorted(output_list))



if __name__ == "__main__":       
    print("*** Task 1C: CUED Part IA Flood Warning System ***")  
    run()