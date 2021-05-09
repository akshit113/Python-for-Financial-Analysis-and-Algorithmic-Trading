from pandas import concat
from pandas_datareader import get_data_yahoo

# comparing stock performance of tesla, general motors and ford motor company

# getting the data
tsla_df = get_data_yahoo(symbols='tsla', start='2012-01-01', end='2017-01-01')
gm_df = get_data_yahoo(symbols='gm', start='2012-01-01', end='2017-01-01')
f_df = get_data_yahoo(symbols='f', start='2012-01-01', end='2017-01-01')
print(tsla_df.head(100))
print(gm_df.head(100))
print(f_df.head(100))

open_df = concat([tsla_df['Open'], gm_df['Open'], f_df['Open']], axis=1)
# open_df['Date'] = to_datetime(open_df['Date'])
# open_df = open_df.loc['2016-01-01':'2017-01-01', :]
open_df.columns = ['TSLA', 'GM', 'FORD']


# visualize the data - linear plot of Open prices
ax = open_df[['TSLA', 'GM', 'FORD']].plot(figsize=(16, 6))
ax.set_xlabel("Trade Date")
ax.set_ylabel("Open Prices")

# 30 Day moving averages
tsla_df['Open: 30 Day MA'] = tsla_df['Open'].rolling(30).mean()
tsla_df[['Open: 30 Day MA', 'Open']].plot(figsize=(16, 6))
print('')
