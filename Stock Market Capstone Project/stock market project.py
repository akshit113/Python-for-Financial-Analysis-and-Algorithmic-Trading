from pandas_datareader import get_data_yahoo

# comparing stock performance of tesla, general motors and ford motor company

# getting the data
tsla_df = get_data_yahoo(symbols='tsla', start='2012-01-01', end='2017-01-01')
print(tsla_df.head(100))

# visualize the data - linear plot of Open prices
tsla_df['Open'].plot(figsize=(16, 6))

# 30 Day moving averages
tsla_df['Open: 30 Day MA'] = tsla_df['Open'].rolling(30).mean()
tsla_df[['Open: 30 Day MA', 'Open']].plot(figsize=(16, 6))
print('')
