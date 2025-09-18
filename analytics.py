from data_handler import load_data

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
