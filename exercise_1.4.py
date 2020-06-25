import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy import stats
import numpy as np
import seaborn as sb

# =============================================================================
#                                 Task 1.4
# =============================================================================
tickers = ['AXP']
start = dt.datetime(1999, 1, 1)
end = dt.datetime(2008, 12, 31)

stocks = yf.download(tickers, start, end)['Adj Close']

returns = np.log(stocks.pct_change()+1)
returns.dropna(inplace=True)

skewness = skew(returns)
e_kurtosis = kurtosis(returns) - 3

# Hypothesis test H0: skew = 0; Ha: skew =/= 0
mean = np.mean(returns)
z_returns = (mean) / np.var(returns, ddof=1)


alpha = 0.05
standard_error = (6/len(returns))**0.5
t_skewness = skewness / standard_error

p = stats.norm.ppf(alpha/2)


standard_error_k = (24/len(returns))**(1/2)
t_kurtosis = (e_kurtosis) / standard_error_k

jb = ((skewness)**2)/(6/len(returns)) + ((e_kurtosis)**2)/(24/len(returns))
p_val = stats.chi2.cdf(jb, df=2)

sb.distplot(returns, hist=True, kde=True, bins=100)