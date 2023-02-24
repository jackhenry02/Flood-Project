
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime

def run():
    """Requirements for Task 2E"""
    stations=build_station_list()  # Makes list of stations
    update_water_levels(stations)
    number_of_stations = 5

    stations_highest_risk = stations_highest_rel_level(stations, number_of_stations)

    for station in stations_highest_risk:
        dates, levels = fetch_measure_levels(station[0].measure_id, datetime.timedelta(days=10))
        plot_water_levels(station[0], dates, levels)



if __name__ == "__main__":       
    print("*** Task 2E: CUED Part IA Flood Warning System ***")  
    run()