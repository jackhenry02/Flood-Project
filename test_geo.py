from haversine import haversine
from floodsystem.geo import *
from floodsystem.station import MonitoringStation


# Creating a test station list
coord = (-2.0, 4.0)
stations = [
    MonitoringStation('s_id1', 'm_id1', 'label1', (-2.0,4.0), (0.0073, 0.14), 'river1', 'town1'),
    MonitoringStation('s_id2', 'm_id2', 'label2', (3.0,2.0), (1.12, 1.12), 'river2', 'town2'),
    MonitoringStation('s_id3', 'm_id3', 'label3', (1.6,-1.6), (24.94, 7.51), 'river2', 'town3'),
    MonitoringStation('s_id4', 'm_id4', 'label4', (0.1,0.1), None, 'river3', 'town4'),
    MonitoringStation('s_id5', 'm_id5', 'label5', (0.1,0), (9.04, 11.68), 'river3', 'town5')
]


def test_stations_by_distance():
    output = stations_by_distance(stations,(0,0))
    #using haversine
    output_list = []
    for i in range(len(stations)):
        output_list.append((stations[len(stations) - (i + 1)], haversine(stations[len(stations) - (i + 1)].coord, (0,0))))
    assert output == output_list                        #checks value and order
    assert type(output) == list                          #checks type
    assert len(output) == len(stations)                 #checks length
    # Note for future tests: d1,d2,d3,d4,d5 = 497.19868760742435, 400.8631781687255, 251.58939201339484, 15.725355061691959, 11.11950802335329

def test_stations_within_radius():
    output = stations_within_radius(stations,(0,0),260)
    d3 = haversine (stations[2].coord, (0,0))
    d4 = haversine (stations[3].coord, (0,0))
    d5 = haversine (stations[4].coord, (0,0))

    assert output == [stations[4],stations[3],stations[2]]    #checks correct output
    assert type(output) == list         #checks type
    assert len(output) == 3             #checks length 

def test_rivers_with_station():
    output = rivers_with_station(stations)
    assert output == {'river1','river2','river3'}       #checks correct output
    assert type(output) == set                          #checks type
    assert len(output) == 3                             #checks length (should ommitt duplicate)

def test_stations_by_river():
    output = stations_by_river(stations)
    assert output == {'river1':['label1'],'river2':['label2','label3'],'river3':['label4','label5']}      #checks correct output
    assert type(output) == dict                                                                  #checks type
    assert len(output) == 3                                                                      #checks length

def test_rivers_by_station_number():
    """Assert that the function works correctly, especially the case when the number of stations on a set of rivers are equal"""
    
    rivers = rivers_by_station_number(stations, 1)

    assert rivers == [('river2', 2), ('river3', 2)]     # Expected output
    assert type(rivers) == list
    assert len(rivers) == 2
