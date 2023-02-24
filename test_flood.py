from floodsystem.flood import *
from floodsystem.station import MonitoringStation

stations = [
    MonitoringStation('s_id1', 'm_id1', 'label1', (-2.0,4.0), (0.0073, 0.14), 'river1', 'town1'),
    MonitoringStation('s_id2', 'm_id2', 'label2', (3.0,2.0), (1.12, 1.12), 'river2', 'town2'),
    MonitoringStation('s_id3', 'm_id3', 'label3', (1.6,-1.6), (24.94, 7.51), 'river2', 'town3'),
    MonitoringStation('s_id4', 'm_id4', 'label4', (0.1,0.1), None, 'river3', 'town4'),
    MonitoringStation('s_id5', 'm_id5', 'label5', (0.1,0), (9.04, 11.68), 'river3', 'town5')
]
water_levels = [0.032, 1.2, 0.5, 2.3, 3.0]
#for i in water_levels:

def test_stations_highest_rel_level(stations, N):
    stations_highest_risk = stations_highest_rel_level(stations, 3)
    for station in stations_highest_risk:
        assert type(station[0].name) == str
        assert type(station[1]) == float
        print(station[0].name,station[1])
    assert stations_highest_risk == [('river2', 2), ('river3', 2)]     # Expected output

