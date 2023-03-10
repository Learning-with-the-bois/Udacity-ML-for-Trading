# Machine Learning for Trading

## Lesson 0: Introduction

Udacity course: https://www.udacity.com/course/machine-learning-for-trading--ud501
Course website: https://lucylabs.gatech.edu/ml4t/

The course is a starting point for automatic trading. It has 3 parts:
1. Manipulating Financial Data in Python
2. Computational Investing
3. Learning Algorithms for Trading

The 3 books to be used are:
* Python for Finance
* What Hedge Funds Really Do
* Machine Learning by Mitchell

Other Materials (from website, more formal course):
* Introduciton to Statistical Learning by James, Witten, et al.
* Probabilistic Machine Learning by Kevin Murphy.
* Foundations of Deep Reinforcement Learning by Graesser and Keng.

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

## Lesson 1.2 Working with multiple stocks

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


## Lesson 1.3 The Power of Numpy

Can treat dataframes like ndarrays, but they contain many more routines.

Can access data using nd\[row,col].

Can also create different arrays with specific values using .empty(), .ones(), .zeros(), 
.random.random() and specify datatype with the parameter dtype.

Can also use random sampling that follows normal deviations. method .random.seed() to get same number generator.

Can specify in which way and operation is wanted to be made, axis=0 means rows and axis=1 equals columns.

* Quiz 1.3.1: Found the index of the maximum value in a 1D array using .argmax().
time library to calculate time. Can use time.time() and compare values.

Can access values in array with array\[row,colum], or slicing to get a range of them. It can also be used to modify the respective elements.

<sub>Date: March 8,9, 2023. Time spent: 1.5 hours. Total: 5.0 hours</sub>

## Lesson 1.4 Statistical analysis of time series

Can easily calculate statistics on pandas dataframes. There’s two types:

* Global statistics: General statistics over the whole interval, i.e mean, median, std, sum, etc.

* Rolling statistics: Statistics of a specific range of the interval done repeatedly to form a graph, i.e. rolling mean, rolling std, etc. 

Bollinger Bands: They consist on comparing the rolling mean to two standard deviations away from it, and seeing when the stock price goes outiside the range to potentially inform trading decisions.

* Quiz 1.4.1: Obtained Bollinger bands by calculating the rolling mean of the stock price and the rolling standard deviation and then added 2 of them to the rolling mean to obtain the upper limit, and subtracted 2 for the lower limit.

Daily returns: Day-to-day change in stock price. One of the most important factors used in financial analysis. It is calculated by seeing the amount the price change relative to its total price.

* Quiz 1.4.2: Calculated the daily return by dividing the current stock dataframe to one shifted by 1 space (the current vs the one on the previous day) and subtracting 1 to it. Then had to assign 0 to the first values as they couldn't be calculated.

<sub>Date: March 9, 2023. Time spent: 1.0 hour. Total: 6.0 hours</sub>

## Lesson 1.5 Incomplete Data

Stock data is not perfect. It can have gaps or missing points, and different sources can have different values. So, they are usually an amalgamation of them. Furthermore, stocks can temporarily or permanently stop or begin trading, which means there wouldn’t always be data related to them.

Fill forward/backwards is better than interpolation for filling gaps in data, as interpolation implies knowledge from the future.

To fill the missing data, can use .fillna(), use method ‘ffill’ for forward fill and 'dfill for backwards.

* Quiz 1.5.1: Used methods ffill and bfill in that order to complete the data and set inplace to True so that the values are replaced.

<sub>Date: March 10, 2023. Time spent: 0.5 hours. Total: 6.5 hours</sub>

## Lesson 1.6 Histograms and Scatter Plots

Looking at daily returns alone isn’t very useful, they should be contextualized with other stocks.

Histograms can be a valuable tool to understanding stock data. Can measure statistics like standard deviation, mean and kurtosis (how much the actual results differ from the normal distribution on the tail ends). Use .hist() to plot it.

Scatterplots can be useful to see a relation between two stocks. 

* Beta, the slope of the line in scatterplot, refers to how reactive the stock is to the market (if compared to a stock that closely follows the market, like S&P500). 

* Alpha, where the line intersects the y-axis, can tell you whether the stock is consistently performing better than the market.

* Correlation is a measure of how similarly two stocks change.

<sub>Date: March 10, 2023. Time spent: 0.5 hours. Total: 7.0 hours</sub>

## Lesson 1.8 Optimizers: Building a parametrized model 
Optimizers are algorithms that can:

•	Find minimum values of functions.

•	Build Parametrized models based on data.

•	Refine allocations to stocks in portfolios.

How to use them:

1.	Provide a function to minimize.
2.	Provide an initial guess (can provide random/standard value).
3.	Call the optimizer until it converges.

Need to use scipy.optimize (spo) to use them. Can call it using the method .minimize().

Convex (graphs) problems are the easiest to solve by minimizers. They must have only one minima and can’t have flat regions. Also, functions with discontinuities can be hard to compute.

A good question to ask is what are we minimizing? When trying to optimize some function.

<sub>Date: March 10, 2023. Time spent: 0.5 hours. Total: 7.5 hours</sub>

## Lesson 1.9 Optimizers: How to optimize a portfolio

Portfolio optimization: Given a set of assets and a time period, find an allocation of funds to assets that maximizes performance, (must define metrics on which performance is measured).

To improve optimizing speed, can provide ranges (limits on the values), and constrains (properties of x that must be true).

<sub>Date: March 10, 2023. Time spent: 0.5 hours. Total: 8.0 hours</sub>
