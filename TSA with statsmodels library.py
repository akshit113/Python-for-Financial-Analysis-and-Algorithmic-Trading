from pandas import Index, read_csv
from statsmodels.api import datasets, tsa


def main():
    df = datasets.macrodata.load_pandas().data
    print(df.head())
    print(df.shape)

    print(datasets.macrodata.NOTE)  # print info about df
    index = Index(
        tsa.datetools.dates_from_range(start='1959Q1', end='2009Q3'))  # creates date indexes for dataframe row
    df.index = index

    df['realgdp'].plot(figsize=(16, 6))

    # use hpfilter to generate cycles and trends
    gdp_cycle, gdp_trend = tsa.filters.hpfilter(df['realgdp'])
    df['GDP Trend'] = gdp_trend

    ax = df[['realgdp', 'GDP Trend']].plot(figsize=(16, 8))
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP")

    """
    ETS - Error Trend Seasonality
    EWMA - Exponential Weighted Moving Average
    """

    airline_df = read_csv('datasets/airline_passengers.csv')
    airline_df.dropna(inplace=True)
    print(airline_df.head())
    index = Index(tsa.datetools.dates_from_range(start='1949M1', end='1960M12'))
    airline_df.index = index

    airline_df['6-month-SMA'] = airline_df['Thousands of Passengers'].rolling(window=6).mean()
    airline_df['12-month-SMA'] = airline_df['Thousands of Passengers'].rolling(window=12).mean()

    ax = airline_df[['6-month-SMA', '12-month-SMA', 'Thousands of Passengers']].plot(figsize=(16, 8))
    ax.set_xlabel("Year")
    ax.set_ylabel("Thousands of Passengers")

    airline_df['12-Month EWMA'] = airline_df['Thousands of Passengers'].ewm(span=12).mean()
    ax = airline_df[['12-Month EWMA', 'Thousands of Passengers']].plot(figsize=(16, 8))
    ax.set_ylabel('Thousands of Passengers')
    ax.set_xlabel('Years')
    print('')


if __name__ == '__main__':
    main()
