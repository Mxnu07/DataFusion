import pandas as pd
# from sqlalchemy import create_engine

def save_to_csv(data, filename="unified_data.csv"):
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
