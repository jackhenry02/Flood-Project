from haversine import haversine
from floodsystem.geo import *
from floodsystem.station import MonitoringStation


# Creating a test station list
coord = (-2.0, 4.0)
s1 = MonitoringStation('s_id1', 'm_id1', 'label1', (-2.0,4.0), 'range1', 'river1', 'town1')
s2 = MonitoringStation('s_id2', 'm_id2', 'label2', (3.0,2.0), 'range2', 'river2', 'town2')
s3 = MonitoringStation('s_id3', 'm_id3', 'label3', (1.6,-1.6), 'range3', 'river3', 'town3')
s4 = MonitoringStation('s_id4', 'm_id4', 'label4', (0.1,0.1), 'range4', 'river3', 'town4')
test_list = [s1,s2,s3,s4]

def test_stations_by_distance():
    output = stations_by_distance(test_list,(0,0))
    #using haversine
    d1 = haversine (s1.coord, (0,0))
    d2 = haversine (s2.coord, (0,0))
    d3 = haversine (s3.coord, (0,0))
    d4 = haversine (s4.coord, (0,0))
    assert output == [(s4,d4),(s3,d3),(s2,d2),(s1,d1)]   #checks value and order
    assert type(output) == list                          #checks type
    assert len(output) == len(test_list)                 #checks length
    # Note for future tests: d1,d2,d3,d4 = 497.19868760742435, 400.8631781687255, 251.58939201339484, 15.725355061691959

def test_stations_within_radius():
    output = stations_within_radius(test_list,(0,0),260)
    d3 = haversine (s3.coord, (0,0))
    d4 = haversine (s4.coord, (0,0))
    assert output == [s4,s3]            #checks correct output
    assert type(output) == list         #checks type
    assert len(output) == 2             #checks length 

def test_rivers_with_station():
    output = rivers_with_station(test_list)
    assert output == {'river1','river2','river3'}       #checks correct output
    assert type(output) == set                          #checks type
    assert len(output) == 3                             #checks length (should ommitt duplicate)

def test_stations_by_river():
    output = stations_by_river(test_list)
    assert output == {'river1':['label1'],'river2':['label2'],'river3':['label3','label4']}      #checks correct output
    assert type(output) == dict                                                                  #checks type
    assert len(output) == 3                                                                      #checks length
