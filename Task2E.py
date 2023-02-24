
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime

def run():
    """Requirements for Task 2E"""
    stations=build_station_list()  # Makes list of stations
    
    
    dates, levels = fetch_measure_levels(stations[0].measure_id, datetime.timedelta(days=10))
    
    plot_water_levels(stations[0], dates, levels)
    




if __name__ == "__main__":       
    print("*** Task 2E: CUED Part IA Flood Warning System ***")  
    run()