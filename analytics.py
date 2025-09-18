from data_handler import load_data
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def calculate_summary():
    df = load_data()
    if df.empty:
        return 0, 0, 0
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    savings = total_income - total_expense
    return total_income, total_expense, savings

def expenses_by_category():
    df = load_data()
    if df.empty:
        return None
    expense_data = df[df['Type'] == 'Expense']
    if expense_data.empty:
        return None
    return expense_data.groupby('Category')['Amount'].sum()

def train_predict_expenses():
    df = load_data()
    if df.empty:
        return None, None

    df = df[df["Type"] == "Expense"]
    if df.empty:
        return None, None

    df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M").astype(str)
    monthly = df.groupby("Month")["Amount"].sum().reset_index()

    monthly["MonthIndex"] = np.arange(len(monthly))

    X = monthly[["MonthIndex"]]
    y = monthly["Amount"]
    model = LinearRegression()
    model.fit(X, y)

    next_month = [[len(monthly)]]
    prediction = model.predict(next_month)[0]

    return monthly, round(prediction, 2)
