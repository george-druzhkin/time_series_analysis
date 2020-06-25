import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy import stats
import numpy as np


# =============================================================================
#                                 Task 1.3
# =============================================================================
tickers = ['^GSPC']
start = dt.datetime(1975, 1, 1)
end = dt.datetime(2008, 12, 31)

stocks = yf.download(tickers, start, end)['Adj Close']

returns = pd.DataFrame()
returns['pct'] = stocks.pct_change()
returns['manual'] = (stocks - stocks.shift(1))/stocks
returns['log'] = np.log(stocks.pct_change() + 1)

returns.dropna(inplace=True)


std = stocks / stocks.shift(-1)
std.dropna(inplace=True)

annual_return = sum(np.log(std+1))/(2009-1975) - 1
annual_return = float(annual_return)
print("%.2f" % (annual_return))
profit = 1 * annual_return * (2009-1975)
profit = float(profit)
print("%.2f" % (profit))
