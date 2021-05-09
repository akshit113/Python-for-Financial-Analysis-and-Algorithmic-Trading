from pandas import Index
from statsmodels.api import datasets, tsa


def main():
    df = datasets.macrodata.load_pandas().data
    print(df.head())
    print(df.shape)

    print(datasets.macrodata.NOTE)  # print info about df
    index = Index(
        tsa.datetools.dates_from_range(start='1959Q1', end='2009Q3'))  # creates date indexes for dataframe row
    df.index = index

    ax = df['realgdp'].plot(figsize=(16, 6))
    #use hpfilter



    print('')

if __name__ == '__main__':
    main()
