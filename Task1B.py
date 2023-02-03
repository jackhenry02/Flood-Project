from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def run():
    """Requirements for Task 1B"""
    p=(52.2053, 0.1218) #Coordinates of Cambridge
    stations=build_station_list()  #makes list of stations
    station_distances=stations_by_distance(stations,p)  #list of stations with sorted distances. NB stations is an object with data behind it
    output_list=[]
    for stationTuple in station_distances:
        output_list.append((stationTuple[0].name,stationTuple[0].town,stationTuple[1])) #makes list of tuples(name,town,distance)

    print(output_list[:10])

    print(output_list[-10:])


    


if __name__ == "__main__":        
    print("*** Task 1B: CUED Part IA Flood Warning System ***")  
    run()