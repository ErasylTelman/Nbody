import numpy as np
import matplotlib.pyplot as plt

#This code was used to create figures in the prootocol

#function for plotting histograms of semi-major axis distribution
def plot_histogram_grid(filenames, bins=500):
    n_rows = 4 
    n_cols = 3 
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 12), constrained_layout=True)
    axes = axes.flatten()

    for i, filename in enumerate(filenames):
        data = np.loadtxt(filename, usecols=0)
        data = data[(data >= 2) & (data <= 3.6)]
        
        axes[i].hist(data, bins=bins)
        axes[i].axvline(x=2.502, linestyle='--', color='red')
        axes[i].axvline(x=2.825, linestyle='--', color='red')
        axes[i].axvline(x=2.958, linestyle='--', color='red')
        axes[i].axvline(x=3.279, linestyle='--', color='red')

        axes[i].set_title(f't = {i}e5 Myr', fontsize=14)
        if i >= 8:
            axes[i].set_xlabel('Semi-Major Axis (AU)', fontsize=12)
        if i % n_cols == 0:
            axes[i].set_ylabel('Number of Bodies', fontsize=12)
        axes[i].grid(True, linestyle='--', alpha=0.5)
    
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.suptitle('Histograms of Semi-Major Axis Values Over Time', fontsize=20)
    plt.show()

filenames = [f'orbits_t{i}.txt' for i in range(11)]
plot_histogram_grid(filenames, bins=500)

#function for plotting scatter plots of eccentricity vs semi-major axis
def plot_scatter_grid(filenames):
    n_rows = 4
    n_cols = 3 
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 12), constrained_layout=True)
    axes = axes.flatten()

    for i, filename in enumerate(filenames):
        a_data = np.loadtxt(filename, usecols=0)
        e_data = np.loadtxt(filename, usecols=1)

        mask = (a_data >= 2) & (a_data <= 3.6)
        a_data_filtered = a_data[mask]
        e_data_filtered = e_data[mask]

        axes[i].scatter(a_data_filtered, e_data_filtered, s=5)
        axes[i].axvline(x=2.502, linestyle='--', color='red')
        axes[i].axvline(x=2.825, linestyle='--', color='red')
        axes[i].axvline(x=2.958, linestyle='--', color='red')
        axes[i].axvline(x=3.279, linestyle='--', color='red')

        axes[i].set_title(f't = {i}e5 Myr', fontsize=14)
        if i >= 8:
            axes[i].set_xlabel('Semi-Major Axis (AU)', fontsize=12)
        if i % n_cols == 0:
            axes[i].set_ylabel('Eccentricity', fontsize=12)
        axes[i].grid(True)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.suptitle('Eccentricity vs. Semi-Major Axis Over Time', fontsize=20)
    plt.show()

filenames = [f'orbits_t{i}.txt' for i in range(11)]
plot_scatter_grid(filenames)
