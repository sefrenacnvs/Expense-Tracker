import pandas as pd
from datetime import datetime

FILE_NAME = "expenses.csv"

def load_data():
    try:
        return pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])
        df.to_csv(FILE_NAME, index=False)
        return df

def save_entry(category, amount, entry_type):
    df = load_data()
    date = datetime.now().strftime("%Y-%m-%d")
    new_entry = pd.DataFrame([[date, category, amount, entry_type]],
                             columns=["Date", "Category", "Amount", "Type"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
