# Imports

import matplotlib.pyplot as plt
import pandas as pd
import numpy
from pathlib import Path, PureWindowsPath
import itertools

# Filename and Paths ---------------------------------------------------------------------------------------------------------------------

filename1 = Path('C:/Users/chald/Desktop/sample_data.csv')
path1_on_windows = PureWindowsPath(filename1)

filename2 = Path('C:/Users/chald/Desktop/pine_marten_data.csv')
path2_on_windows = PureWindowsPath(filename2)

# Read CSV Files to variables ------------------------------------------------------------------------------------------------------------

csvFile1 = pd.read_csv(filename1)

csvFile2 = pd.read_csv(filename2)

# Iterate through CSV data to lists ------------------------------------------------------------------------------------------------------

month = csvFile1['Date'].tolist()
pop1 = csvFile1['Population'].tolist()
pop2 = csvFile2['Population'].tolist()

# Function to Calculate changes between population values for population -----------------------------------------------------------------

def population_change(pop):
    pop_change = numpy.diff(pop)
    pop_change = [float(x) for x in pop_change]
    return pop_change

pc = population_change(pop1)
lastpcval = pc[-1]
pc.append(lastpcval)

# Function to Calculate % growth rate in population --------------------------------------------------------------------------------------

def growth_rate(pop):
    rate = pd.Series(pop)
    change = rate.pct_change()
    return(round(change[1:], 2).tolist())
        
gr = growth_rate(pop1)
lastgrval = gr[-1]
gr.append(lastgrval)

# Function to Calculate Carrying Capacity -----------------------------------------------------------------------------------------------

def calc_car_cap(r,N,cp):
 # K = (r * N * (1-N) / cp)
    C = []
    for a, b, c in itertools.zip_longest(r, N, cp):
        K = round((a * b * (1 - b) / c) * -1, 2)
        C.append(K)
    return(C)

carry_capacity = calc_car_cap(gr, pop1, pc)

# Graph Plot and Display ---------------------------------------------------------------------------------------------------------------

plt.plot(month,pop1, label = "Grey Squirrels")

plt.plot(month,pop2, label = "Pine Martens", color = "green")

plt.plot(month,carry_capacity, label = "Squirrel Carrying Capacity", color = "red", linestyle = 'dotted')

plt.xlabel('Month')
plt.ylabel('Population')

plt.legend()

plt.show()