from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import *
from floodsystem.station import *
from floodsystem.flood import *


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    tol_list = stations_level_over_threshold(stations, 0.8)
    for item in tol_list:
        print(item[0].name,item[1])



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()