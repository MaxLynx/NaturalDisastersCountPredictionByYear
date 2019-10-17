import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def regression(t, f, function, xlabels, xlim_added=10, ylim_added=10):
    c = np.dot(f, function(t)) / np.dot(function(t), function(t))
    print("Coefficient: " + str(c))
    y = c * function(t)
    error = np.sum((f - y) ** 2) ** (1/2)
    print("Approximation error: " + str(error))
    plt.plot(f, color='green')
    plt.plot(y, color='red')
    plt.xlim(t[0] - xlim_added, t[-1] + xlim_added)
    plt.ylim(np.min(f) - ylim_added, np.max(f) + ylim_added)
    plt.xticks(t, xlabels, rotation='vertical')
    plt.show()


deseases_data = pd.read_csv('number-of-natural-disaster-events.csv')
deseases_data = deseases_data[deseases_data['Entity'] == 'All natural disasters']
data_sequence = np.array(deseases_data['Number of reported natural disasters (reported disasters)'])
time_sequence = np.array([time for time in range(len(data_sequence))])
regression(time_sequence, data_sequence, lambda x: x, [str(1900 + number) if (1900 + number) % 10 == 0
                                                       else ""
                                                       for number in range(len(data_sequence))])