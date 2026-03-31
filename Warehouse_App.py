import streamlit as st

# 1. App Header
st.title("📦 Warehouse Capacity Tracker")
st.write("Enter the current stock to check warehouse status.")

# 2. User Inputs (The Sidebar or Main Page)
max_capacity = st.number_input("Total Warehouse Capacity", value=100)
current_pallets = st.number_input("Current Pallets in Stock", min_value=0)

# 3. Logic & Interaction
if st.button("Check Status"):
    if current_pallets >= max_capacity:
        st.error(f"🛑 ALERT: Warehouse is at 100% capacity!")
        st.warning("Action Required: Reroute incoming shipments immediately.")
    else:
        remaining = max_capacity - current_pallets
        utilization = (current_pallets / max_capacity) * 100
        
        st.success(f"✅ Space Available: {remaining} slots remaining.")
        st.progress(utilization / 100) # Visual progress bar
        st.write(f"Current Utilization: **{utilization:.1f}%**")