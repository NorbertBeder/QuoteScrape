import pandas as pd


def from_csv(csv_file):
    df = pd.read_csv(csv_file + '.csv', index_col=[0])

    return df
