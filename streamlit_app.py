import os
import streamlit as st
import google.generativeai as genai

# Load API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Error: GEMINI_API_KEY not found in environment variables.")
else:
    client = genai.Client(api_key=api_key)

    # Example variables (replace these with your existing variables in your code)
    # VehicleNum, VehicleYear, VehicleBrand, VehicleModel, VehicleType, VehicleFuel, VehicleEmissions
    # HouseT, HouseA_m2, RecyclingScore

    vehicle_summary = ""
    for i in range(VehicleNum):
        vehicle_summary += (
            f"- {VehicleYear[i]} {VehicleBrand[i]} {VehicleModel[i]} ({VehicleType[i]}), "
            f"Fuel: {VehicleFuel[i]}, Distance: {VehicleEmissions[i]:.2f} km/year\n"
        )

    prompt = (
        f"Based on the following data, calculate the estimated annual carbon footprint (in kg CO2e) "
        f"and provide recommendations:\n\n"
        f"Household Monthly Energy (Electricity + Gas): {HouseT:.2f} kWh\n"
        f"House Area: {HouseA_m2:.2f} m²\n"
        f"Vehicles:\n{vehicle_summary}"
        f"Recycling Score: {RecyclingScore}/20\n"
    )

    try:
        st.write("\n--- Gemini Analysis ---")
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", contents=prompt
        )
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
    
from emissions import calculate_house_emissions, calculate_vehicle_emissions, calculate_recycling_score

st.title("Harmful Gas Emissions Tracker")
st.caption("Estimate your household's emissions for CO₂, Methane, and NOₓ")

# House energy
HouseE = st.number_input("Monthly house energy consumption (kWh)", 0, 2000000000, 900)
PersonalT = st.selectbox("Do you have personal renewable energy sources?", ["No", "Yes"])
PersonalE = 0
if PersonalT == "Yes":
    PersonalE = st.number_input("Monthly energy from personal sources (kWh)", 0, HouseE, 0)

# Gas
HouseG = st.number_input("Monthly gas consumption", 0, 2000000000000, 300)
Gmeasure = st.selectbox("Is gas measured in volume (m³/ft³) or energy (kWh)?", ["kWh", "volume"])
G_in_kwh = True
if Gmeasure == "volume":
    m3_check = st.selectbox("Is it in m³?", ["No", "Yes"])
    if m3_check == "Yes":
        G_in_kwh = False
    else:
        HouseG *= 0.3113

# House area
HouseA = st.number_input("House area", 10, 5000000, 120)
Areaunit = st.selectbox("Is the area in ft²?", ["No", "Yes"])
Area_in_m2 = True if Areaunit == "No" else False

HouseT, HouseA_m2 = calculate_house_emissions(HouseE, PersonalE, HouseG, G_in_kwh, HouseA, Area_in_m2)

# Vehicles
VehicleNum = st.number_input("Number of vehicles", 0, 1000000000, 1)
VehicleType = []
VehicleBrand = []
VehicleModel = []
VehicleYear = []
VehicleFuel = []
VehicleDistance = []
VehicleDistance_in_km = []
for count in range(VehicleNum):
    st.subheader(f"Vehicle {count+1} Details")

    v_type = st.text_input("Vehicle type", key=f"type_{count}")
    v_brand = st.text_input("Brand", key=f"brand_{count}")
    v_model = st.text_input("Model", key=f"model_{count}")
    v_year = st.text_input("Year model", key=f"year_{count}")
    v_fuel = st.text_input("Fuel type", key=f"fuel_{count}")

    dist = st.number_input(
        "Yearly distance",
        min_value=0.0,
        step=100.0,
        key=f"dist_{count}"
    )

    dist_unit = st.selectbox(
        "Is this distance in miles?",
        ["No", "Yes"],
        key=f"unit_{count}"
    )

    # Store values
    VehicleType.append(v_type)
    VehicleBrand.append(v_brand)
    VehicleModel.append(v_model)
    VehicleYear.append(v_year)
    VehicleFuel.append(v_fuel)
    VehicleDistance.append(dist)
    VehicleDistance_in_km.append(False if dist_unit == "Yes" else True)

if VehicleNum > 0:
    VehicleEmissions = calculate_vehicle_emissions(
        VehicleDistance,
        VehicleDistance_in_km
    )

# Recycling
Recycling = ["Paper and Cardboard", "Plastic", "Glass", "Metals"]
Recyclescale = []
for item in Recycling:
    scale = st.slider(f"How often do you recycle {item}?", 1, 5, 3)
    Recyclescale.append(scale)

RecyclingScore = calculate_recycling_score(Recyclescale)

# Display 
st.header("Results")
st.write(f"Total household energy consumption (kWh): {HouseT:.2f}")
st.write(f"Vehicle distances (km): {VehicleEmissions}")
st.write(f"Recycling score: {RecyclingScore}")
