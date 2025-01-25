def add_features(df):
    # Example feature: is_low_amount
    df['is_low_amount'] = df['transaction_amount'] < 10
    return df
