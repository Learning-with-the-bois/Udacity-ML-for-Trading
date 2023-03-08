# Machine Learning for Trading

## Lesson 0: Introduction

The course is a starting point for automatic trading. It has 3 parts:
1. Manipulating Financial Data in Python
2. Computational Investing
3. Learning Algorithms for Trading

The 3 books to be used are:
* Python for Finance
* What Hedge Funds Really Do
* Machine Learning by Mitchell

Throughout the course, we will use Numpy, Scipy, and Matplotlib, but mainly Pandas.

<sub>Date: March 5, 2023. Time spent: 1.0 hour. Total: 1.0 hour</sub>

## Lesson 1.1: Reading and Plotting Stock Data

CSV = Comma-Separated-Values. It contains a header and data organized into rows and columns, divided by commas.

Panda’s (pd) library: https://pandas.pydata.org/

Matplotlib's (plt) library: https://matplotlib.org/

* Quiz 1.1.1: Had to print the last 5 rows of a stock data frame that was read (using .read_csv()). Used .tail() method of panda for n=5. Also could have done dataframe[-5:] by treating it as a list and doing slicing.

Can also use the name of the column as if it were a dictionary. Can use commas to retrieve more than one column.

* Quiz 1.1.2: Calculated the mean volume of different stocks using .mean().

Matplotlib to plot data, use .plot() and .show() to create it. Check library for further improvements of the graph (title, x/y-axis, colors, legend, grid, etc.)

* Quiz 1.1.3: Plotted the ‘High’ data column from the data and added some details

<sub>Date: March 6, 2023. Time spent: 0.5 hours. Total: 1.5 hours</sub>

## 1.2 Working with multiple stocks

* Quiz 1.2.1:  Used read_csv() with several parameters -index_col, parse_dates, usecols, and na_values. Then used join() to save the desired data. Also took out the nan with the .dropna() method.

<sub>Date: March 7, 2023. Time spent: 1.0 hour. Total: 2.5 hours</sub>

Quiz 1.2.2: Graphed the appropriate columns and rows using .ix(start_date:end_date, [columns]).
To normalize you can do df/df.ix[0,:]. That is, divide each of the columns of the data set by the first value of them.

Given lesson summary is useful:

To read multiple stocks into a single dataframe, you need to:
 
 * Specify a set of dates using pandas.date_range
 
 * Create an empty dataframe with dates as index
    
    * This helps align stock data and orders it by trading date
 
 * Read in a reference stock (here SPY) and drop non-trading days using pandas.DataFrame.dropna
 
 * Incrementally join dataframes using pandas.DataFrame.join
 
Once you have multiple stocks, you can:

 * Select a subset of stocks by ticker symbols
 
 * Slice by row (dates) and column (symbols)
 
 * Plot multiple stocks at once (still using pandas.DataFrame.plot)

 * Carry out arithmetic operations across stocks, e.g. normalize by the first day's price

<sub>Date: March 8, 2023. Time spent: 1.0 hour. Total: 3.5 hours</sub>
