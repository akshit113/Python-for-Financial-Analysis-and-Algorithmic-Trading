from pandas import read_csv


def main():
    df = read_csv(r'datasets/walmart_stock.csv', index_col='Date', parse_dates=True)
    print(df.head(20))

    print(df.info())

    # df['Date'] = to_datetime(df['Date'])
    # print(df.info())

    # mean, max, min
    # print(df.resample(rule='A').mean())  # Year End Frequency
    print(df.resample(rule='M').mean())  # Month End Frequency

    # df['Close'].resample(rule='M').mean().plot(kind='bar', figsize=(14, 4))

    # ts.show()

    print('')

    print(df.shift(periods=-1).head())

    print(df.tshift(freq='M').head())

    # df['Open'].plot(figsize=(16, 6))

    df['Open Moving Average'] = df['Open'].rolling(window=30).mean()
    df[['Open', 'Open Moving Average']].plot(figsize=(16, 6))
    df['Expanding Open Prices'] = df['Open'].expanding().mean()
    df[['Open', 'Expanding Open Prices']].plot(figsize=(16, 6))
    print('')


def first_day(entry):
    return entry[0]


if __name__ == '__main__':
    main()
