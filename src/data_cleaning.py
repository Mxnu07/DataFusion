import pandas as pd

def clean_data(df):
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Fill missing values
    df.fillna('', inplace=True)
    return df

def flatten_location(df):
    if 'location' in df.columns:
        df['city'] = df['location'].apply(lambda loc: loc['City'] if loc else '')
        df['country'] = df['location'].apply(lambda loc: loc['Country'] if loc else '')
        df.drop(columns=['location'], inplace=True)
    return df

def handle_missing_values(df, column):
    """
    Ensure there are no missing values in the key column.
    If the column is missing, create it and fill missing values.
    """
    if column not in df.columns:
        print(f"Warning: '{column}' not found in DataFrame, creating it.")
        df[column] = ''

    df[column] = df[column].fillna('')
    return df