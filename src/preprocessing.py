import pandas as pd

def preprocess(df):
      # Remove identifiers
    df = df.drop(
        ['RowNumber','CustomerId','Surname'], # do not provide predictive information about customer behaviour
        axis=1
    )

    # One-hot encode categorical features
    df = pd.get_dummies(
        df,
        columns=['Geography','Gender'],
        drop_first=True
    )

    return df