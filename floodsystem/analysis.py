import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])



#dt = 10
#dates, levels = data.fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))
'''stations=build_station_list()  # Makes list of stations
    update_water_levels(stations)
    number_of_stations = 5

    stations_highest_risk = stations_highest_rel_level(stations, number_of_stations)

    for station in stations_highest_risk:
        dates, levels = fetch_measure_levels(station[0].measure_id, datetime.timedelta(days=10))
        plot_water_levels(station[0], dates, levels)'''