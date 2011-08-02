## Author: John Stachurski
## Filename: nikkei_plot.py

from __future__ import division
import pylab

# First let's create some functions 

def percent_change(data):
    """ 
    Calculates change in percentages from one data point to the next,  
    where data is an array of numbers.
    """
    percent_change = []
    for next, current in zip(data[1:], data[:-1]):
        percent_change.append(100 * (next - current) / current)
    return percent_change

def seriesplot(data):
    pylab.plot(data)
    pylab.show()

def returnsplot(start_year, end_year, data, dates):
    """
    Plots daily returns from start_year to end_year.
    Parameters: start_year and end_year are integers from 1984 to 2008.  data
    is the price data as a list of floats, and dates is the corresponding list
    of dates.  Each date is a string in the format YYYY-MM-DD.
    """
    plotvals = []
    for value, date in zip(values, dates):
        year = int(date.split('-')[0])  # extract the year
        if start_year <= year <= end_year:
            plotvals.append(value)
    seriesplot(percent_change(plotvals))

def densityplot(data):
    """
    Plots a histogram of daily returns from data, plus fitted normal density.
    """
    dailyreturns = percent_change(data)
    pylab.hist(dailyreturns, bins=200, normed=True)
    m, M = min(dailyreturns), max(dailyreturns)
    mu = pylab.mean(dailyreturns)
    sigma = pylab.std(dailyreturns)
    grid = pylab.linspace(m, M, 100)
    densityvalues = pylab.normpdf(grid, mu, sigma)
    pylab.plot(grid, densityvalues, 'r-')
    pylab.show()

def monthly_returns(data, dates):
    plotdata = []
    # Append the first data entry for plotting
    plotdata.append(data[0])
    # Get the month corresponding to the first data entry
    month = dates[0].split('-')[1]
    for value, date in zip(data, dates):
        current_month = date.split('-')[1]
        if current_month == month:
            pass  # Do nothing
        else:
            plotdata.append(value)
            month = current_month
    seriesplot(plotdata)
