import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    '''function that returns a best fit polynomial and the offset date'''
    x = matplotlib.dates.date2num(dates)
    y = levels
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])

def water_change(item, dates, levels):      #unused, possible way to figure out if water levels are rising
    '''function that returns a tuple of the station name and the gradient of a 1st degree best fit'''
    return(item.name, np.gradient(polyfit(dates, levels, 1)[0])) 