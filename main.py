# emissions.py
def calculate_house_emissions(HouseE, PersonalE, HouseG, G_in_kwh, HouseA, Area_in_m2):
    # Adjust house energy if personal renewable sources exist
    HouseE_adjusted = HouseE - PersonalE

    # Convert gas to kWh if needed
    if not G_in_kwh:
        HouseG = HouseG * 11  # m³ to kWh
    # else: assume already in kWh

    # Total household energy
    HouseT = HouseE_adjusted + HouseG

    # Adjust house area to m² if needed
    HouseA_m2 = HouseA if Area_in_m2 else HouseA * 0.0929

    return HouseT, HouseA_m2


def calculate_vehicle_emissions(VehicleDistance, VehicleDistance_in_km):
    # VehicleDistance = list of distances
    # VehicleDistance_in_km = list of booleans: True if in km, False if in miles
    emissions = []
    for i, dist in enumerate(VehicleDistance):
        km = dist if VehicleDistance_in_km[i] else dist * 1.609
        emissions.append(km)  # placeholder, you can multiply by emission factor later
    return emissions


def calculate_recycling_score(Recyclescale):
    # Example: higher score = more recycling, reduce methane
    # Just sum the scores
    return sum(Recyclescale)
