# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

stations = [
    MonitoringStation('s_id1', 'm_id1', 'label1', (-2.0,4.0), (0.0073, 0.14), 'river1', 'town1'),
    MonitoringStation('s_id2', 'm_id2', 'label2', (3.0,2.0), (1.12, 1.12), 'river2', 'town2'),
    MonitoringStation('s_id3', 'm_id3', 'label3', (1.6,-1.6), (24.94, 7.51), 'river2', 'town3'),
    MonitoringStation('s_id4', 'm_id4', 'label4', (0.1,0.1), None, 'river3', 'town4'),
    MonitoringStation('s_id5', 'm_id5', 'label5', (0.1,0), (9.04, 11.68), 'river3', 'town5')
]

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    """Assert to confirm whether this function is working correctly, taking into consideration the cases when the typical value is none and when its proportions are incorrect."""
    
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert inconsistent_stations == [stations[2], stations[3]]      # Expected output
    assert type(inconsistent_stations) == list
    assert len(inconsistent_stations) == 2

def relative_water_level_test(stations):
     for item in stations:
        assert MonitoringStation.relative_water_level(item) == None
        #while item.typical_range[1] != item.typical_range[0]:
         #   assert ((item.typical_range[1]-item.typical_range[0]))/(item.typical_range[1]-item.typical_range[0]) == 1 #breaks code for some reason