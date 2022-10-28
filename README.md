# Wildlife Carrying Capacity Calculator
 
## Purpose

This simple software provides a way to compare and contrast the population numbers and carrying capacity of multiple wildlife species. The user is able to select multiple files (currently 2) which contain time and population data. A graph is then generated to display both the numbers of each species as well as their individual carrying capacities over time.

## Screenshots

![1](https://user-images.githubusercontent.com/66743889/198626975-05262b6c-e0fc-4a86-ac39-0556f008b8e6.png)
![2](https://user-images.githubusercontent.com/66743889/198627101-348ab6d2-93b8-4d5a-8d9f-6b5904d38a5b.png)
![3](https://user-images.githubusercontent.com/66743889/198627137-92fdd145-0b3e-4f2b-acdc-4bc54b51b57a.png)

## Usage

Currently the software requires some data preperation work to be completed prior to use. Currently a CSV file must be used which contains column A for 'Date' and column B for 'Population'. The first row of each column should be labelled as above. 

## TO-DO

- [x]  Improvements to error handling and testing
- [x]  Remove Zero Division Error for float values
- [ ]  Adjust data inputs to match actual population datasets
- [x]  Add the ability to add custom axis labels
- [ ]  Add the ability to autogenerate plot labels from csv files
- [x]  Improve graph appearance and behaviour - improve axis markings and custom titles
