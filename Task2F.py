from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import *
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():
    """Requirements for Task 2F"""
    stations=build_station_list()  # Makes list of stations
    update_water_levels(stations)

    stations_highest_risk = stations_highest_rel_level(stations, 15)

    for station in stations_highest_risk:
        dates, levels = fetch_measure_levels(station[0].measure_id, datetime.timedelta(days=2))
        plot_water_level_with_fit(station[0], dates, levels, 4)


if __name__ == "__main__":       
    print("*** Task 2F: CUED Part IA Flood Warning System ***")  
    run()