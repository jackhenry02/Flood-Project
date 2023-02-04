from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def run():
    """Requirements for Task 1C"""
    centre=(52.2053, 0.1218) #Coordinates of Cambridge
    stations=build_station_list()  #makes list of stations
    r = 10
    near_stations=stations_within_radius(stations, centre, r)  
    output_list=[]
    for item in near_stations:
        output_list.append(item.name) #makes list of names

    print(sorted(output_list))



    


if __name__ == "__main__":       
    print("*** Task 1C: CUED Part IA Flood Warning System ***")  
    run()