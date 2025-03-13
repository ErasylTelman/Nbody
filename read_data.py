import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(filename, bins=100):
    data = np.loadtxt(filename, usecols=0)
    
    data = data[(data >= 2) & (data <= 3.5)]
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.xlabel('Semi-Major Axis (a)', fontsize=14)
    plt.ylabel('Number of Bodies', fontsize=14)
    plt.title('Histogram of Semi-Major Axis Values', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.axvline(x = 2.502, linestyle = '--', color = 'red')
    plt.axvline(x = 2.825, linestyle = '--', color = 'red')
    plt.axvline(x = 2.958, linestyle = '--', color = 'red')
    plt.axvline(x = 3.279, linestyle = '--', color = 'red')
    
    plt.show()

plot_histogram('orbits_t10.txt', bins=100)