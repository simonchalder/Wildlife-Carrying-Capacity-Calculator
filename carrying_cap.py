# Imports

import matplotlib.pyplot as plt
import pandas as pd
import numpy
from pathlib import Path, PureWindowsPath
import itertools
from tkinter import *
from tkinter import filedialog

# Function to Calculate changes between population values for population -----------------------------------------------------------------

def population_change(pop):
    pop_change = numpy.diff(pop)
    pop_change = [float(x) for x in pop_change]
    return pop_change

# Function to Calculate % growth rate in population --------------------------------------------------------------------------------------

def growth_rate(pop):
    rate = pd.Series(pop)
    change = rate.pct_change()
    return(round(change[1:], 2).tolist())

# Function to Calculate Carrying Capacity -----------------------------------------------------------------------------------------------

def calc_car_cap(r,N,cp):
 # K = (r * N * (1-N) / cp)
    C = []
    for a, b, c in itertools.zip_longest(r, N, cp):
        try:
            K = round((a * b * (1 - b) / c) * -1, 2)
            # K = b / 1 - (c / a * b) * -1
            C.append(K)
        except ZeroDivisionError:           
            K = C[-1]
            C.append(K)
    return(C)

# Function to select 1st CSV file -------------------------------------------------------------------------------------------------------

def browseFiles1():
    global filename1
    filename1 = filedialog.askopenfilename(initialdir = "C:\\", title = "Select a File", filetypes = (("CSV Files", "*.csv*"), ("all files", "*.*")))
    label.configure(text=filename1) 

# Function to select 2nd CSV file -------------------------------------------------------------------------------------------------------

def browseFiles2():
    global filename2
    filename2 = filedialog.askopenfilename(initialdir = "C:\\", title = "Select a File", filetypes = (("CSV Files", "*.csv*"), ("all files", "*.*")))
    label2.configure(text=filename2)

# Function to generate graph data using both selected files ------------------------------------------------------------------------------

def genGraph():
    print(check_var)
    if check_var.get() == 1:
        csvFile1 = pd.read_csv(filename1) # Place the contents of file 1 into a variable
        month = csvFile1['Date'].tolist() # Extract 1st column data into a list
        pop1 = csvFile1['Population'].tolist() # Extract 2nd Column data to a list

        csvFile2 = pd.read_csv(filename2) # As above for file 2
        month = csvFile2['Date'].tolist()
        pop2 = csvFile2['Population'].tolist()

        pc1 = population_change(pop1) # Run pop1 list through population_change function to create a list of changes
        lastpcval1 = pc1[-1] # get the last value in the list
        pc1.append(lastpcval1) # Append the last value again to the list as the list will have 1 fewer entries than the population list
        
        pc2 = population_change(pop2) # As above for pop2
        lastpcval2 = pc2[-1]
        pc2.append(lastpcval2)

        gr1 = growth_rate(pop1) # Run pop1 through the growth_rate function to calculate growth rate and generate a new list
        lastgrval1 = gr1[-1] # Get the last value in the list
        gr1.append(lastgrval1) # Append the last value again to the list as the list will have 1 fewer entries than the population list

        gr2 = growth_rate(pop2) # As above
        lastgrval2 = gr2[-1]
        gr2.append(lastgrval2)

        carry_capacity1 = calc_car_cap(gr1, pop1, pc1) # Perform Carrying capacity calculation on species from file 1 using gr, pop1 and pc lists generated above

        carry_capacity2 = calc_car_cap(gr2, pop2, pc2) # As above for species in file 2
        
        species1 = input1.get()
        species2 = input2.get()

        plt.plot(month,pop1, label = species1) # Plot data from file 1 population numbers

        plt.plot(month,pop2, label = species2, color = "green") # Plot data from file 2 population numbers

        plt.plot(month,carry_capacity1, label = species1 + " Carrying Capacity", color = "red", linestyle = 'dotted') # Plot carrying capacity data for species 1

        plt.plot(month,carry_capacity2, label = species2 + " Carrying Capacity", color = "orange", linestyle = 'dotted') # Plot carrying capacity data for species 2

        # plt.xticks(numpy.arange(0, len(month), 1))
        # plt.yticks(numpy.arange(0, max(pop1), 100))

        plt.title(species1 + " vs " + species1)
        
        plt.grid(True)
        
        plt.xlabel(om_var.get()) # Axis labels # Axis labels
        plt.ylabel('Population')

        plt.legend(loc="upper right") # Display graph legend

        plt.show() # Display graph

    else:
        csvFile1 = pd.read_csv(filename1) # Place the contents of file 1 into a variable
        month = csvFile1['Date'].tolist() # Extract 1st column data into a list
        pop1 = csvFile1['Population'].tolist() # Extract 2nd Column data to a list

        pc1 = population_change(pop1) # Run pop1 list through population_change function to create a list of changes
        lastpcval1 = pc1[-1] # get the last value in the list
        pc1.append(lastpcval1) # Append the last value again to the list as the list will have 1 fewer entries than the population list

        gr1 = growth_rate(pop1) # Run pop1 through the growth_rate function to calculate growth rate and generate a new list
        lastgrval1 = gr1[-1] # Get the last value in the list
        gr1.append(lastgrval1) # Append the last value again to the list as the list will have 1 fewer entries than the population list

        carry_capacity1 = calc_car_cap(gr1, pop1, pc1) # Perform Carrying capacity calculation on species from file 1 using gr, pop1 and pc lists generated above
        
        species1 = input1.get()
        
        plt.title(species1)
        
        plt.plot(month,pop1, label = species1) # Plot data from file 1 population numbers
        
        plt.plot(month,carry_capacity1, label = species1 + " Carrying Capacity", color = "red", linestyle = 'dotted') # Plot carrying capacity data for species 1
        
        plt.grid(True)
        
        plt.xlabel(om_var.get()) # Axis labels
        plt.ylabel('Population')

        plt.legend(loc="upper right") # Display graph legend

        plt.show() # Display graph

# Tkinter Frontend Code -----------------------------------------------------------------------------------------------------------------

root = Tk()
root.geometry('480x550+330+100')
root.title("W3C by Simon Chalder")

# List Creation -------------------------------------------------------------------------------------------------------------------------

month = ()
pop1 = ()
pop2 = ()

# Tkinter GUI Layout

# Title ------------------------------------------------------------------------------------------
titlelabel = Label(root, text="W3C by Simon Chalder", padx=50, pady=25) 
titlelabel.grid(column=0, row=1)

# Container Frame --------------------------------------------------------------------------------

container_frame = Frame(root)
container_frame.grid(column=0, row=2)

# Frame 1 ----------------------------------------------------------------------------------------

frame1 = LabelFrame(container_frame, text="Select First File")
frame1.grid(column=0, row=2, padx=10, pady=5)

button = Button(frame1, text='Select File', command=browseFiles1)
button.grid(column=0, row=2, columnspan=2, ipadx=30, ipady=10, padx=15, pady=15)

label = Label(frame1, text="") 
label.grid(column=1, row=3, columnspan=3)

input1 = Entry(frame1, text="Species 1: ")
input1.insert(0, 'Species 1')
input1.grid(column=3, row=2, padx=80, pady=5)

# Frame 2 ----------------------------------------------------------------------------------------

frame2 = LabelFrame(container_frame, text="Options")
frame2.grid(column=0, row=3, ipady=5, pady=5)

check_var = IntVar()

cb1 = Checkbutton(frame2, text="Check to compare 2 Species", variable = check_var, onvalue=1, offvalue=0)
cb1.grid(column=0, row=1, padx=10)

om_var = StringVar()

om_var.set("X Axis")
om = OptionMenu(frame2, om_var, "Month", " Year  ", " Day   ")
om.grid(column=1, row=1, padx=17.5, ipadx=30)

# Frame 3 ----------------------------------------------------------------------------------------

frame3 = LabelFrame(container_frame, text="Select Second File")
frame3.grid(column=0, row=4, padx=10, pady=5)

button2 = Button(frame3, text='Select file 2', command=browseFiles2)
button2.grid(column=0, row=1, columnspan=2, ipadx=30, ipady=10, padx=15, pady=15)

label2 = Label(frame3, text="")
label2.grid(column=1, row=2, columnspan=3)

input2 = Entry(frame3, text="Species 2: ")
input2.insert(0, 'Species 2')
input2.grid(column=2, row=1, padx=80, pady=5)

# Frame 4 -----------------------------------------------------------------------------------------

frame4 = LabelFrame(container_frame, text="Generate")
frame4.grid(column=0, row=5, padx=10, pady=5)

button3 = Button(frame4, text='Generate Graph', command=genGraph)
button3.grid(column=1, row=1, ipadx=30, ipady=10, padx=145, pady=15)

footlabel = Label(root, text="Distributed under the MIT License - Copyright (c) 2022 Simon Chalder", padx=50, pady=25) 
footlabel.grid(column=0, row=3,padx=5)

root.mainloop()