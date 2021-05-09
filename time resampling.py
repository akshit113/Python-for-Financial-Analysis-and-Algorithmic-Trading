from pandas import read_csv


def main():
    df = read_csv(r'datasets/walmart_stock.csv', index_col='Date', parse_dates=True)
    print(df.head(20))

    print(df.info())

    # df['Date'] = to_datetime(df['Date'])
    # print(df.info())

    print(df.resample(rule='A').mean())  # Year End Frequency
    print(df.resample(rule='M').mean())  # Month End Frequency


if __name__ == '__main__':
    main()
