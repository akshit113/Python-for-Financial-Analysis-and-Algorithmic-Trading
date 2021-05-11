from pandas import concat, read_csv

print


def main():
    folder = f'/Users/akshitagarwal/Desktop/Python for Finance and Trading Algorithms/python-for-financial-analysis-and-trading/datasets'
    aapl_df = read_csv(folder + '/AAPL_CLOSE', parse_dates=True, index_col='Date')
    csco_df = read_csv(folder + '/CISCO_CLOSE', parse_dates=True, index_col='Date')
    ibm_df = read_csv(folder + '/IBM_CLOSE', parse_dates=True, index_col='Date')
    amzn_df = read_csv(folder + '/AMZN_CLOSE', parse_dates=True, index_col='Date')

    print(aapl_df.head())

    for df in (aapl_df, csco_df, ibm_df, amzn_df):
        df['Normed Return'] = df['Adj. Close'] / df.iloc[0]['Adj. Close']

    print(aapl_df.head())
    print('')

    """
    Allocation Details:
    AAPL - 30%
    CSCO - 20%
    AMZN - 40%
    IBM - 10%
    """

    for df, allo in zip((aapl_df, csco_df, amzn_df, ibm_df), (0.3, 0.2, 0.4, 0.1)):
        df['Allocation'] = df['Normed Return'] * allo
        df['Position Values'] = df['Allocation'] * 1000000

    print(aapl_df.head())

    portfolio_df = concat([aapl_df['Position Values'],
                           csco_df['Position Values'],
                           amzn_df['Position Values'],
                           ibm_df['Position Values']], axis=1)

    portfolio_df.columns = ['AAPL Position', 'CSCO Position', 'AMZN Position', 'IBM Position']
    portfolio_df['Total Position'] = portfolio_df.sum(axis=1)
    print(portfolio_df)

    ax = portfolio_df[['AAPL Position', 'CSCO Position', 'AMZN Position', 'IBM Position', 'Total Position']].plot(
        figsize=(16, 8))

    ax.set_ylabel('Position Values')

    """
    Calculate Daily Returns, Average Daily Returns, Std. Deviation of Returns
    to calculate Sharpe Ratio
    """

    portfolio_df['Daily Returns'] = portfolio_df['Total Position'].pct_change(1)
    average_returns = portfolio_df['Daily Returns'].mean()
    std_deviation = portfolio_df['Daily Returns'].std()

    sharpe_ratio = average_returns / std_deviation
    print(f'The sharpe ratio of portfolio is {sharpe_ratio}')

    portfolio_df[['Daily Returns']].plot(kind='kde', figsize=(6, 8))
    print('')


if __name__ == '__main__':
    main()
