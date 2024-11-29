"""Functions helper for data merge."""
import pandas as pd

def consolidate_columns(df, column_name):
    """
    Consolidate duplicated columns from outer joins, e.g., 'id_x' and 'id_y' into 'id'.
    """
    if f'{column_name}_x' in df.columns and f'{column_name}_y' in df.columns:
        df[column_name] = df[f'{column_name}_x'].fillna(df[f'{column_name}_y'])  # Consolidate _x and _y
        df.drop(columns=[f'{column_name}_x', f'{column_name}_y'], inplace=True)  # Drop redundant columns
    return df

def ensure_id_first_column(df):
    # Ensure 'id' is the first column if it exists in the DataFrame
    if 'id' in df.columns:
        # Create a list of columns with 'id' first
        columns = ['id'] + [col for col in df.columns if col != 'id']
        df = df[columns]
    else:
        print("Error: 'id' column not found in DataFrame.")
    return df

