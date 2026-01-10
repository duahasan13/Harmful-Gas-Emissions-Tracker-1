import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Harmful Gas Emissions Footprint Calculator")

# --- Constants & Factors ---
FACTOR_ELEC = 0.4     # kg/kWh
FACTOR_GAS = 0.2      # kg/kWh
FACTOR_PETROL = 0.19  # kg/km
FACTOR_DIESEL = 0.17  # kg/km
FACTOR_HYBRID = 0.11  # kg/km
FACTOR_EV = 0.05      # kg/km

st.title(" Personal Harmful Gas Emissions Footprint Calculator")
st.markdown("Calculate your annual CO2e emissions (Carbon+Methane+Nitrogen Oxides converted into CO2e) and discover how many trees are needed to offset your impact.")

# --- Sidebar / Navigation ---
st.sidebar.header("Input Sections")
tab1, tab2, tab3, tab4 = st.tabs(["Household", "Vehicles", " Recycling", "Results"])

# --- Tab 1: Household Energy ---
with tab1:
    st.header("Household Energy Consumption")
    
    col1, col2 = st.columns(2)
    with col1:
        house_e = st.number_input("Monthly Electricity (kWh)", min_value=0.0, value=300.0)
        has_renewable = st.checkbox("I have personal renewable energy")
        personal_e = 0.0
        if has_renewable:
            personal_e = st.number_input("Renewable Contribution (kWh/month)", min_value=0.0, max_value=house_e, value=0.0)
            
    with col2:
        gas_val = st.number_input("Monthly Gas Consumption", min_value=0.0, value=50.0)
        gas_unit = st.selectbox("Gas Unit", ["kWh", "Cubic Meters (m³)", "Cubic Feet (ft³)"])
        
        # Gas Conversion logic
        if gas_unit == "Cubic Meters (m³)":
            house_g = gas_val * 11
        elif gas_unit == "Cubic Feet (ft³)":
            house_g = gas_val * 0.3113
        else:
            house_g = gas_val

    house_area = st.number_input("Total House Area", min_value=0.0, value=100.0)
    area_unit = st.radio("Area Unit", ["m²", "ft²"], horizontal=True)
    house_a_m2 = house_area if area_unit == "m²" else house_area * 0.0929

    # Calculation for House
    house_emissions_annual = ((house_e - personal_e) * FACTOR_ELEC + house_g * FACTOR_GAS) * 12

# --- Tab 2: Vehicles ---
with tab2:
    st.header("Transportation")
    num_vehicles = st.number_input("How many vehicles do you own?", min_value=0, max_value=10, step=1, value=1)
    
    vehicle_emissions_annual = 0.0
    total_km = 0.0
    
    for i in range(num_vehicles):
        with st.expander(f"Vehicle {i+1} Details", expanded=True):
            v_col1, v_col2 = st.columns(2)
            with v_col1:
                v_type = st.text_input(f"Type (e.g. SUV)", key=f"type_{i}")
                v_fuel = st.selectbox(f"Fuel Type", ["Petrol", "Diesel", "Hybrid", "Electric"], key=f"fuel_{i}")
            with v_col2:
                dist = st.number_input(f"Annual Distance", min_value=0.0, value=10000.0, key=f"dist_{i}")
                dist_unit = st.radio(f"Unit", ["km", "miles"], key=f"unit_{i}", horizontal=True)
            
            # Distance conversion
            km = dist if dist_unit == "km" else dist * 1.609
            total_km += km
            
            # Select factor
            if v_fuel == "Diesel": factor = FACTOR_DIESEL
            elif v_fuel == "Hybrid": factor = FACTOR_HYBRID
            elif v_fuel == "Electric": factor = FACTOR_EV
            else: factor = FACTOR_PETROL
            
            vehicle_emissions_annual += km * factor

# --- Tab 3: Recycling ---
with tab3:
    st.header("Recycling Habits")
    st.info("On a scale of 1 (Never) to 5 (Always), how often do you recycle:")
    
    recycling_items = ["Paper and Cardboard", "Plastic", "Glass", "Metals"]
    recycling_scores = []
    
    cols = st.columns(2)
    for idx, item in enumerate(recycling_items):
        with cols[idx % 2]:
            score = st.slider(item, 1, 5, 3)
            recycling_scores.append(score)
            
    recycling_total = sum(recycling_scores)

# --- Tab 4: Results & Report ---
with tab4:
    total_emissions = house_emissions_annual + vehicle_emissions_annual
    trees_needed = int(total_emissions / 20)

    st.header("Your Harmful Gas Emissions Footprint Report")
    
    # Big Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Emissions", f"{total_emissions:,.0f} kg")
    m2.metric("Trees to Offset", f"{trees_needed}")
    m3.metric("Recycling Score", f"{recycling_total}/20")

    st.divider()

    # Visual Breakdown
    st.subheader("Breakdown")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Household**")
        st.write(f"Annual: {house_emissions_annual:,.2f} kg CO2e")
    with col_b:
        st.write("**Transportation**")
        st.write(f"Annual: {vehicle_emissions_annual:,.2f} kg CO2e")

    # Recommendations
    st.subheader("Personalized Recommendations")
    if recycling_total < 10:
        st.warning("Your recycling score is low. Try to separate waste to reduce methane emissions from landfills.")
    elif recycling_total < 15:
        st.info("Good job on recycling! Consider looking for specialty recycling centers for electronics or textiles.")
    else:
        st.success("Excellent recycling habits! You are significantly reducing your secondary footprint.")

    if vehicle_emissions_annual > house_emissions_annual:
        st.warning("Your transport emissions are higher than your home energy. Consider carpooling or checking tire pressure to improve fuel efficiency.")


    st.balloons()

