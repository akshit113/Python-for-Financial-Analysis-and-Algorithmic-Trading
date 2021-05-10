from pandas import Index, read_csv, to_datetime
from statsmodels.api import datasets, tsa
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller


def adf_check(df):
    result = adfuller(df)
    labels = ['ADF Test Statistic', 'p-value', '# of Lags', 'Num of Observations used']
    for key, label in zip(result, labels):
        print(f'{label} : {key}')

    if result[1] <= 0.05:
        print(
            "strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")


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

    """
    ETS (Error-Trend-Seasonality) Decomposition
    """
    result = tsa.seasonal_decompose(airline_df['Thousands of Passengers'], model='multiplicative')
    fig = result.plot()
    fig.savefig('ets.png')

    """
    ARIMA: Auto Regressive Integrated Moving Averages
    It is a generalization of ARMA. Works fantastic on predicting sales, capturing seasonality and trends.
    May not work well for historic stock data
    
    ARIMA is of two types - Seasonal ARIMA and Non-Seasonal ARIMA
    """

    milk_df = read_csv(f'datasets/monthly-milk-production-pounds-p.csv')
    milk_df.columns = ['Month', 'Milk Production']

    milk_df.dropna(inplace=True)
    milk_df['Month'] = to_datetime(milk_df['Month'])
    milk_df.set_index('Month', inplace=True)

    print(milk_df.describe().transpose())

    milk_df[['Milk Production']].plot(figsize=(16, 6))

    decomposed = seasonal_decompose(milk_df['Milk Production'], model='multiplicative')
    ax = decomposed.plot()
    ax.set_size_inches(16, 8)

    result = adfuller(milk_df['Milk Production'])

    adf_check(milk_df['Milk Production'])
    print('')


if __name__ == '__main__':
    main()
