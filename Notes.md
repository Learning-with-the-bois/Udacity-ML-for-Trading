# Machine Learning for Trading

## Lesson 0: Introduction

A starting point for automatic trading.
3 parts of the course:
1. Manipulating Financial Data in Python
2. Computational Investing
3. Learning Algorithms for Trading

3 Books to Use
* Python for Finance
* What Hedge Funds Really Do
* Machine Learning by Mitchell

Will use Numpy, Scipy, Matplotlib, but mainly Pandas.

<sub>Date: March 5, 2023. Time spent: 1 hour. Total: 1 hour_</sub>

## Lesson 1.1: Reading and Plotting Stock Data

CSV = Comma-Separated-Values
Contains a header and data organized into rows and columns, divided by commas.

Panda’s library: https://pandas.pydata.org/
Matplotlib library: https://matplotlib.org/

* Quiz 1.1: Had to print the last 5 rows of a stock data frame that was read. Used .tail method of panda for n=5. Also could have done dataframe[-5:] by treating it as a list and doing slicing on it.

Can also use the name of the column as if it were a dictionary. Can use commas to retrieve more than one column.

* Quiz 1.2: Calculated the mean volume of different stocks using .mean().

Matplotlib to plot data, use .plot() and .show() to create it. Check library for further improvements of the graph (title, x/y-axis, colors, legend, etc.)

* Quiz 1.3: Plotted the ‘High’ data column from the data and added some details

<sub>Date: March 6, 2023. Time spent: 0.5 hours. Total: 1.5 hours</sub>

## 1.2 Working with multiple stocks


