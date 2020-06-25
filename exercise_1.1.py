import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy import stats
import numpy as np


# =============================================================================
#                                 Task 1.1
# =============================================================================
tickers = ['AXP', 'CAT', 'SBUX']
start = dt.datetime(1999, 1, 1)
end = dt.datetime(2008, 12, 31)

stocks = yf.download(tickers, start, end)['Adj Close']


### A
returns = stocks[tickers].pct_change()*100
returns.dropna(inplace=True)

parameters = pd.DataFrame(index = ['Mean', 'Var', 'Std', 'Skewness',
                                   'Excess Kurtosis', 'Min R', 'Max R'],
                          columns = tickers
                          )
parameters.loc['Mean', tickers] = returns[tickers].mean()
parameters.loc['Var', tickers] = returns[tickers].var()
parameters.loc['Std', tickers] = returns[tickers].std()
parameters.loc['Skewness', tickers] = returns[tickers].skew()
parameters.loc['Excess Kurtosis', tickers] = returns[tickers].kurtosis() - 3
parameters.loc['Min R', tickers] = returns[tickers].min()
parameters.loc['Max R', tickers] = returns[tickers].max()


### B
returns_log = np.log(stocks[tickers].pct_change()+1) * 100
returns_log.dropna(inplace=True)

parameters_log = pd.DataFrame(index = ['Mean', 'Var', 'Std', 'Skewness',
                                   'Excess Kurtosis', 'Min R', 'Max R'],
                          columns = tickers
                          )

### C
parameters_log.loc['Mean', tickers] = returns_log[tickers].mean()
parameters_log.loc['Var', tickers] = returns_log[tickers].var()
parameters_log.loc['Std', tickers] = returns_log[tickers].std()
parameters_log.loc['Skewness', tickers] = returns_log[tickers].skew()
parameters_log.loc['Excess Kurtosis',
                   tickers] = returns_log[tickers].kurtosis() - 3
parameters_log.loc['Min R', tickers] = returns_log[tickers].min()
parameters_log.loc['Max R', tickers] = returns_log[tickers].max()

### D
alpha = 0.05
    #H0: mean_log = 0
    #Ha: mean_log is not = 0
    
def test(data):
    p_val = pd.DataFrame()
    for ticker in tickers:
        SE = data.loc['Std', tickers] / len(returns)
        z = data.loc['Mean', tickers] / SE
        p_val.append(z, ignore_index=True)

    print(z)
    return p_val
            
            
p = test(parameters_log)