from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()     # Build list of stations

    update_water_levels(stations)      # Update latest level data for all stations
    number_of_stations = 10

    stations_highest_risk = stations_highest_rel_level(stations, number_of_stations)
    for station in stations_highest_risk:
        print(station[0].name,station[1])


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()