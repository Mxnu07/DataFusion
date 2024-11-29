#!/usr/bin/env python3
import pandas as pd
from data_ingestion import load_json, load_csv, load_yaml, load_xml
from data_cleaning import clean_data, flatten_location, handle_missing_values
from data_merge import merge_data
from data_persistence import save_to_csv


def main():
    # Load the data from various sources (adjust file paths accordingly)
    json_data = load_json("data/people.json")
    yaml_data = load_yaml("data/people.yml")
    promotions_data = load_csv("data/promotions.csv")
    transactions_data = load_xml("data/transactions.xml")
    transfers_data = load_csv("data/transfers.csv")

    # Clean and preprocess data
    json_data = flatten_location(clean_data(json_data))
    yaml_data = clean_data(yaml_data)
    promotions_data = clean_data(promotions_data)
    transactions_data = clean_data(transactions_data)
    transfers_data = clean_data(transfers_data)

    # Handle missing values in key columns for all dataframes
    json_data = handle_missing_values(json_data, 'id')
    yaml_data = handle_missing_values(yaml_data, 'id')
    promotions_data = handle_missing_values(promotions_data, 'id')
    promotions_data = handle_missing_values(promotions_data, 'client_email')
    json_data = handle_missing_values(json_data, 'email')


    # Convert necessary columns to strings to avoid type mismatches
    json_data['id'] = json_data['id'].astype(str)
    yaml_data['id'] = yaml_data['id'].astype(str)
    promotions_data['id'] = promotions_data['id'].astype(str)
    promotions_data['client_email'] = promotions_data['client_email'].astype(str)

    # Merge the data using updated merge logic
    unified_data = merge_data(json_data, transfers_data, yaml_data, promotions_data, transactions_data)

    # Save the unified data
    save_to_csv(unified_data, filename="data/processed/unified_data.csv")


if __name__ == "__main__":
    main()
