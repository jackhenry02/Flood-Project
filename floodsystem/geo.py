# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    '''function that returns list of stations and distances from point p, sorted by distnace'''
    stations_distance_list=[]
    for item in stations:           #iterates through station (the list) where for the each iteration 'item' refers to the nth thing in the list. Just neater than for in range function
        stations_distance_list.append((item,haversine(p,item.coord)))    #haversine takes two coordinates and finds distance
    stations_distance_list= sorted_by_key(stations_distance_list,1)     
    return stations_distance_list

def stations_within_radius(stations, centre, r):
    '''function that returns list of stations within a given radius of a centre'''
    distances_from_centre=stations_by_distance(stations, centre)   #list of station objects and distances from centre using previous function
    within_radius_list=[]
    for item in distances_from_centre:
        if item[1] < r:
            within_radius_list.append(item[0])
    return within_radius_list    #NB. This is a list of objects

def rivers_with_station(stations):
    '''function that returns a set of the names of rivers with a station'''
    output_list=[]
    for item in stations:
        output_list.append(item.river)
    return set(output_list)

def stations_by_river(stations):  
    '''function that returns a dictionary that maps river names to a list of station objects on a given river'''
    output_dict={}
    for item in stations:
        if item.river in output_dict:
            output_dict[item.river].append(item.name)
        else:
            output_dict[item.river]=[item.name]
    return output_dict

def rivers_by_station_number(stations, N):
    '''function that determines the rivers with the greatest number of monitoring stations'''
    river_monitoring_stations = []
    stations_by_river_dict = stations_by_river(stations)    # Calls the stations_by_river function and generates a dictionary of the river names and the locations associated with the rivers.

    for river_name, locations in stations_by_river_dict.items():
        river_monitoring_stations.append((river_name, len(locations)))      # Appends the rivers and the number of locations associated with each river.

    sorted_list = sorted_by_key(river_monitoring_stations, 1, reverse=True)     # Sorts in relation to the magnitude of the number of locations.

    output_list = []
    river_name, num = zip(*sorted_list)     # Used to seperate the variables of the tuple list into seperate lists.

    for i in range(len(sorted_list)):
        if i < N:
            pass
        elif i >= N and num[i] != num[i - 1]:
            break
        output_list.append(sorted_list[i])

    return output_list