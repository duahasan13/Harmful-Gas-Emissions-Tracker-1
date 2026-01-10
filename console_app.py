from emissions import calculate_house_emissions, calculate_vehicle_emissions, calculate_recycling_score

# House energy
HouseE = float(input("How much energy does your house consume monthly (kWh)? "))
PersonalT = input("Do you have any personal renewable energy sources? (Yes or No) ").lower()
PersonalE = 0
if PersonalT == "yes":
    PersonalE = float(input("How much of your monthly house consumption comes from this source? "))

# Gas
HouseG = float(input("How much gas does your home consume monthly? "))
Gmeasure = input("Is your gas consumption measured in volume (m³ or ft³) or energy (kWh)? ").lower()
G_in_kwh = True
if Gmeasure == "volume":
    m3_check = input("Is it in m³? (Yes or No) ").lower()
    if m3_check == "yes":
        G_in_kwh = False
    else:
        HouseG *= 0.3113  # ft³ to kWh

# House area
HouseA = float(input("What is the total area of the house? "))
Areaunit = input("Is the area in ft²? (Yes or No) ").lower()
Area_in_m2 = True if Areaunit == "no" else False

HouseT, HouseA_m2 = calculate_house_emissions(HouseE, PersonalE, HouseG, G_in_kwh, HouseA, Area_in_m2)

# Vehicles
VehicleNum = int(input("How many vehicles do you have? "))
VehicleType = [None] * VehicleNum
VehicleBrand = [None] * VehicleNum
VehicleModel = [None] * VehicleNum
VehicleYear = [None] * VehicleNum
VehicleFuel = [None] * VehicleNum
VehicleDistance = [None] * VehicleNum
VehicleDistance_in_km = [True] * VehicleNum 

for count in range(VehicleNum):
    print(f"\n--- Vehicle {count+1} Details ---")
    VehicleType[count] = input("What type of vehicle is it? ")
    VehicleBrand[count] = input("What brand is this vehicle? ")
    VehicleModel[count] = input("What is the model of this vehicle? ")
    VehicleYear[count] = input("What year model is this vehicle? ")
    VehicleFuel[count] = input("What type of fuel does your vehicle consume? ")
    
    dist = float(input("How much distance do you cover on this vehicle yearly? "))
    dist_unit = input("Is the distance measured in miles? (Yes or No) ").lower()
    
    if dist_unit == "yes":
        VehicleDistance[count] = dist
        VehicleDistance_in_km[count] = False
    else:
        VehicleDistance[count] = dist
        VehicleDistance_in_km[count] = True

VehicleEmissions = calculate_vehicle_emissions(VehicleDistance, VehicleDistance_in_km)

# Recycling
Recycling = ["Paper and Cardboard", "Plastic", "Glass", "Metals"]
Recyclescale = []
for item in Recycling:
    Recyclescale.append(int(input(f"On a scale of 1-5, how often do you recycle {item}? ")))

RecyclingScore = calculate_recycling_score(Recyclescale)

# Display
print("\n--- Results ---")
print(f"Total household energy consumption (kWh): {HouseT:.2f}")
print(f"Vehicle distances (km): {VehicleEmissions}")
print(f"Recycling score out of 20 : {RecyclingScore}")
