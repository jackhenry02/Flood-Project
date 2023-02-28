from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import *
import datetime
from floodsystem.geo import *
from floodsystem.station import *
from floodsystem.flood import *
from floodsystem.analysis import *

'''
possible criteria:
- tolerance
    - different tolerances for different risk
    - 0.8 - 0.9 Low
    - 0.9 - 1.0 Moderate
    - 1.0 - 1.1 High
    - 1.1+ Severe
- negative or positive poly function?
    - falling at a certain rate decreases risk by 1
    - rising at a certain rate increases risk by 1
    - use difference in last few hours instead
- 
'''

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    tol_list = stations_level_over_threshold(stations, 0.8) #any station with a relative level below 0.8 regarded as no risk
    
    #tolerance checking
    severe_list = []
    high_list = []
    moderate_list = []
    low_list = []
    for item in tol_list:
        dates, levels = fetch_measure_levels(item[0].measure_id, datetime.timedelta(days=1))
        adj = (item[1]-(((levels[len(levels)//2])-(item[0].typical_range[0]))/(item[0].typical_range[1]-item[0].typical_range[0])))/2    #adjustment taking into account the change in level in the last 12 hours
        if (item[1]+adj) > 1.4:                                   #adjusted tolerance over 1.4 is severe
            severe_list.append(item)    
        elif (item[1]+adj) > 1.2:                                 #adjusted tolerance of 1.2 to 1.4 is high
            high_list.append(item)
        elif (item[1]+adj) > 1.0:                                 #adjusted tolerance of 1.0 to 1.2 is moderate
            moderate_list.append(item)
        elif (item[1]+adj) > 0.8:
            low_list.append(item)                           #adjusted tolerance of 0.8 to 1.0 is low

    print("Severe Risk:")
    for item in severe_list: 
        dates, levels = fetch_measure_levels(item[0].measure_id, datetime.timedelta(days=1))
        print(item[0].name,";","rel.lvl. is", item[1],";", "rel.rise in last 12 hours is", (item[1]-(((levels[len(levels)//2])-(item[0].typical_range[0]))/(item[0].typical_range[1]-item[0].typical_range[0]))))
    print()
    print("High Risk:")
    for item in high_list: 
        dates, levels = fetch_measure_levels(item[0].measure_id, datetime.timedelta(days=1))
        print(item[0].name,";","rel.lvl. is", item[1],";", "rel.rise in last 12 hours is", (item[1]-(((levels[len(levels)//2])-(item[0].typical_range[0]))/(item[0].typical_range[1]-item[0].typical_range[0]))))
    print()
    print("Moderate Risk:")
    for item in moderate_list: 
        dates, levels = fetch_measure_levels(item[0].measure_id, datetime.timedelta(days=1))
        print(item[0].name,";","rel.lvl. is", item[1],";", "rel.rise in last 12 hours is", (item[1]-(((levels[len(levels)//2])-(item[0].typical_range[0]))/(item[0].typical_range[1]-item[0].typical_range[0]))))
    print()
    print("Low Risk:")
    for item in low_list: 
        dates, levels = fetch_measure_levels(item[0].measure_id, datetime.timedelta(days=1))
        print(item[0].name,";","rel.lvl. is", item[1],";", "rel.rise in last 12 hours is", (item[1]-(((levels[len(levels)//2])-(item[0].typical_range[0]))/(item[0].typical_range[1]-item[0].typical_range[0]))))
'''
    

    for item in tol_list:
        item = item[0]
        dates, levels = fetch_measure_levels(item.measure_id, datetime.timedelta(days=1))
        print(MonitoringStation.relative_water_level(item),
              MonitoringStation.relative_water_level(item)-(((levels[len(levels)//2])-(item.typical_range[0]))/(item.typical_range[1]-item.typical_range[0])),
              MonitoringStation.relative_water_level(item)+(MonitoringStation.relative_water_level(item)-(((levels[len(levels)//2])-(item.typical_range[0]))/(item.typical_range[1]-item.typical_range[0])))/2)
'''
#(self.latest_level)-(self.typical_range[0]))/(self.typical_range[1]-self.typical_range[0])

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()


#to run pytest: python3 -m pytest