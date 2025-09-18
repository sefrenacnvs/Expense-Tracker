import streamlit as st

def show_expense_chart(expense_by_category):
    if expense_by_category is not None:
        st.write("### Expenses by Category")
        st.bar_chart(expense_by_category)
    else:
        st.info("No expense data to display.")
