from emissions import calculate_house_emissions, calculate_vehicle_emissions, calculate_recycling_score

# House energy
HouseE = get_float_input("How much electricity does your house consume monthly (kWh)? ")
PersonalE = 0
if get_yes_no("Do you have any personal renewable energy sources? (Yes or No) "):
    PersonalE = get_float_input("How much of your monthly house consumption comes from this source (kWh)? ")

# Gas
HouseG = get_float_input("How much gas does your home consume monthly? ")
if not get_yes_no("Is this amount in kWh? (Yes or No) "):
    if get_yes_no("Is it in cubic meters (m³)? (Yes or No) "):
        HouseG *= 11  # m³ to kWh
    else:
        print("Assuming measurement in cubic feet (ft³).")
        HouseG *= 0.3113  # ft³ to kWh

# House area
HouseA = get_float_input("What is the total area of the house? ")
if get_yes_no("Is the area in ft²? (Yes or No) "):
    HouseA *= 0.0929  # ft² to m²

HouseT = (HouseE - PersonalE) + HouseG
HouseA_m2 = HouseA

# Vehicles
VehicleNum = get_int_input("How many vehicles do you have? ")
VehicleType = [None] * VehicleNum
VehicleBrand = [None] * VehicleNum
VehicleModel = [None] * VehicleNum
VehicleYear = [None] * VehicleNum
VehicleFuel = [None] * VehicleNum
VehicleDistance = [None] * VehicleNum
VehicleDistance_in_km = [True] * VehicleNum 

for count in range(VehicleNum):
    print(f"\n--- Vehicle {count+1} Details ---")
    VehicleType[count] = input("Enter the vehicle type (e.g., Car, SUV, Truck): ")
    VehicleBrand[count] = input("Enter the brand (e.g., Toyota, Ford): ")
    VehicleModel[count] = input("Enter the model (e.g., Corolla, F-150): ")
    VehicleYear[count] = input("Enter the year of manufacture: ")
    VehicleFuel[count] = input("Enter fuel type (Petrol, Diesel, Hybrid, Electric): ")
    
    dist = get_float_input("Annual distance driven: ")
    
    if get_yes_no("Is the distance measured in miles? (Yes or No) "):
        VehicleDistance[count] = dist
        VehicleDistance_in_km[count] = False
    else:
        VehicleDistance[count] = dist
        VehicleDistance_in_km[count] = True

VehicleDistancesKm = calculate_vehicle_distances_km(VehicleDistance, VehicleDistance_in_km)

# Recycling
Recycling = ["Paper and Cardboard", "Plastic", "Glass", "Metals"]
Recyclescale = []
for item in Recycling:
    val = get_int_input(f"On a scale of 1-5, how often do you recycle {item}? ")
    val = max(1, min(5, val))  # Clamp between 1 and 5
    Recyclescale.append(val)

RecyclingScore = calculate_recycling_score(Recyclescale)

# --- Calculations ---
# Emission Factors (kg CO2e per unit)
FACTOR_ELEC = 0.4     # kg/kWh (approx grid average)
FACTOR_GAS = 0.2      # kg/kWh (natural gas)
FACTOR_PETROL = 0.19  # kg/km
FACTOR_DIESEL = 0.17  # kg/km
FACTOR_HYBRID = 0.11  # kg/km
FACTOR_EV = 0.05      # kg/km

# 1. Household Emissions (Annualized)
# HouseE is monthly electricity, HouseG is monthly gas (already in kWh)
house_emissions_annual = ((HouseE - PersonalE) * FACTOR_ELEC + HouseG * FACTOR_GAS) * 12

# 2. Vehicle Emissions
vehicle_emissions_annual = 0
for i in range(VehicleNum):
    fuel = VehicleFuel[i].lower()
    dist = VehicleDistancesKm[i]
    
    if 'diesel' in fuel:
        factor = FACTOR_DIESEL
    elif 'hybrid' in fuel:
        factor = FACTOR_HYBRID
    elif 'electric' in fuel or 'ev' in fuel:
        factor = FACTOR_EV
    else:
        factor = FACTOR_PETROL # Default to petrol
        
    vehicle_emissions_annual += dist * factor

total_emissions = house_emissions_annual + vehicle_emissions_annual

# --- Final Results Display ---
print("\n" + "="*50)
print("             CARBON FOOTPRINT REPORT")
print("="*50)

print(f"\n1. Household Energy")
print(f"   - Monthly Consumption: {HouseT:.2f} kWh")
print(f"   - Annual Emissions:    {house_emissions_annual:,.2f} kg CO2e")

print(f"\n2. Transportation ({VehicleNum} vehicles)")
print(f"   - Total Distance:      {sum(VehicleDistancesKm):,.2f} km")
print(f"   - Annual Emissions:    {vehicle_emissions_annual:,.2f} kg CO2e")

print(f"\n3. Recycling Habits")
print(f"   - Score: {RecyclingScore}/20")

# Simple recommendation based on recycling score
if RecyclingScore < 10:
    rec_msg = "Recommendation: Your recycling score is low. Try to separate waste to reduce landfill impact."
elif RecyclingScore < 15:
    rec_msg = "Recommendation: Good job on recycling! Look for more items to recycle like electronics."
else:
    rec_msg = "Recommendation: Excellent recycling habits!"
print(f"   - {rec_msg}")

print("-" * 50)
print(f"TOTAL ANNUAL CARBON FOOTPRINT: {total_emissions:,.2f} kg CO2e")
print("-" * 50)

# for user reference
trees_needed = total_emissions / 20  # Approx 20kg CO2 absorbed per tree per year
print(f"\nTo offset this amount, you would need to plant approximately {int(trees_needed)} trees this year.")
print("="*50)
