# Wildlife Carrying Capacity Calculator
 
## Purpose

This simple software provides a way to compare and contrast the population numbers and carrying capacity of multiple wildlife species. The user is able to select multiple files (currently 2) which contain time and population data. A graph is then generated to display both the numbers of each species as well as their individual carrying capacities over time.

## Screenshots

![1](https://user-images.githubusercontent.com/66743889/198642071-888c19c9-d7e3-4076-9475-876a66940cd5.png)
![2](https://user-images.githubusercontent.com/66743889/198642158-1b71e296-fb77-4aea-af68-40fe9eba0368.png)
![3](https://user-images.githubusercontent.com/66743889/198642189-4e266699-126e-4dd8-afff-72d7b9668c84.png)

## Usage

Currently the software requires some data preperation work to be completed prior to use. Currently a CSV file must be used which contains column A for 'Date' and column B for 'Population'. The first row of each column should be labelled as above. 

## TO-DO

- [x]  Improvements to error handling and testing
- [x]  Remove Zero Division Error for float values
- [x]  Test with real life population datasets
- [x]  Add the ability to add custom axis labels
- [ ]  Add the ability to autogenerate plot labels from csv files
- [x]  Improve graph appearance and behaviour - improve axis markings and custom titles
