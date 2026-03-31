# --- SECTION 1: IMPORTS (Always at the very top) ---
import streamlit as st
import pandas as pd

# --- SECTION 2: THE HEADER ---
st.title("📦 Warehouse Dashboard")

# --- SECTION 3: THE NEW TABLE (Pandas) ---
st.subheader("Inventory Overview")
data = {
    'SKU': ['A101', 'B202', 'C303'],
    'Stock': [15, 40, 5],
    'Status': ['Healthy', 'Healthy', 'Low']
}
df = pd.DataFrame(data)
st.table(df) 

# --- SECTION 4: YOUR ORIGINAL CALCULATOR ---
st.divider() # Adds a nice horizontal line
st.subheader("Capacity Checker")

max_capacity = st.number_input("Total Warehouse Capacity", value=100)
current_pallets = st.number_input("Current Pallets in Stock", min_value=0)

if st.button("Check Status"):
    if current_pallets >= max_capacity:
        st.error(f"🛑 ALERT: Warehouse is at 100% capacity!")
    else:
        remaining = max_capacity - current_pallets
        st.success(f"✅ Space Available: {remaining} slots remaining.")