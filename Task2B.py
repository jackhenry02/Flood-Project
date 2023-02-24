from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import *
from floodsystem.station import *

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print station and latest level for first 5 stations in list
    
    for item in stations:
        MonitoringStation.relative_water_level(item)





if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()