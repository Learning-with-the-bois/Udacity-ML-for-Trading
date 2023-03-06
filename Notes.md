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

<sub>Date: March 5, 2023. Time spent: 1 hour. Total: 1 hour</sub>

## Lesson 1.1: Reading and Plotting Stock Data

CSV = Comma-Separated-Values. It contains a header and data organized into rows and columns, divided by commas.

Panda’s library: https://pandas.pydata.org/
Matplotlib's library: https://matplotlib.org/

* [Quiz 1.1](Quizzes/Quiz1_1.py): Had to print the last 5 rows of a stock data frame that was read. Used .tail method of panda for n=5. Also could have done dataframe[-5:] by treating it as a list and doing slicing.

Can also use the name of the column as if it were a dictionary. Can use commas to retrieve more than one column.

* [Quiz 1.2](Quizzes/Quiz1_2.py): Calculated the mean volume of different stocks using .mean().

Matplotlib to plot data, use .plot() and .show() to create it. Check library for further improvements of the graph (title, x/y-axis, colors, legend, etc.)

* [Quiz 1.3](Quizzes/Quiz1_3.py): Plotted the ‘High’ data column from the data and added some details

<sub>Date: March 6, 2023. Time spent: 0.5 hours. Total: 1.5 hours</sub>

## 1.2 Working with multiple stocks


