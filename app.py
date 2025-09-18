import streamlit as st
from data_handler import save_entry, load_data
from analytics import calculate_summary, expenses_by_category, train_predict_expenses
from visuals import show_expense_chart

st.set_page_config(page_title="💰 Expense Tracker", layout="centered")
st.title("💰 Expense Tracker with Prediction")

menu = ["Add Income", "Add Expense", "Show Summary"]
choice = st.sidebar.radio("Menu", menu)

if choice == "Add Income":
    st.subheader("➕ Add Income")
    category = st.text_input("Income Source")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    if st.button("Add Income"):
        if category and amount > 0:
            save_entry(category, amount, "Income")
            st.success(f"✅ Added Income: {category} - {amount}")
        else:
            st.error("⚠ Please enter valid data.")

elif choice == "Add Expense":
    st.subheader("➖ Add Expense")
    category = st.text_input("Expense Category")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    if st.button("Add Expense"):
        if category and amount > 0:
            save_entry(category, amount, "Expense")
            st.success(f"✅ Added Expense: {category} - {amount}")
        else:
            st.error("⚠ Please enter valid data.")

elif choice == "Show Summary":
    st.subheader("📊 Summary")
    df = load_data()

    if df.empty:
        st.warning("No records found. Add income or expenses first.")
    else:
        total_income, total_expense, savings = calculate_summary()
        st.metric("Total Income", f"${total_income:,.2f}")
        st.metric("Total Expense", f"${total_expense:,.2f}")
        st.metric("Savings", f"${savings:,.2f}")

        expense_by_category = expenses_by_category()
        show_expense_chart(expense_by_category)

        st.subheader("🔮 Expense Prediction")
        monthly, prediction = train_predict_expenses()
        if monthly is not None:
            st.line_chart(monthly.set_index("Month")["Amount"])
            st.success(f"Predicted Expense for Next Month: ${prediction:,.2f}")
        else:
            st.info("Not enough data for prediction.")

