# Script for preprocessing data (handling missing values, outliers, etc.).

import pandas as pd

def preprocess_data(df):
    # Correct the date time feature to reflect correct datatype
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    # Fill missing values
    df.fillna(0, inplace=True)
    # Log-transform skewed columns
    df['transaction_amount'] = df['transaction_amount'].apply(lambda x: np.log1p(x))
    return df
