import pandas as pd
from helpers import ensure_id_first_column, consolidate_columns


def merge_data(json_data, transfers_data, yaml_data, promotions_data, transactions_data):
    """
    Merge data from multiple sources.
    """
    # Merge json_data and promotions_data on 'email' and 'client_email'
    merged_data = pd.merge(json_data, promotions_data, left_on='email', right_on='client_email', how='outer')

    # Consolidate 'id' and 'telephone' columns using the helper function
    merged_data = consolidate_columns(merged_data, 'id')
    merged_data = consolidate_columns(merged_data, 'telephone')

    # Ensure 'id' and 'sender_id' columns are strings before merging
    merged_data['id'] = merged_data['id'].astype(str)
    transfers_data['sender_id'] = transfers_data['sender_id'].astype(str)

    # Merge with yaml_data on 'id'
    merged_data = pd.merge(merged_data, yaml_data, on='id', how='outer')

    # Merge with transactions_data on 'telephone'
    merged_data = pd.merge(merged_data, transactions_data, left_on='telephone', right_on='phone', how='outer')

    # Merge with transfers_data on 'sender_id'
    merged_data = pd.merge(merged_data, transfers_data, left_on='id', right_on='sender_id', how='outer')

    if 'id' in merged_data.columns:
        # Sort by 'id'
        merged_data = merged_data.sort_values(by='id', ascending=True)
        # Reorder columns to make 'id' first
        merged_data = ensure_id_first_column(merged_data)
    else:
        print("Error: 'id' column not found in merged_data.")

    return merged_data
