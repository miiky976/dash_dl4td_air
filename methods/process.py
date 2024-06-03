import pandas as pd


def process_input(data: list):
    df = pd.DataFrame({
        'p1': [data[0]],
        'p2': [data[1]],
        'p3': [data[2]],
        'p4': [data[3]],
        'T': [data[4]],
        'RH': [data[5]],
        'AH': [data[6]],
        'datetime': [data[7]]
    })
    df['datetime'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H")
    df['datetime'] = (
        df['datetime'] - pd.Timestamp("1970-01-01 00:00:00")) // pd.Timedelta('1h')

    return df
