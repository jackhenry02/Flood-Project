# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """This method checks the typical high/low range data for consistency."""

        if self.typical_range == None or len(self.typical_range) != 2:      # Checks to see whether the typical range contains two values.
            return False
        elif type(self.typical_range[0]) != float or type(self.typical_range[1]) != float or self.typical_range[1] < self.typical_range[0]:     # Checks to see whether values are of type float and whether the 'Low Range' value is less than the 'High Range' value.
            return False
        else:
            return True
    
def inconsistent_typical_range_stations(stations):
    """This function returns a list of stations that have inconsistent data."""

    inconsistent_stations = []

    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:        # Calls the method inside of the class - MonitoringStation.
            inconsistent_stations.append(station)

    return inconsistent_stations