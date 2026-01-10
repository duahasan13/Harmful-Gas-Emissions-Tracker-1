import streamlit as st
from emissions import calculate_house_emissions, calculate_vehicle_emissions, calculate_recycling_score

st.title("Harmful Gas Emissions Tracker")
st.caption("Estimate your household's emissions for CO₂, Methane, and NOₓ")

# House energy
HouseE = st.number_input("Monthly house energy consumption (kWh)", 0, 20000, 900)
PersonalT = st.selectbox("Do you have personal renewable energy sources?", ["No", "Yes"])
PersonalE = 0
if PersonalT == "Yes":
    PersonalE = st.number_input("Monthly energy from personal sources (kWh)", 0, HouseE, 0)

# Gas
HouseG = st.number_input("Monthly gas consumption", 0, 20000, 300)
Gmeasure = st.selectbox("Is gas measured in volume (m³/ft³) or energy (kWh)?", ["kWh", "volume"])
G_in_kwh = True
if Gmeasure == "volume":
    m3_check = st.selectbox("Is it in m³?", ["No", "Yes"])
    if m3_check == "Yes":
        G_in_kwh = False
    else:
        HouseG *= 0.3113

# House area
HouseA = st.number_input("House area", 10, 1000, 120)
Areaunit = st.selectbox("Is the area in ft²?", ["No", "Yes"])
Area_in_m2 = True if Areaunit == "No" else False

HouseT, HouseA_m2 = calculate_house_emissions(HouseE, PersonalE, HouseG, G_in_kwh, HouseA, Area_in_m2)

# Vehicles
VehicleNum = st.number_input("Number of vehicles", 0, 10, 1)
VehicleDistance = []
VehicleDistance_in_km = []
for count in range(VehicleNum):
    dist = st.number_input(f"Vehicle {count+1} yearly distance", 0, 100000, 1000)
    VehicleDistance.append(dist)
    dist_unit = st.selectbox(f"Is vehicle {count+1} distance in miles?", ["No", "Yes"], key=f"unit{count}")
    VehicleDistance_in_km.append(False if dist_unit == "Yes" else True)

VehicleEmissions = calculate_vehicle_emissions(VehicleDistance, VehicleDistance_in_km)

# Recycling
Recycling = ["Paper and Cardboard", "Plastic", "Glass", "Metals"]
Recyclescale = []
for item in Recycling:
    scale = st.slider(f"How often do you recycle {item}?", 1, 5, 3)
    Recyclescale.append(scale)

RecyclingScore = calculate_recycling_score(Recyclescale)

# Display results
st.header("Results")
st.write(f"Total household energy consumption (kWh): {HouseT:.2f}")
st.write(f"House area in m²: {HouseA_m2:.2f}")
st.write(f"Vehicle distances (km): {VehicleEmissions}")
st.write(f"Recycling score: {RecyclingScore}")
