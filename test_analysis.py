from floodsystem.analysis import *
from floodsystem.station import MonitoringStation

stations = [
    MonitoringStation('s_id1', 'm_id1', 'label1', (-2.0,4.0), (0.0073, 0.14), 'river1', 'town1'),
    MonitoringStation('s_id2', 'm_id2', 'label2', (3.0,2.0), (1.12, 1.12), 'river2', 'town2'),
    MonitoringStation('s_id3', 'm_id3', 'label3', (1.6,-1.6), (24.94, 7.51), 'river2', 'town3'),
    MonitoringStation('s_id4', 'm_id4', 'label4', (0.1,0.1), None, 'river3', 'town4'),
    MonitoringStation('s_id5', 'm_id5', 'label5', (0.1,0), (9.04, 11.68), 'river3', 'town5')
]


dates = (1,2,3,4,5,6)
levels = np.linspace(2.0, 3.0, num=len(dates))

def polyfit_test(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    output = polyfit(dates, levels, p)
    assert type(output) == tuple
    



print(polyfit_test(dates,levels, 1))