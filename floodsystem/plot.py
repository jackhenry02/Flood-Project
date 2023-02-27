import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from .analysis import polyfit
import matplotlib

def plot_water_levels(station, dates, levels):
    """Function plotting the water level data against time for a station, including plot lines for the typical low and high levels."""
    low = station.typical_range[0]
    high = station.typical_range[1]

    # Plot all the points
    plt.plot(dates, levels)
    plt.axhline(y=low, color='r')
    plt.axhline(y=high, color='g')
    
    # Add axis labels, rotate date labels and add plot title
    plt.legend(['Water Levels', 'Typical Low', 'Typical High'])
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name + " Water Levels")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()  

def plot_water_level_with_fit(station, dates, levels, p):
    #plot_water_levels(station, dates, levels), but without showing:
    low = station.typical_range[0]
    high = station.typical_range[1]

    # Plot all the points
    plt.plot(dates, levels)
    plt.axhline(y=low, color='r')
    plt.axhline(y=high, color='g')
    
    x = matplotlib.dates.date2num(dates)
    y = polyfit(dates, levels, p)[0]

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, y(x1 - x[0]))

    # Add axis labels, rotate date labels and add plot title
    plt.legend(['Water Levels', 'Typical Low', 'Typical High', 'Best Fit'])
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name + " Water Levels")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()