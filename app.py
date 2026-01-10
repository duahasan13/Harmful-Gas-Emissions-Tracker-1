import streamlit as st

st.set_page_config(page_title="Harmful Gas Emissions Tracker", layout="centered")

st.title("Harmful Gas Emissions Tracker")
st.caption("Monthly household/individual emissions for CO₂, Methane (CH₄), and Nitrogen Oxides (NOₓ)")

st.header("Your Inputs")

# User Inputs
country = st.selectbox("Country of residence", ["UAE", "USA", "UK", "Canada", "Other"])
house_area = st.number_input("House area (m²)", 10, 1000000, 120)

electricity = st.number_input("Monthly electricity usage (kWh)", 0, 2000000, 900)
gas = st.number_input("Monthly gas usage (kWh or m³)", 0, 2000000, 300)

st.subheader("Transport")
car_km = st.number_input("Distance traveled by car (km/month)", 0, 1000000, 500)
bus_km = st.number_input("Distance traveled by bus (km/month)", 0, 1000000, 200)

st.subheader("Recycling")
recycling_rate = st.slider("Recycling rate (%)", 0, 100, 25)

# Calculate emissions
if st.button("Calculate emissions"):
    # CO₂ emissions (kg)
    co2_energy = electricity * 0.4 + gas * 0.2
    co2_transport = car_km * 0.21 + bus_km * 0.05
    co2_total = co2_energy + co2_transport

    # Methane emissions (kg)
    methane = (1 - recycling_rate / 100) * 0.5 

    # NOx emissions (kg)
    nox = car_km * 0.0007 

    # Display results
    st.subheader("Monthly Emissions")
    st.write(f"CO₂: {co2_total:.2f} kg")
    st.write(f"Methane (CH₄): {methane:.2f} kg")
    st.write(f"Nitrogen Oxides (NOₓ): {nox:.4f} kg")

    st.subheader("Breakdown")
    st.write(f"Energy CO₂: {co2_energy:.2f} kg")
    st.write(f"Transport CO₂: {co2_transport:.2f} kg")
